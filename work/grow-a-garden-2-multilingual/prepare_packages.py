from __future__ import annotations
import re
from pathlib import Path
SRC=Path(r"C:\Users\Og\Desktop\已SEO文章\Grow a Garden 2七语言SEO"); OUT=Path(r"C:\Users\Og\.codex\skills\game-guides-seo-rewriter\work\grow-a-garden-2-multilingual\packages")
LANG={"Traditional-Chinese":"繁體中文","English":"English","Portuguese":"Português","Spanish":"Español","Thai":"ภาษาไทย","Indonesian":"Bahasa-Indonesia","Vietnamese":"Tiếng-Việt"}; KEYS={"slug":"Slug","seo_title":"SEO Title","primary_keyword":"Primary Keyword","secondary_keywords":"Secondary Keywords","meta_description":"Meta Description","tags":"Tags","body_length_target":"Body Length Target","output_language":"Output Language"}
def parse(t):
 m=re.match(r"^---\n(.*?)\n---\n\n(.*)$",t,re.S); d={}
 for x in m.group(1).splitlines(): k,v=x.split(':',1);d[k]=v.strip().strip('"')
 return d,m.group(2)
def make(stem,old):
 d,b=parse((SRC/f"Grow a Garden 2_SEO_{old}_500-600.md").read_text(encoding='utf-8')); alts=[]
 def repl(m):alts.append(m.group(1));return f"<!-- SOURCE_IMAGE:{len(alts)} -->"
 b=re.sub(r"!\[(.*?)\]\(<[^>]*source-image-\d+\.[^>]+>\)",repl,b); b=re.sub(r"^(##\s+(?:Introduction|Introdução|Introducción|前言|บทนำ|Pendahuluan|Giới thiệu)\s*\n\n)",'',b,flags=re.M);assert len(alts)==10
 meta='\n'.join(f"- {KEYS[k]}: {d[k]}" for k in KEYS); plan=[]
 for i,a in enumerate(alts,1):plan += [f"{i}. Source image {i}",f"   - Alt: {a}","   - Purpose: Preserve the matching source visual in its original article context.",f"   - Source Image: {i}"]
 (OUT/f'{stem}.md').write_text(f"# {d['title']}\n\n## SEO Metadata\n\n{meta}\n\n## Article Body\n\n{b.strip()}\n\n## Image Plan\n\n"+'\n'.join(plan)+'\n',encoding='utf-8')
OUT.mkdir(parents=True,exist_ok=True)
for s,o in LANG.items():make(s,o)
