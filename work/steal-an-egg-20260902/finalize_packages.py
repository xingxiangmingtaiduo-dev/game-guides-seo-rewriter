from pathlib import Path
import re
root=Path(__file__).parent/'packages'
cfg={'English':('Steal an egg AFK Guide','English'),'Portuguese':('Guia AFK de Steal an egg','Portuguese'),'Spanish':('Guía AFK de Steal an egg','Spanish'),'Indonesian':('Panduan AFK Steal an egg','Indonesian'),'Vietnamese':('Hướng dẫn AFK Steal an egg','Vietnamese'),'Thai':('คู่มือ AFK Steal an egg','Thai'),'Traditional-Chinese':('Steal an egg掛機攻略','Traditional Chinese')}
for stem,(kw,ol) in cfg.items():
 p=root/(stem+'.md'); t=p.read_text(encoding='utf-8')
 t=re.sub(r'(?m)^- Primary Keyword:.*$',f'- Primary Keyword: {kw}',t)
 t=re.sub(r'(?m)^- Meta Description:.*$',f'- Meta Description: {kw} covers stealing eggs, safe escapes, zone speed checks, hatching pets, home upgrades, treadmill training, AFK timing, and practical UgPhone setup tips for longer sessions.',t)
 t=t.replace('## Introduction\n\n','')
 t=t.replace('   - Alt: Steal an egg gameplay image 1','   - Alt: Steal an egg AFK Guide gameplay overview')
 p.write_text(t,encoding='utf-8')
