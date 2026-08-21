from __future__ import annotations
import re
from pathlib import Path
SRC=Path(r"C:\Users\Og\Desktop\已SEO文章\Kick A Lucky Block七语言SEO");OUT=Path(r"C:\Users\Og\.codex\skills\game-guides-seo-rewriter\work\kick-lucky-block-multilingual\packages")
LANG={"Traditional-Chinese":"繁體中文","English":"English","Portuguese":"Português","Spanish":"Español","Thai":"ภาษาไทย","Indonesian":"Bahasa-Indonesia","Vietnamese":"Tiếng-Việt"};SUFFIX={"Traditional-Chinese":"tw","English":"en","Portuguese":"pt","Spanish":"es","Thai":"th","Indonesian":"id","Vietnamese":"vi"};K={"slug":"Slug","seo_title":"SEO Title","primary_keyword":"Primary Keyword","secondary_keywords":"Secondary Keywords","meta_description":"Meta Description","tags":"Tags","body_length_target":"Body Length Target","output_language":"Output Language"}
def p(t):
 m=re.match(r'^---\n(.*?)\n---\n\n(.*)$',t,re.S);d={}
 for x in m.group(1).splitlines():a,b=x.split(':',1);d[a]=b.strip().strip('"')
 return d,m.group(2)
def make(s,o):
 d,b=p((SRC/f'Kick A Lucky Block_SEO_{o}_500-600.md').read_text(encoding='utf-8'));a=[]
 d['slug']=re.sub(r'-(?:cn|tw|en|pt|es|th|id|vi)$','',d['slug'].lower())+'-'+SUFFIX[s]
 def r(m):a.append(m.group(1));return f'<!-- SOURCE_IMAGE:{len(a)} -->'
 b=re.sub(r'!\[(.*?)\]\(<[^>]*source-image-\d+\.[^>]+>\)',r,b);b=re.sub(r'^(##\s+(?:Introduction|Introdução|Introducción|前言|บทนำ|Pendahuluan|Giới thiệu)\s*\n\n)','',b,flags=re.M);assert len(a)==7
 meta='\n'.join(f'- {K[x]}: {d[x]}' for x in K);plan=[]
 for i,x in enumerate(a,1):plan += [f'{i}. Source image {i}',f'   - Alt: {x}','   - Purpose: Preserve the matching source visual in its original article context.',f'   - Source Image: {i}']
 (OUT/f'{s}.md').write_text(f"# {d['title']}\n\n## SEO Metadata\n\n{meta}\n\n## Article Body\n\n{b.strip()}\n\n## Image Plan\n\n"+'\n'.join(plan)+'\n',encoding='utf-8')
OUT.mkdir(parents=True,exist_ok=True)
for s,o in LANG.items():make(s,o)
