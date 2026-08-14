from __future__ import annotations
import re
from pathlib import Path

SOURCE_DIR = Path(r"C:\Users\Og\Desktop\已SEO文章\Broken Blade七语言SEO")
OUTPUT_DIR = Path(r"C:\Users\Og\.codex\skills\game-guides-seo-rewriter\work\broken-blade-multilingual\packages")
LANGUAGES = {"Traditional-Chinese":"繁體中文","English":"English","Portuguese":"Português","Spanish":"Español","Thai":"ภาษาไทย","Indonesian":"Bahasa-Indonesia","Vietnamese":"Tiếng-Việt"}
KEY_MAP={"slug":"Slug","seo_title":"SEO Title","primary_keyword":"Primary Keyword","secondary_keywords":"Secondary Keywords","meta_description":"Meta Description","tags":"Tags","body_length_target":"Body Length Target","output_language":"Output Language"}
def parse(text):
 m=re.match(r"^---\n(.*?)\n---\n\n(.*)$",text,re.S); values={}
 for line in m.group(1).splitlines():
  k,v=line.split(":",1); values[k]=v.strip().strip('"')
 return values,m.group(2)
def build(stem,old):
 values,body=parse((SOURCE_DIR/f"Broken Blade_SEO_{old}_500-600.md").read_text(encoding="utf-8")); alts=[]
 def image(m): alts.append(m.group(1)); return f"<!-- SOURCE_IMAGE:{len(alts)} -->"
 body=re.sub(r"!\[(.*?)\]\(<[^>]*source-image-\d+\.[^>]+>\)",image,body)
 body=re.sub(r"^(##\s+(?:Introduction|Introdução|Introducción|前言|บทนำ|Pendahuluan|Giới thiệu)\s*\n\n)","",body,flags=re.M)
 assert len(alts)==6,(stem,len(alts))
 metadata="\n".join(f"- {KEY_MAP[k]}: {values[k]}" for k in KEY_MAP)
 plan=[]
 for i,alt in enumerate(alts,1): plan += [f"{i}. Source image {i}",f"   - Alt: {alt}","   - Purpose: Preserve the matching source visual in its original article context.",f"   - Source Image: {i}"]
 (OUTPUT_DIR/f"{stem}.md").write_text(f"# {values['title']}\n\n## SEO Metadata\n\n{metadata}\n\n## Article Body\n\n{body.strip()}\n\n## Image Plan\n\n"+"\n".join(plan)+"\n",encoding="utf-8")
OUTPUT_DIR.mkdir(parents=True,exist_ok=True)
for stem,old in LANGUAGES.items(): build(stem,old)
