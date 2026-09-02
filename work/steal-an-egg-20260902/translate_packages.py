from pathlib import Path
import re, urllib.parse, urllib.request, json, time
root=Path(__file__).parent/'packages'; src=(root/'English.md').read_text(encoding='utf-8')
langs={'Portuguese':('pt','Guia AFK de Steal an egg'),'Spanish':('es','Guía AFK de Steal an egg'),'Thai':('th','คู่มือ AFK Steal an egg'),'Indonesian':('id','Panduan AFK Steal an egg'),'Vietnamese':('vi','Hướng dẫn AFK Steal an egg'),'Traditional-Chinese':('zh-TW','Steal an egg掛機攻略')}
def tr(s,code):
 if not s.strip(): return s
 url='https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl='+code+'&dt=t&q='+urllib.parse.quote(s)
 try:
  data=json.loads(urllib.request.urlopen(url,timeout=20).read().decode('utf-8')); return ''.join(x[0] for x in data[0] if x and x[0])
 except Exception: return s
head=re.search(r'(?ms)^## Article Body\n\n(.*?)\n## Image Plan\n',src).group(1)
for lang,(code,kw) in langs.items():
 p=root/(lang+'.md'); t=p.read_text(encoding='utf-8'); pre=t.split('\n## Article Body\n',1)[0]; plan='\n## Image Plan\n'+t.split('\n## Image Plan\n',1)[1]
 lines=[]
 for line in head.splitlines():
  st=line.strip()
  if not st or st.startswith('<!-- SOURCE_IMAGE:'):
   lines.append(line); continue
  if st.startswith('#'):
   lines.append(tr(line,code)); continue
  lines.append(tr(line,code)); time.sleep(.08)
 body='\n'.join(lines)
 # Keep exact localized keyword in H1 and restore a natural localized title line.
 body=re.sub(r'^# .*$', '# '+kw, body, count=1, flags=re.M)
 labels={'Portuguese':'Introdução','Spanish':'Introducción','Thai':'บทนำ','Indonesian':'Pendahuluan','Vietnamese':'Giới thiệu','Traditional-Chinese':'前言'}
 conclusion={'Portuguese':'Conclusão','Spanish':'Conclusión','Thai':'สรุป','Indonesian':'Kesimpulan','Vietnamese':'Kết luận','Traditional-Chinese':'結語'}
 body=re.sub(r'^## (Introduction|Introducción|Introdução|บทนำ|Pendahuluan|Giới thiệu|前言)$','## '+labels[lang],body,flags=re.M)
 body=re.sub(r'^## (Conclusion|Conclusión|Conclusão|สรุป|Kesimpulan|Kết luận|結語)$','## '+conclusion[lang],body,flags=re.M)
 p.write_text(pre+'\n## Article Body\n\n'+body+plan,encoding='utf-8')
