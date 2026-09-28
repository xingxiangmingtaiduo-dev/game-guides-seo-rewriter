from pathlib import Path
from deep_translator import MyMemoryTranslator
import re,time
src=Path('work/the-tower-20260924/English.md').read_text(encoding='utf8')
langs={'Traditional-Chinese':('chinese traditional','Traditional Chinese','tw'),'Portuguese':('portuguese','Portuguese','pt'),'Spanish':('spanish','Spanish','es'),'Thai':('thai','Thai','th'),'Indonesian':('indonesian','Indonesian','id'),'Vietnamese':('vietnamese','Vietnamese','vi')}
# translate article lines only; preserve markers and image plan structure
for name,(target,label,suffix) in langs.items():
 tr=MyMemoryTranslator(source='english',target=target)
 out=[]
 for line in src.splitlines():
  if not line.strip() or line.startswith(('<!--','1. Source image','2. Source image','3. Source image','4. Source image','5. Source image','6. Source image','7. Source image','8. Source image','9. Source image','10. Source image','11. Source image','12. Source image','13. Source image','14. Source image','   - Source Image:','   - Purpose:')) or line.startswith('!'):
   out.append(line); continue
  if line.startswith('#') or line.startswith('- '):
   # translate visible value after key, except structural fields
   if line.startswith('- Slug:') or line.startswith('- Body Length Target:'):
    out.append(line); continue
   if line.startswith('- Output Language:'):
    out.append('- Output Language: '+label); continue
   if ':' not in line:
    try: out.append(tr.translate(line))
    except: out.append(line)
    time.sleep(.08)
    continue
   prefix,txt=line.split(':',1)
   try: out.append(prefix+': '+tr.translate(txt.strip()))
   except: out.append(line)
  elif line.startswith('   - Alt: '):
   try: out.append('   - Alt: '+tr.translate(line[9:]))
   except: out.append(line)
  else:
   try: out.append(tr.translate(line))
   except: out.append(line)
  time.sleep(.08)
 text='\n'.join(out)+'\n'
 text=re.sub(r'- Slug:.*',f'- Slug: the-tower-coins-gems-afk-guide-{suffix}',text,1)
 text=re.sub(r'- Body Length Target:.*','- Body Length Target: 500-600',text,1)
 # normalize markers if translated accidentally
 text=re.sub(r'<!--.*?SOURCE_IMAGE\s*:?\s*(\d+).*?-->',lambda m:f'<!-- SOURCE_IMAGE:{m.group(1)} -->',text)
 Path(f'work/the-tower-20260924/{name}.md').write_text(text,encoding='utf8')
 print(name)

