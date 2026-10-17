import base64
import json
import struct
from pathlib import Path

import numpy as np


ROOT = Path(__file__).parents[1]
GLB = ROOT / "outputs/assets/female-office-worker/characters/female-office-worker/female-office-worker.glb"
OUTPUT = ROOT / "outputs/assets/female-office-worker-mesh.js"


def load_glb(path):
    data = path.read_bytes()
    magic, version, length = struct.unpack_from("<III", data, 0)
    if magic != 0x46546C67 or version != 2 or length != len(data):
        raise ValueError("Expected a valid GLB 2.0 file")
    json_size, json_kind = struct.unpack_from("<II", data, 12)
    if json_kind != 0x4E4F534A:
        raise ValueError("Missing GLB JSON chunk")
    document = json.loads(data[20 : 20 + json_size].decode("utf-8").rstrip("\0 "))
    binary_header = 20 + json_size
    binary_size, binary_kind = struct.unpack_from("<II", data, binary_header)
    if binary_kind != 0x004E4942:
        raise ValueError("Missing GLB binary chunk")
    return document, memoryview(data)[binary_header + 8 : binary_header + 8 + binary_size]


def accessor(document, binary, index):
    item = document["accessors"][index]
    view = document["bufferViews"][item["bufferView"]]
    components = {"SCALAR": 1, "VEC2": 2, "VEC3": 3, "VEC4": 4}[item["type"]]
    dtype = {5121: np.uint8, 5123: np.uint16, 5125: np.uint32, 5126: np.float32}[item["componentType"]]
    packed = np.dtype(dtype).itemsize * components
    stride = view.get("byteStride", packed)
    offset = view.get("byteOffset", 0) + item.get("byteOffset", 0)
    if stride == packed:
        return np.frombuffer(binary, dtype=dtype, count=item["count"] * components, offset=offset).reshape(-1, components)
    return np.ndarray((item["count"], components), dtype=dtype, buffer=binary, offset=offset, strides=(stride, np.dtype(dtype).itemsize)).copy()


document, binary = load_glb(GLB)
primitive = document["meshes"][0]["primitives"][0]
positions = accessor(document, binary, primitive["attributes"]["POSITION"]).astype(np.float64)
normals = accessor(document, binary, primitive["attributes"]["NORMAL"]).astype(np.float64)
uvs = accessor(document, binary, primitive["attributes"]["TEXCOORD_0"]).astype(np.float64)
faces = accessor(document, binary, primitive["indices"]).reshape(-1, 3)

# This replacement asset is already game-optimized, so preserve every supplied
# triangle and UV seam rather than applying the scan decimation used previously.
vertices = np.column_stack((positions, normals, uvs)).astype(np.float32)
triangles = vertices[faces].reshape(-1)

image = document["images"][0]
image_view = document["bufferViews"][image["bufferView"]]
image_start = image_view.get("byteOffset", 0)
image_bytes = bytes(binary[image_start : image_start + image_view["byteLength"]])
mime = image.get("mimeType", "image/png")
texture_uri = f"data:{mime};base64," + base64.b64encode(image_bytes).decode("ascii")


def number(value):
    rounded = round(float(value), 4)
    if rounded == 0:
        return "0"
    return f"{rounded:.4f}".rstrip("0").rstrip(".")


payload = ",".join(number(value) for value in triangles)
OUTPUT.write_text(
    "// Generated from the supplied office-employee2.glb; source bundle is preserved beside this file.\n"
    f"const femaleOfficeNpcMesh=[{payload}];\n"
    f"const femaleOfficeNpcTexture={json.dumps(texture_uri)};\n",
    encoding="utf-8",
)
print(
    f"Generated {len(faces):,} textured triangles "
    f"({OUTPUT.stat().st_size:,} bytes)"
)
