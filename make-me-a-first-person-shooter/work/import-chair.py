import json,struct,io,shutil
from pathlib import Path
from PIL import Image
b=Path('D:/voxChair.glb').read_bytes();ln=struct.unpack_from('<I',b,12)[0];j=json.loads(b[20:20+ln]);off=20+ln;binlen=struct.unpack_from('<I',b,off)[0];data=b[off+8:off+8+binlen]
def accessor(i):
 a=j['accessors'][i];v=j['bufferViews'][a['bufferView']];n={'SCALAR':1,'VEC2':2,'VEC3':3}[a['type']];fmt={5126:'f',5123:'H'}[a['componentType']];stride=v.get('byteStride',struct.calcsize(fmt)*n);start=v.get('byteOffset',0)+a.get('byteOffset',0);return [struct.unpack_from('<'+fmt*n,data,start+k*stride) for k in range(a['count'])]
v=j['bufferViews'][j['images'][0]['bufferView']];image=Image.open(io.BytesIO(data[v['byteOffset']:v['byteOffset']+v['byteLength']])).convert('RGB');pos=accessor(0);norm=accessor(1);uv=accessor(2);indices=accessor(3);verts=[]
for (i,) in indices:
 u,v=uv[i];color=image.getpixel((min(image.width-1,int(u*image.width)),min(image.height-1,int(v*image.height))));verts.extend([round(c*1.15/1.8,6) for c in pos[i]]+list(norm[i])+[round((c/255)**2.2,6) for c in color])
Path('work/chair-mesh.json').write_text(json.dumps(verts,separators=(',',':')));Path('outputs/assets').mkdir(exist_ok=True);shutil.copyfile('D:/voxChair.glb','outputs/assets/voxChair.glb');print('Converted original mesh:',len(indices)//3,'triangles; texture',image.size,'; height 1.15 meters')
