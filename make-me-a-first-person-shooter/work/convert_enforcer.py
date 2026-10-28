"""Build the game's WebGL assets from the supplied Enforcer character bundle."""
import base64
import io
import json
import struct
import zipfile
from pathlib import Path
import numpy as np
from PIL import Image
from scipy.spatial.transform import Rotation, Slerp

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'outputs/assets'
archive = zipfile.ZipFile(ASSETS / 'enforcer-source.zip')
prefix = 'characters/character/'
raw = archive.read(prefix + 'character.glb')
assert raw[:4] == b'glTF'
size = struct.unpack_from('<I', raw, 12)[0]
doc = json.loads(raw[20:20 + size])
binary = raw[28 + size:]

def accessor(index):
    a = doc['accessors'][index]; v = doc['bufferViews'][a['bufferView']]
    width = {'SCALAR': 1, 'VEC2': 2, 'VEC3': 3, 'VEC4': 4, 'MAT4': 16}[a['type']]
    dtype = np.dtype({5121: 'u1', 5123: '<u2', 5125: '<u4', 5126: '<f4'}[a['componentType']])
    return np.ndarray((a['count'], width), dtype=dtype, buffer=binary,
        offset=v.get('byteOffset', 0) + a.get('byteOffset', 0),
        strides=(v.get('byteStride', width * dtype.itemsize), dtype.itemsize)).copy()

def encode(array):
    assert np.isfinite(array).all()
    return base64.b64encode(np.asarray(array, dtype='<f4').tobytes()).decode()

def save(name, variable, data):
    (ASSETS / name).write_text('const ' + variable + '=' + json.dumps(data, separators=(',', ':')) + ';\n')

primitive = doc['meshes'][0]['primitives'][0]
a = primitive['attributes']; faces = accessor(primitive['indices']).ravel()
vertices = np.column_stack([accessor(a[k]) for k in ['POSITION', 'NORMAL', 'TEXCOORD_0', 'JOINTS_0', 'WEIGHTS_0']])
triangles = vertices[faces]
image = doc['images'][0]; view = doc['bufferViews'][image['bufferView']]
start = view.get('byteOffset', 0)
Image.open(io.BytesIO(binary[start:start + view['byteLength']])).convert('RGB').save(ASSETS / 'enforcer-basecolor.jpg', quality=95)
save('enforcer-mesh.js', 'enforcerAsset', {'data': encode(triangles[:, :8]), 'count': len(faces), 'textureUrl': 'assets/enforcer-basecolor.jpg'})

nodes = doc['nodes']; skin = doc['skins'][0]; joints = skin['joints']
inverse = accessor(skin['inverseBindMatrices']).reshape(-1, 4, 4).transpose(0, 2, 1)
parents = {c: i for i, n in enumerate(nodes) for c in n.get('children', [])}
base = []
for n in nodes:
    if 'matrix' in n:
        m = np.array(n['matrix']).reshape(4, 4).T
        scale = np.linalg.norm(m[:3, :3], axis=0)
        base.append((m[:3, 3], Rotation.from_matrix(m[:3, :3] / scale).as_quat(), scale))
    else:
        base.append((np.array(n.get('translation', [0, 0, 0])), np.array(n.get('rotation', [0, 0, 0, 1])), np.array(n.get('scale', [1, 1, 1]))))
manifest = json.loads(archive.read(prefix + 'manifest.json'))
profile = json.loads(archive.read(prefix + 'profiles/Enforcer.profile.json'))['profile']['prefs']
clips_by_id = {c['id']: c['file'] for c in manifest['files']['animations']}
slots = {slot: clips_by_id[clip] for slot, clip in profile['slots'].items() if clip}
slots['fire'] = 'animations/firing_an_assault_rifle.clip.json'
clips = {}
for mode, filename in slots.items():
    clip = json.loads(archive.read(prefix + filename)); duration = clip['duration']
    frames = max(1, round(duration * 30)); tracks = {}
    for track in clip['tracks']:
        bone, kind = track['name'].rsplit('.', 1)
        times = np.array(track['times']); values = np.array(track['values']).reshape(len(times), -1)
        tracks[(bone, kind)] = (times, values)
    baked = []
    for frame in range(frames):
        time = frame / 30; local = []
        for i, n in enumerate(nodes):
            t, q, scale = [v.copy() for v in base[i]]
            for kind, default in [('position', t), ('quaternion', q), ('scale', scale)]:
                track = tracks.get((n.get('name'), kind))
                if track is None: continue
                times, values = track; when = np.clip(time, times[0], times[-1])
                value = Slerp(times, Rotation.from_quat(values))([when]).as_quat()[0] if kind == 'quaternion' and len(times) > 1 else np.array([np.interp(when, times, values[:, j]) for j in range(values.shape[1])])
                if kind == 'position': t = value
                elif kind == 'quaternion': q = value
                else: scale = value
            # Game AI controls horizontal movement; remove authored root travel.
            if n.get('name') in ['root', 'pelvis']: t[[0, 2]] = base[i][0][[0, 2]]
            m = np.eye(4); m[:3, :3] = Rotation.from_quat(q).as_matrix() * scale; m[:3, 3] = t
            local.append(m)
        world = {}
        def transform(i):
            if i not in world: world[i] = transform(parents[i]) @ local[i] if i in parents else local[i]
            return world[i]
        matrices = np.array([transform(j) @ inverse[k] for k, j in enumerate(joints)])
        baked.append(matrices.transpose(0, 2, 1).reshape(-1))
    clips[mode] = {'duration': duration, 'frames': frames, 'data': encode(np.array(baked))}
save('enforcer-rig.js', 'enforcerRigAsset', {'name': 'enforcer', 'boneCount': len(joints), 'count': len(faces), 'vertices': encode(triangles), 'clips': clips})
print(f'Converted {len(faces)//3} triangles, {len(joints)} bones, clips: {list(clips)}')
