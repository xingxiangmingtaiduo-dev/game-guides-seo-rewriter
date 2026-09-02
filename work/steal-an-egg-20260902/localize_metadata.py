from pathlib import Path
import re, urllib.parse, urllib.request, json
root=Path(__file__).parent/'packages'
codes={'Traditional-Chinese':'zh-TW','English':'en','Portuguese':'pt','Spanish':'es','Thai':'th','Indonesian':'id','Vietnamese':'vi'}
skip={'Slug','Body Length Target','Output Language','Tags'}
def tr(s,code):
 u='https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl='+code+'&dt=t&q='+urllib.parse.quote(s)
 try:
  d=json.loads(urllib.request.urlopen(u,timeout=20).read().decode()); return ''.join(x[0] for x in d[0] if x and x[0])
 except Exception:return s
for lang,code in codes.items():
 p=root/(lang+'.md'); lines=p.read_text(encoding='utf-8').splitlines(); out=[]
 for line in lines:
  m=re.match(r'^- (SEO Title|Primary Keyword|Secondary Keywords|Meta Description):\s*(.*)$',line)
  if m and lang!='English': line='- '+m.group(1)+': '+tr(m.group(2),code)
  out.append(line)
 # Correct output-language metadata values and localized tag list.
 for i,line in enumerate(out):
  if line.startswith('- Tags:') and lang!='English': out[i]='- Tags: Steal an egg, Roblox, AFK, '+tr('Pets, UgPhone',code)
 p.write_text('\n'.join(out)+'\n',encoding='utf-8')
