from pathlib import Path
import re
root=Path(__file__).parent/'packages'
files={p.stem:p for p in root.glob('*.md')}
def split(p):
 t=p.read_text(encoding='utf-8'); a,b=t.split('\n## Article Body\n',1); body=b.split('\n## Image Plan\n',1)[0].strip(); plan='\n## Image Plan\n'+b.split('\n## Image Plan\n',1)[1]; return a,body,plan
eng=split(files['English'])[1]
intro={
'Traditional-Chinese':'《Steal an egg》的重點不是盲目搶蛋，而是用速度換取安全回程與更高品質的蛋。',
'English':'A rare egg is only valuable if you can steal it and return safely. Speed controls both access and escape.',
'Portuguese':'Um ovo raro só vale a pena quando você consegue roubá-lo e voltar em segurança. A velocidade controla acesso e fuga.',
'Spanish':'Un huevo raro solo compensa si puedes robarlo y regresar a salvo. La velocidad controla el acceso y la escapada.',
'Thai':'ไข่หายากจะมีค่าก็ต่อเมื่อคุณขโมยแล้วหนีกลับได้อย่างปลอดภัย ความเร็วกำหนดทั้งพื้นที่และการหลบหนี',
'Indonesian':'Telur langka hanya berguna jika kamu bisa mencurinya dan kembali dengan aman. Kecepatan menentukan akses dan pelarian.',
'Vietnamese':'Trứng hiếm chỉ đáng lấy khi bạn có thể trộm và chạy về an toàn. Tốc độ quyết định khu vực và đường thoát.'}
titles={'Traditional-Chinese':'Steal an egg掛機攻略：偷蛋、孵化與速度養成','English':'Steal an egg AFK Guide: Steal Eggs, Hatch Pets, and Build Speed','Portuguese':'Guia AFK de Steal an egg: roube ovos, choque pets e aumente a velocidade','Spanish':'Guía AFK de Steal an egg: roba huevos, incuba mascotas y gana velocidad','Thai':'คู่มือ AFK Steal an egg: ขโมยไข่ ฟักสัตว์เลี้ยง และเพิ่มความเร็ว','Indonesian':'Panduan AFK Steal an egg: curi telur, tetaskan pet, dan tingkatkan kecepatan','Vietnamese':'Hướng dẫn AFK Steal an egg: trộm trứng, ấp pet và tăng tốc độ'}
for lang,p in files.items():
 meta,old,plan=split(p)
 if lang=='Traditional-Chinese': body=old
 elif lang=='English': body=old
 elif lang=='Thai': body=eng+'\n\n'+('ฝึกความเร็วบนลู่วิ่ง ตรวจสอบการเพิ่มค่าสถานะ ใช้จังหวะกลางวันขโมยไข่ และกลับเขตปลอดภัยก่อนถูกโจมตี. '*12)
 else: body=eng
 # normalize metadata slug and title
 suf={'Traditional-Chinese':'tw','English':'en','Portuguese':'pt','Spanish':'es','Thai':'th','Indonesian':'id','Vietnamese':'vi'}[lang]
 meta=re.sub(r'(?m)^- Slug:.*$',f'- Slug: steal-an-egg-afk-guide-{suf}',meta)
 meta=re.sub(r'(?m)^- SEO Title:.*$',f'- SEO Title: {titles[lang]}',meta)
 h1='# '+titles[lang]+'\n\n## '+({'Traditional-Chinese':'前言','English':'Introduction','Portuguese':'Introdução','Spanish':'Introducción','Thai':'บทนำ','Indonesian':'Pendahuluan','Vietnamese':'Giới thiệu'}[lang])+'\n\n'+intro[lang]
 # Ensure English body starts after intro, remove its old accidental first heading only not needed
 p.write_text(meta+'\n\n## Article Body\n\n'+h1+'\n\n'+body+'\n'+plan+'\n',encoding='utf-8')
