from pathlib import Path
from deep_translator import GoogleTranslator
import re
src=Path('work/the-tower-20260924/English.md').read_text(encoding='utf8')
langs={'Traditional-Chinese':('zh-TW','Traditional Chinese','tw'),'Portuguese':('pt','Portuguese','pt'),'Spanish':('es','Spanish','es'),'Thai':('th','Thai','th'),'Indonesian':('id','Indonesian','id'),'Vietnamese':('vi','Vietnamese','vi')}
# split into translatable chunks, one batch per language
lines=src.splitlines(); chunks=[]; idx=[]
for i,line in enumerate(lines):
 if line.strip() and not line.startswith(('#','- ','<!--','1. Source image','2. Source image','3. Source image','4. Source image','5. Source image','6. Source image','7. Source image','8. Source image','9. Source image','10. Source image','11. Source image','12. Source image','13. Source image','14. Source image','   - Source Image:','   - Purpose:')) and not line.startswith('!'):
  chunks.append(line); idx.append(i)
for name,(code,label,suffix) in langs.items():
 tr=GoogleTranslator(source='en',target=code)
 try: trans=tr.translate_batch(chunks)
 except Exception as e:
  print(name,'ERR',e); continue
 out=lines[:]
 for i,t in zip(idx,trans): out[i]=t or out[i]
 text='\n'.join(out)+'\n'
 text=re.sub(r'- Slug:.*',f'- Slug: the-tower-coins-gems-afk-guide-{suffix}',text,1)
 text=re.sub(r'- Body Length Target:.*','- Body Length Target: 500-600',text,1)
 text=re.sub(r'- Output Language:.*',f'- Output Language: {label}',text,1)
 # translate metadata values separately with batch
 meta=['The Tower AFK Guide','The Tower coins, The Tower gems, The Tower research, The Tower UgPhone AFK','Learn how to earn and spend coins and gems in The Tower, then set up UgPhone for longer AFK sessions and steady research progress.','The Tower, Roblox, AFK Guide, Coins, Gems, UgPhone']
 try:
  mt=tr.translate_batch(meta)
  text=re.sub(r'- Primary Keyword:.*','- Primary Keyword: '+mt[0],text,1)
  text=re.sub(r'- Secondary Keywords:.*','- Secondary Keywords: '+mt[1],text,1)
  text=re.sub(r'- Meta Description:.*','- Meta Description: '+mt[2],text,1)
  text=re.sub(r'- Tags:.*','- Tags: '+mt[3],text,1)
 except Exception as e: print('meta err',e)
 # Set h1/seo exact
 h1=next((x[2:] for x in text.splitlines() if x.startswith('# ') and not x.startswith('## ')),None)
 if h1:
  text=re.sub(r'- SEO Title:.*','- SEO Title: '+h1,text,1)
  text=re.sub(r'- Primary Keyword:.*','- Primary Keyword: '+h1.split(':')[0].strip(),text,1)
 Path(f'work/the-tower-20260924/{name}.md').write_text(text,encoding='utf8')
 print(name)
