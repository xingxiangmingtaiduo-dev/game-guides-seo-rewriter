from pathlib import Path
from deep_translator import GoogleTranslator
import re,time
src=Path('work/the-tower-20260924/English.md').read_text(encoding='utf8')
langs={'Traditional-Chinese':('zh-TW','Traditional Chinese','tw'),'Portuguese':('pt','Portuguese','pt'),'Spanish':('es','Spanish','es'),'Thai':('th','Thai','th'),'Indonesian':('id','Indonesian','id'),'Vietnamese':('vi','Vietnamese','vi')}
# translate prose lines while preserving markdown, markers, metadata keys, image plan numbering
skip_prefix=('- Slug:','- SEO Title:','- Primary Keyword:','- Secondary Keywords:','- Meta Description:','- Tags:','- Body Length Target:','- Output Language:','# ','## ','<!--','1. Source image','2. Source image','3. Source image','4. Source image','5. Source image','6. Source image','7. Source image','8. Source image','9. Source image','10. Source image','11. Source image','12. Source image','13. Source image','14. Source image','   - Source Image:')
for name,(code,label,suffix) in langs.items():
    tr=GoogleTranslator(source='en',target=code)
    out=[]
    for line in src.splitlines():
        if not line.strip() or line.startswith(skip_prefix) or line.startswith('   - Purpose:'):
            out.append(line); continue
        if line.startswith('   - Alt: '):
            text=line[len('   - Alt: '):]
            out.append('   - Alt: '+tr.translate(text)); continue
        # preserve metadata values selectively by translating entire value
        if line.startswith('- '):
            k,v=line.split(':',1); out.append(k+': '+tr.translate(v.strip())); continue
        if line.startswith('!') or line.startswith('['): out.append(line); continue
        try: out.append(tr.translate(line))
        except Exception: out.append(line)
        time.sleep(0.03)
    text='\n'.join(out)+'\n'
    # Correct metadata structural values
    text=re.sub(r'- Slug:.*',f'- Slug: the-tower-coins-gems-afk-guide-{suffix}',text,1)
    text=re.sub(r'- Body Length Target:.*','- Body Length Target: 500-600',text,1)
    text=re.sub(r'- Output Language:.*',f'- Output Language: {label}',text,1)
    # Keep image markers and plan source fields; translator may alter marker lines? restore
    text=re.sub(r'<!--.*?SOURCE_IMAGE\s*:?\s*(\d+).*?-->',lambda m:f'<!-- SOURCE_IMAGE:{m.group(1)} -->',text)
    # headings are translated but ensure H1 contains translated primary keyword is hard; use translated title line as primary
    lines=text.splitlines();
    # set primary keyword from H1 line, and make H1/SEO title same translated title
    h1=next((x[2:] for x in lines if x.startswith('# ') and not x.startswith('## ')),None)
    if h1:
      text=re.sub(r'- Primary Keyword:.*', '- Primary Keyword: '+h1.split(':')[0].strip(), text,1)
      text=re.sub(r'- SEO Title:.*','- SEO Title: '+h1,text,1)
    Path(f'work/the-tower-20260924/{name}.md').write_text(text,encoding='utf8')
    print(name)
