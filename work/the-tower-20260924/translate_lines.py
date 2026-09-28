from pathlib import Path
import requests,time,re
src=Path('work/the-tower-20260924/English.md').read_text(encoding='utf8')
langs={'Traditional-Chinese':('zh-TW','Traditional Chinese','tw'),'Portuguese':('pt-PT','Portuguese','pt'),'Spanish':('es-ES','Spanish','es'),'Thai':('th-TH','Thai','th'),'Indonesian':('id-ID','Indonesian','id'),'Vietnamese':('vi-VN','Vietnamese','vi')}
def trans(text,target):
 if not text.strip(): return text
 out=[]
 for i in range(0,len(text),450):
  chunk=text[i:i+450]
  try:
   j=requests.get('https://api.mymemory.translated.net/get',params={'q':chunk,'langpair':f'en|{target}'},timeout=12).json(); out.append(j.get('responseData',{}).get('translatedText') or chunk)
  except: out.append(chunk)
 return ''.join(out)
# translate each meaningful prose block independently; preserve markers
for name,(target,label,suffix) in langs.items():
 lines=src.splitlines(); out=[]; buf=[]
 def flush():
  nonlocal_dummy=None
 for line in lines:
  if line.strip() and not line.startswith(('<!--','!','## Image Plan','1. Source image','2. Source image','3. Source image','4. Source image','5. Source image','6. Source image','7. Source image','8. Source image','9. Source image','10. Source image','11. Source image','12. Source image','13. Source image','14. Source image','   - Source Image:','   - Purpose:')):
   # translate line directly (short)
   if line.startswith('- Slug:'): out.append(f'- Slug: the-tower-coins-gems-afk-guide-{suffix}')
   elif line.startswith('- Body Length Target:'): out.append('- Body Length Target: 500-600')
   elif line.startswith('- Output Language:'): out.append(f'- Output Language: {label}')
   elif line.startswith('   - Alt: '): out.append('   - Alt: '+trans(line[9:],target))
   elif line.startswith('- '):
    k,v=line.split(':',1); out.append(k+': '+trans(v.strip(),target))
   else: out.append(trans(line,target))
  else: out.append(line)
 text='\n'.join(out)+'\n'; text=re.sub(r'<!--.*?SOURCE_IMAGE\s*:?\s*(\d+).*?-->',lambda m:f'<!-- SOURCE_IMAGE:{m.group(1)} -->',text)
 Path(f'work/the-tower-20260924/{name}.md').write_text(text,encoding='utf8'); print(name)
