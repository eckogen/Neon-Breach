import io
import json
import struct
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).parents[1]
GLB = ROOT / "outputs/assets/male-office-worker/characters/male-office-worker_1/male-office-worker_1.glb"
OUTPUT = ROOT / "outputs/assets/office-worker-mesh.js"


def load_glb(path):
    data = path.read_bytes()
    magic, version, length = struct.unpack_from("<III", data, 0)
    if magic != 0x46546C67 or version != 2 or length != len(data):
        raise ValueError("Expected a valid GLB 2.0 file")
    offset = 12
    chunks = {}
    while offset < length:
        size, kind = struct.unpack_from("<II", data, offset)
        offset += 8
        chunks[kind] = data[offset : offset + size]
        offset += size
    document = json.loads(chunks[0x4E4F534A].decode("utf-8").rstrip("\0 "))
    return document, chunks[0x004E4942]


def accessor(document, binary, index):
    item = document["accessors"][index]
    view = document["bufferViews"][item["bufferView"]]
    components = {"SCALAR": 1, "VEC2": 2, "VEC3": 3, "VEC4": 4}[item["type"]]
    formats = {5121: "B", 5123: "H", 5125: "I", 5126: "f"}
    fmt = "<" + formats[item["componentType"]] * components
    packed_size = struct.calcsize(fmt)
    stride = view.get("byteStride", packed_size)
    start = view.get("byteOffset", 0) + item.get("byteOffset", 0)
    return [struct.unpack_from(fmt, binary, start + i * stride) for i in range(item["count"])]


document, binary = load_glb(GLB)
primitive = document["meshes"][0]["primitives"][0]
positions = accessor(document, binary, primitive["attributes"]["POSITION"])
normals = accessor(document, binary, primitive["attributes"]["NORMAL"])
uvs = accessor(document, binary, primitive["attributes"]["TEXCOORD_0"])
indices = [value[0] for value in accessor(document, binary, primitive["indices"])]

image_view = document["bufferViews"][document["images"][0]["bufferView"]]
image_start = image_view.get("byteOffset", 0)
texture = Image.open(io.BytesIO(binary[image_start : image_start + image_view["byteLength"]])).convert("RGB")


def texture_color(uv):
    u = uv[0] % 1
    v = uv[1] % 1
    px = u * (texture.width - 1)
    py = (1 - v) * (texture.height - 1)
    x0, y0 = int(px), int(py)
    x1, y1 = min(texture.width - 1, x0 + 1), min(texture.height - 1, y0 + 1)
    tx, ty = px - x0, py - y0
    samples = [texture.getpixel((x0, y0)), texture.getpixel((x1, y0)), texture.getpixel((x0, y1)), texture.getpixel((x1, y1))]
    return tuple(
        ((samples[0][channel] * (1 - tx) + samples[1][channel] * tx) * (1 - ty)
         + (samples[2][channel] * (1 - tx) + samples[3][channel] * tx) * ty) / 255
        for channel in range(3)
    )


# Preserve every source vertex and UV seam. The earlier clustered conversion merged
# vertices that shared a position but belonged to unrelated texture-atlas islands.
vertices = [list(position) + list(normal) + list(texture_color(uv)) for position, normal, uv in zip(positions, normals, uvs)]
triangles = [value for index in indices for value in vertices[index]]


def number(value):
    rounded = round(value, 4)
    if rounded == 0:
        return "0"
    return f"{rounded:.4f}".rstrip("0").rstrip(".")


payload = ",".join(number(value) for value in triangles)
OUTPUT.write_text(
    "// Generated from the supplied male-office-worker_1.glb. Preserve the source bundle beside this file.\n"
    f"const officeNpcMesh=[{payload}];\n",
    encoding="utf-8",
)
print(f"Generated {len(triangles) // 27:,} UV-preserving triangles ({OUTPUT.stat().st_size:,} bytes)")
