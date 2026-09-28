from pathlib import Path
import requests,time,re,json
src=Path('work/the-tower-20260924/English.md').read_text(encoding='utf8')
langs={'Traditional-Chinese':('zh-TW','Traditional Chinese','tw'),'Portuguese':('pt-PT','Portuguese','pt'),'Spanish':('es-ES','Spanish','es'),'Thai':('th-TH','Thai','th'),'Indonesian':('id-ID','Indonesian','id'),'Vietnamese':('vi-VN','Vietnamese','vi')}
cache={}
def tr(text,target):
 key=(text,target)
 if key in cache:return cache[key]
 for attempt in range(3):
  try:
   r=requests.get('https://api.mymemory.translated.net/get',params={'q':text,'langpair':f'en|{target}'},timeout=30)
   j=r.json(); val=j.get('responseData',{}).get('translatedText')
   if val: cache[key]=val; time.sleep(.35); return val
  except Exception: time.sleep(2)
 return text
for name,(target,label,suffix) in langs.items():
 out=[]
 for line in src.splitlines():
  st=line.strip()
  if not st or st.startswith('<!--') or st.startswith('!') or re.match(r'^(\d+\. Source image|\s+- Source Image:|\s+- Purpose:)',line):
   out.append(line); continue
  if st.startswith('- Slug:'):
   out.append(f'- Slug: the-tower-coins-gems-afk-guide-{suffix}'); continue
  if st.startswith('- Body Length Target:'):
   out.append('- Body Length Target: 500-600'); continue
  if st.startswith('- Output Language:'):
   out.append(f'- Output Language: {label}'); continue
  # translate headings, metadata values, alt text, and body
  if line.startswith('   - Alt: '):
   out.append('   - Alt: '+tr(line[len('   - Alt: '):],target)); continue
  if line.startswith('- '):
   k,v=line.split(':',1); out.append(k+': '+tr(v.strip(),target)); continue
  out.append(tr(line,target))
 text='\n'.join(out)+'\n'
 # restore source markers if translation changed them
 text=re.sub(r'<!--.*?SOURCE_IMAGE\s*:?\s*(\d+).*?-->',lambda m:f'<!-- SOURCE_IMAGE:{m.group(1)} -->',text)
 Path(f'work/the-tower-20260924/{name}.md').write_text(text,encoding='utf8')
 print(name)
