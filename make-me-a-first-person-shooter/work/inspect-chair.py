import struct,json
b=open('D:/voxChair.glb','rb').read();n,t=struct.unpack_from('<II',b,12);j=json.loads(b[20:20+n]);print(json.dumps(j,indent=2)[:18000])
