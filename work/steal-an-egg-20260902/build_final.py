from pathlib import Path
import subprocess
root=Path(r'C:\Users\Og\.codex\skills\game-guides-seo-rewriter'); out=Path(r'C:\Users\Og\Desktop\已SEO文章\Steal an egg七语言SEO'); out.mkdir(exist_ok=True)
src=Path(r'C:\Users\Og\Desktop\待SEO文章\Steal an egg测评.docx'); py=r'C:\Users\Og\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
for lang in ['Traditional-Chinese','English','Portuguese','Spanish','Thai','Indonesian','Vietnamese']:
 stem='Steal_an_egg_SEO_'+lang+'_500-600'; pkg=root/'work'/'steal-an-egg-20260902'/'packages'/(lang+'.md')
 subprocess.run([py,str(root/'scripts'/'build_docx.py'),'--article-package',str(pkg),'--source-docx',str(src),'--out',str(out/(stem+'.docx'))],check=True)
 subprocess.run([py,str(root/'scripts'/'build_markdown.py'),'--article-package',str(pkg),'--source-docx',str(src),'--out',str(out/(stem+'.md'))],check=True)
