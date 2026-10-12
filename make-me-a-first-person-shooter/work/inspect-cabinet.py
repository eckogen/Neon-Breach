import struct,json
from pathlib import Path
b=Path('C:/Users/Owner/Downloads/FileCabinet.glb').read_bytes();n=struct.unpack_from('<I',b,12)[0];j=json.loads(b[20:20+n]);print(json.dumps(j,indent=2)[:18000])
