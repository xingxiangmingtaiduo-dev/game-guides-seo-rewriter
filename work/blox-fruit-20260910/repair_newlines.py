from pathlib import Path
p=Path(__file__).parent/'packages'/'Thai.md'; t=p.read_text(encoding='utf8'); t=t.replace('`n','\n'); p.write_text(t,encoding='utf8')
