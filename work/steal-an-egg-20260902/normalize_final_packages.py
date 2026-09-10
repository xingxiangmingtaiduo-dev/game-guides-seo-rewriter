from pathlib import Path
import re

ROOT = Path(__file__).parent / "packages"

CONFIG = {
    "English": {
        "title": "Steal an egg AFK Guide: Eggs, Pets, and Speed",
        "primary": "Steal an egg AFK Guide",
        "secondary": "Steal an egg AFK, Roblox egg stealing, pet hatching, treadmill training",
        "description": "Steal an egg AFK Guide covering safe egg routes, pet income, home upgrades, treadmill training, and a practical UgPhone setup for longer sessions.",
        "tags": "Steal an egg, Roblox, AFK, Pets, UgPhone",
        "intro": "A rare egg has no value if its owner catches you before you reach the safe zone. In Steal an egg, speed determines which areas you can enter, how safely you can escape, and whether another player reaches an egg first. Back at your base, stolen eggs hatch into pets that generate money, including while you are offline. This **Steal an egg AFK Guide** connects those systems: choosing realistic routes, using the day-night reset, improving pets, and training speed without wasting time on an unreliable macro.",
        "conclusion": "Build speed before chasing distant egg pools, and use each zone marker as a checkpoint rather than a promise of success. Open finished eggs, equip the strongest pets, sell weak extras, and combine matching duplicates so the base keeps producing useful income. For AFK progress, test the treadmill for several minutes and confirm that the speed number is still rising. If you want to continue that permitted training without keeping your phone occupied and warm, **download UgPhone and start a free trial**, then extend the session only after the short test remains stable.",
        "alts": ["Steal an egg AFK Guide game overview", "NPC egg ready to steal", "Egg owner chasing the player", "Distant egg zones and reward pools", "Recommended speed sign at a zone", "Daytime egg run before the night reset", "Stolen egg incubating at the home base", "Best pets equipped for offline income", "Home upgrade increasing the pet limit", "Pet guide with collection rewards", "Selling an unwanted duplicate pet", "Combining three matching pets", "Character training speed on a treadmill", "Speed multiplier in the trail shop", "UgPhone cloud session running treadmill training"],
    },
    "Portuguese": {
        "title": "Guia AFK de Steal an egg: ovos, pets e velocidade",
        "primary": "Guia AFK de Steal an egg",
        "secondary": "Steal an egg AFK, roubar ovos no Roblox, chocar pets, treinar velocidade",
        "description": "Guia AFK de Steal an egg com rotas seguras, renda dos pets, melhorias da base, treino na esteira e configuração do UgPhone para sessões longas.",
        "tags": "Steal an egg, Roblox, AFK, Pets, UgPhone",
        "intro": "Um ovo raro não serve para nada se o dono alcançar você antes da zona segura. Em Steal an egg, a velocidade define quais áreas podem ser visitadas, a chance de escapar e quem chega primeiro ao ovo. De volta à base, os ovos roubados chocam pets que geram dinheiro, inclusive quando você está offline. Este **Guia AFK de Steal an egg** liga essas partes: escolher rotas realistas, aproveitar a troca entre dia e noite, melhorar os pets e treinar velocidade sem depender de um macro pouco confiável.",
        "conclusion": "Aumente a velocidade antes de disputar ovos em áreas distantes e use a placa de cada zona como referência, não como garantia. Abra os ovos prontos, equipe os pets mais fortes, venda duplicatas fracas e combine três pets iguais para melhorar a renda da base. No AFK, teste a esteira por alguns minutos e confirme que o atributo continua subindo. Para manter esse treino permitido sem ocupar nem aquecer o celular, **baixe o UgPhone e solicite um teste gratuito**; prolongue a sessão somente depois de verificar que ela permanece estável.",
        "alts": ["Guia AFK de Steal an egg na página do jogo", "Ovo de NPC disponível para roubo", "Dono do ovo perseguindo o jogador", "Zonas distantes com ovos melhores", "Placa de velocidade recomendada", "Corrida diurna antes da renovação noturna", "Ovo roubado incubando na base", "Melhores pets equipados para renda offline", "Melhoria da casa aumentando o limite de pets", "Guia de pets e recompensas de coleção", "Venda de um pet duplicado", "Fusão de três pets iguais", "Treino de velocidade na esteira", "Multiplicador de velocidade da loja de rastros", "Treino na esteira executado no UgPhone"],
    },
    "Spanish": {
        "title": "Guía AFK de Steal an egg: huevos, mascotas y velocidad",
        "primary": "Guía AFK de Steal an egg",
        "secondary": "Steal an egg AFK, robar huevos en Roblox, incubar mascotas, entrenar velocidad",
        "description": "Guía AFK de Steal an egg con rutas seguras, ingresos de mascotas, mejoras de la base, entrenamiento en cinta y configuración práctica de UgPhone.",
        "tags": "Steal an egg, Roblox, AFK, Mascotas, UgPhone",
        "intro": "Un huevo raro no sirve de mucho si su dueño te alcanza antes de volver a la zona segura. En Steal an egg, la velocidad decide qué áreas puedes visitar, si logras escapar y quién llega primero a cada huevo. Ya en la base, los huevos robados se incuban y producen mascotas que generan dinero incluso cuando estás desconectado. Esta **Guía AFK de Steal an egg** une esos sistemas: elegir rutas razonables, aprovechar el cambio entre día y noche, mejorar mascotas y entrenar velocidad sin depender de una macro poco fiable.",
        "conclusion": "Aumenta la velocidad antes de competir por huevos en zonas lejanas y toma el cartel de cada área como referencia, no como garantía. Abre los huevos terminados, equipa las mascotas más fuertes, vende duplicados débiles y combina tres iguales para mejorar los ingresos de la base. Para el AFK, prueba la cinta durante unos minutos y comprueba que la estadística sigue aumentando. Si quieres mantener ese entrenamiento permitido sin ocupar ni calentar el teléfono, **descarga UgPhone y solicita una prueba gratuita**; amplía la sesión únicamente cuando la prueba corta se mantenga estable.",
        "alts": ["Guía AFK de Steal an egg en la página del juego", "Huevo de NPC listo para robar", "Dueño del huevo persiguiendo al jugador", "Zonas lejanas con mejores huevos", "Cartel de velocidad recomendada", "Carrera diurna antes del reinicio nocturno", "Huevo robado incubándose en la base", "Mejores mascotas equipadas para ingresos sin conexión", "Mejora de la casa que amplía el límite de mascotas", "Guía de mascotas y premios de colección", "Venta de una mascota duplicada", "Fusión de tres mascotas iguales", "Entrenamiento de velocidad en la cinta", "Multiplicador de velocidad en la tienda de rastros", "Sesión de cinta ejecutándose en UgPhone"],
    },
    "Indonesian": {
        "title": "Panduan AFK Steal an egg: telur, pet, dan kecepatan",
        "primary": "Panduan AFK Steal an egg",
        "secondary": "Steal an egg AFK, mencuri telur Roblox, menetaskan pet, latihan kecepatan",
        "description": "Panduan AFK Steal an egg untuk rute aman, pendapatan pet, upgrade rumah, latihan treadmill, serta pengaturan UgPhone saat menjalankan sesi panjang.",
        "tags": "Steal an egg, Roblox, AFK, Pet, UgPhone",
        "intro": "Telur langka tidak berguna jika pemiliknya menangkapmu sebelum kembali ke zona aman. Di Steal an egg, kecepatan menentukan area yang dapat dimasuki, peluang lolos, dan siapa yang tiba lebih dahulu di depan telur. Setelah pulang, telur curian akan menetas menjadi pet yang menghasilkan uang, termasuk ketika akun sedang offline. **Panduan AFK Steal an egg** ini menghubungkan semua sistem tersebut: memilih rute yang masuk akal, memanfaatkan pergantian siang dan malam, memperkuat pet, serta melatih kecepatan tanpa bergantung pada makro yang mudah gagal.",
        "conclusion": "Tingkatkan kecepatan sebelum memburu telur di zona jauh, lalu gunakan papan rekomendasi sebagai patokan, bukan jaminan. Buka telur yang selesai menetas, pasang pet terkuat, jual duplikat lemah, dan gabungkan tiga pet yang sama agar pendapatan rumah terus membaik. Untuk AFK, uji treadmill selama beberapa menit dan pastikan angka kecepatan masih bertambah. Jika ingin meneruskan latihan yang diizinkan tanpa membuat ponsel terus terpakai dan panas, **unduh UgPhone lalu mulai uji coba gratis**; panjangkan sesi hanya setelah pengujian singkat berjalan stabil.",
        "alts": ["Panduan AFK Steal an egg di halaman game", "Telur NPC yang siap dicuri", "Pemilik telur mengejar pemain", "Zona jauh dengan kumpulan telur lebih baik", "Papan rekomendasi kecepatan zona", "Pencurian siang hari sebelum reset malam", "Telur curian menetas di rumah", "Pet terbaik untuk pendapatan offline", "Upgrade rumah menambah batas pet", "Panduan pet dan hadiah koleksi", "Menjual pet duplikat", "Menggabungkan tiga pet yang sama", "Latihan kecepatan di treadmill", "Pengganda kecepatan dari toko jejak", "Latihan treadmill berjalan di UgPhone"],
    },
}

def replace_latin(name, cfg):
    path = ROOT / f"{name}.md"
    text = path.read_text(encoding="utf-8")
    text = re.sub(r"(?m)^# .+$", f"# {cfg['title']}", text, count=1)
    text = re.sub(r"(?m)^- SEO Title:.*$", f"- SEO Title: {cfg['title']}", text)
    text = re.sub(r"(?m)^- Primary Keyword:.*$", f"- Primary Keyword: {cfg['primary']}", text)
    text = re.sub(r"(?m)^- Secondary Keywords:.*$", f"- Secondary Keywords: {cfg['secondary']}", text)
    text = re.sub(r"(?m)^- Meta Description:.*$", f"- Meta Description: {cfg['description']}", text)
    text = re.sub(r"(?m)^- Tags:.*$", f"- Tags: {cfg['tags']}", text)
    body_match = re.search(r"(?ms)(^## Article Body\s*\n)(.*?)(?=^## Image Plan\s*$)", text)
    body = body_match.group(2).strip()
    body = re.sub(r"(?ms)^# .*?\n\n.*?(?=^## )", f"# {cfg['title']}\n\n{cfg['intro']}\n\n", body, count=1)
    body = re.sub(r"(?ms)(^## (?:Conclusion|Conclusão|Conclusión|Kesimpulan)\s*\n\n).*?\Z", lambda m: m.group(1) + cfg['conclusion'], body)
    text = text[:body_match.start(2)] + body + "\n\n" + text[body_match.end(2):]
    for index, alt in enumerate(cfg["alts"], 1):
        pattern = rf"(?ms)({index}\. Source image {index}\s*\n\s*- Alt:) .*?(?=\n\s*- Purpose:)"
        text = re.sub(pattern, rf"\1 {alt}", text)
    path.write_text(text, encoding="utf-8")

for language, config in CONFIG.items():
    replace_latin(language, config)

# Keep Latin-language articles inside the requested band without cutting image context.
for language, cuts in {
    "English": [],
    "Portuguese": [
        ("O jogo é principalmente PVE: os ovos pertencem aos NPCs, mas os jogadores competem para alcançá-los primeiro. ", ""),
        ("Quanto mais longe for a zona, melhores tendem a ser os ovos e menor a margem para erro. ", ""),
        ("A abertura é manual, por isso volte quando o cronômetro terminar. ", ""),
        ("Eles continuam gerando dinheiro quando você está offline. ", ""),
    ],
    "Spanish": [
        ("El juego es principalmente PVE: los huevos pertenecen a los NPC, pero los jugadores compiten por llegar primero. ", ""),
        ("Cuanto más lejana sea la zona, mejores suelen ser los huevos y menor el margen de error. ", ""),
        ("La apertura es manual, así que vuelve cuando termine el temporizador. ", ""),
        ("Siguen generando dinero cuando estás desconectado. ", ""),
    ],
}.items():
    p=ROOT/f"{language}.md"; t=p.read_text(encoding="utf-8")
    for old,new in cuts: t=t.replace(old,new)
    if language=="English": t=t.replace("only after the short test remains stable.", "after the short test remains stable.")
    p.write_text(t,encoding="utf-8")

def package(title, slug, primary, secondary, description, tags, language, body, alts):
    metadata = "\n".join([
        f"- Slug: {slug}", f"- SEO Title: {title}", f"- Primary Keyword: {primary}",
        f"- Secondary Keywords: {secondary}", f"- Meta Description: {description}",
        f"- Tags: {tags}", "- Body Length Target: 500-600", f"- Output Language: {language}",
    ])
    plan=[]
    for i, alt in enumerate(alts, 1):
        plan.extend([f"{i}. Source image {i}", f"   - Alt: {alt}", "   - Purpose: Preserve the matching source visual in its original article context.", f"   - Source Image: {i}"])
    return f"# {title}\n\n## SEO Metadata\n\n{metadata}\n\n## Article Body\n\n{body.strip()}\n\n## Image Plan\n\n"+"\n".join(plan)+"\n"

zh_title="Steal an egg掛機攻略：偷蛋、孵蛋與速度養成"
zh_primary="Steal an egg掛機攻略"
zh_body=f'''# {zh_title}

《Steal an egg》的關鍵不是看到稀有蛋就衝，而是判斷能否安全帶回基地。蛋由NPC守護，拿走後會立刻遭到追擊；速度不足或鏡頭沒對準回程，都可能讓冒險白費。蛋帶回家園後會自行孵化，寵物則提供主要金錢收益。本篇 **{zh_primary}** 整理區域門檻、日夜刷新、寵物培養與跑步機AFK。先把偷蛋、孵蛋、產錢和練速串成循環，再決定何時前往更遠區域，能少做許多沒有回報的嘗試，也不必為公告中的高級蛋冒不必要的風險。

<!-- SOURCE_IMAGE:1 -->

## Steal an egg是什麼？

核心是PVE偷蛋，但玩家會爭搶同一批蛋。拿蛋後立刻轉身，先把鏡頭對準安全區；跑回去前被蛋主人追上，就算失敗。

<!-- SOURCE_IMAGE:2 -->

遠方區域的蛋池通常更好，追擊難度也更高。

<!-- SOURCE_IMAGE:3 -->

區域告示會提供建議速度，先達標再嘗試更穩妥。

<!-- SOURCE_IMAGE:4 -->

## 日夜刷新怎麼跑？

白天約五分鐘，可外出偷蛋；黑夜約十秒，用來等待刷新。神聖蛋會公告區域，但速度不足時，拿附近的安全蛋更有效率。

<!-- SOURCE_IMAGE:5 -->

## 孵蛋與寵物怎麼管理？

蛋放進家園後會倒數孵化，完成時要手動開蛋。

<!-- SOURCE_IMAGE:6 -->

一鍵裝備最佳寵物，可快速提高離線收入。

<!-- SOURCE_IMAGE:7 -->

升級家園能增加可放置的寵物數量。

<!-- SOURCE_IMAGE:8 -->

寵物指引列出各區收藏，完成可領金錢與速度。

<!-- SOURCE_IMAGE:9 -->

多餘寵物可出售換錢。

<!-- SOURCE_IMAGE:10 -->

三隻相同寵物可合成更高品階。

<!-- SOURCE_IMAGE:11 -->

## 跑步機AFK值得嗎？

跑步機持續增加速度，離開前先確認數值仍在上升。

<!-- SOURCE_IMAGE:12 -->

蹤跡商店的速度倍數可提高每次訓練收益。

<!-- SOURCE_IMAGE:13 -->

偷蛋不適合固定宏：蛋品質隨機、回程要調鏡頭並長按移動，黑夜也會中斷路線。

<!-- SOURCE_IMAGE:14 -->

## 如何用UgPhone訓練？

建立雲手機並安裝Roblox，把角色放上跑步機。短測速度與連線後再延長；UgPhone可減少手機發熱與佔用，但不保證稀有蛋。

<!-- SOURCE_IMAGE:15 -->

## 結語

先在跑步機累積速度，再依告示逐步向外推進；不要為公告蛋跳過無法承擔的路線。孵化完成後手動開蛋，最強寵物優先上場，多餘角色出售或合成。掛機前先做短測，確認速度持續增加；黑夜、斷線或角色離開跑步機後，都要重新檢查。短測的作用不是追求漂亮數字，而是避免整晚停在無效狀態。若想把允許的跑步機訓練放在雲端，避免長時間佔用手機，可立即下載UgPhone並申請免費試用，確認運行穩定後再延長時數。'''
zh_alts=["Steal an egg掛機攻略遊戲首頁","NPC旁可偷取的蛋","拿蛋後遭到主人追擊","遠方區域與更高品質蛋池","區域建議速度告示","白天偷蛋與黑夜刷新","家園內等待孵化的蛋","最佳寵物與離線收入","家園升級與寵物欄位","寵物指引與收藏獎勵","出售多餘寵物","三隻相同寵物合成","角色在跑步機訓練速度","蹤跡商店速度倍數","UgPhone雲端跑步機掛機"]
(ROOT/"Traditional-Chinese.md").write_text(package(zh_title,"steal-an-egg-afk-guide-tw",zh_primary,"Steal an egg AFK、Roblox偷蛋、寵物孵化、跑步機訓練","Steal an egg掛機攻略整理安全偷蛋路線、日夜刷新、寵物離線收益、家園升級與跑步機速度訓練，說明區域門檻、稀有蛋公告、寵物出售和合成方式，也提供使用UgPhone長時間掛機前的短測、連線與收益檢查流程。","Steal an egg、Roblox、掛機攻略、寵物、UgPhone","Traditional Chinese",zh_body,zh_alts),encoding="utf-8")

th_title="คู่มือ AFK Steal an egg: ไข่ สัตว์เลี้ยง และความเร็ว"
th_primary="คู่มือ AFK Steal an egg"
th_body=f'''# {th_title}

ไข่หายากไม่มีค่า ถ้าหนีกลับเขตปลอดภัยไม่ทัน หลังหยิบไข่จาก NPC เจ้าของจะไล่โจมตี ความเร็วจึงกำหนดพื้นที่และโอกาสรอด ไข่ที่นำกลับบ้านฟักเป็นสัตว์เลี้ยงสร้างเงินแม้ออฟไลน์ **{th_primary}** นี้สรุปเส้นทาง จังหวะกลางวันกลางคืน การพัฒนาสัตว์เลี้ยง และลู่วิ่ง เพื่อให้รู้ว่าควรเสี่ยงกับไข่ไกลเมื่อใด

<!-- SOURCE_IMAGE:1 -->

## Steal an egg คืออะไร?

เกมเน้น PVE แต่ผู้เล่นแย่งไข่ชุดเดียวกัน หยิบแล้วหันกล้องกลับฐานทันที

<!-- SOURCE_IMAGE:2 -->

ถ้าถูกเจ้าของตามทัน การขโมยจะล้มเหลว

<!-- SOURCE_IMAGE:3 -->

โซนไกลให้ไข่ดีกว่า แต่หนียากกว่า

<!-- SOURCE_IMAGE:4 -->

ดูป้ายความเร็วก่อนเข้าโซน

## วางแผนช่วงกลางวันอย่างไร?

กลางวันราวห้านาทีใช้ขโมยไข่ กลางคืนสิบวินาทีเป็นช่วงรีเซ็ต ไข่ระดับสูงควรไปเฉพาะโซนที่ความเร็วรับไหว

<!-- SOURCE_IMAGE:5 -->

## จัดการไข่และสัตว์เลี้ยงอย่างไร?

วางไข่ที่บ้าน รอครบเวลา แล้วเปิดด้วยตนเอง

<!-- SOURCE_IMAGE:6 -->

เลือกสัตว์เลี้ยงที่ดีที่สุดเพื่อรับเงินออฟไลน์

<!-- SOURCE_IMAGE:7 -->

อัปเกรดบ้านเพื่อเพิ่มจำนวนสัตว์เลี้ยง

<!-- SOURCE_IMAGE:8 -->

สะสมตามคู่มือเพื่อรับเงินและความเร็ว

<!-- SOURCE_IMAGE:9 -->

ขายตัวที่ไม่ใช้

<!-- SOURCE_IMAGE:10 -->

รวมตัวเหมือนกันสามตัวเพื่อเลื่อนระดับ

<!-- SOURCE_IMAGE:11 -->

## AFK บนลู่วิ่งคุ้มไหม?

ลู่วิ่งเพิ่มความเร็วต่อเนื่อง ตรวจสอบว่าค่ายังเพิ่มก่อนปล่อย AFK

<!-- SOURCE_IMAGE:12 -->

ตัวคูณจากร้านช่วยเพิ่มผลฝึก

<!-- SOURCE_IMAGE:13 -->

มาโครขโมยไข่ไม่เหมาะ เพราะต้องหมุนกล้อง กดวิ่งค้าง และหยุดตอนกลางคืน

<!-- SOURCE_IMAGE:14 -->

## ใช้ UgPhone อย่างไร?

สร้างเครื่องคลาวด์ ติดตั้ง Roblox แล้ววางตัวละครบนลู่วิ่ง ทดสอบก่อนเพิ่มเวลา UgPhone ลดความร้อนและการใช้โทรศัพท์ แต่ไม่รับประกันไข่หายาก

<!-- SOURCE_IMAGE:15 -->

## สรุป

เพิ่มความเร็วก่อนขยับไปโซนไกล เปิดไข่เมื่อฟักเสร็จ เลือกสัตว์เลี้ยงที่ทำเงินดีที่สุด และขายหรือรวมตัวซ้ำ ก่อน AFK ควรทดสอบว่าความเร็วยังเพิ่ม ตัวละครไม่หลุดจากลู่วิ่ง และการเชื่อมต่อไม่ขาด การตรวจสั้น ๆ ช่วยป้องกันการปล่อยเครื่องไว้นานโดยไม่ได้ผล หากต้องการฝึกโดยไม่เปิดโทรศัพท์ไว้นาน ให้ดาวน์โหลด UgPhone และเริ่มทดลองใช้ฟรี จากนั้นค่อยขยายเวลาเมื่อระบบทำงานเสถียร'''
th_alts=["คู่มือ AFK Steal an egg บนหน้าเกม","ไข่ของ NPC ที่ขโมยได้","เจ้าของไข่กำลังไล่ผู้เล่น","โซนไกลและกลุ่มไข่ที่ดีกว่า","ป้ายแนะนำความเร็วประจำโซน","การขโมยไข่ช่วงกลางวัน","ไข่กำลังฟักภายในบ้าน","สัตว์เลี้ยงที่ดีที่สุดสำหรับรายได้ออฟไลน์","การอัปเกรดบ้านเพื่อเพิ่มช่องสัตว์เลี้ยง","คู่มือสัตว์เลี้ยงและรางวัลสะสม","การขายสัตว์เลี้ยงที่ไม่ใช้","การรวมสัตว์เลี้ยงเหมือนกันสามตัว","ตัวละครฝึกความเร็วบนลู่วิ่ง","ตัวคูณความเร็วในร้านค้า","การฝึกลู่วิ่งผ่าน UgPhone"]
(ROOT/"Thai.md").write_text(package(th_title,"steal-an-egg-afk-guide-th",th_primary,"Steal an egg AFK, ขโมยไข่ Roblox, ฟักสัตว์เลี้ยง, ฝึกความเร็ว","คู่มือ AFK Steal an egg อธิบายเส้นทางขโมยไข่ การหนีกลับฐาน วงจรกลางวันกลางคืน การฟักสัตว์เลี้ยง การฝึกบนลู่วิ่ง และการตั้งค่า UgPhone สำหรับเล่นระยะยาว","Steal an egg, Roblox, AFK, สัตว์เลี้ยง, UgPhone","Thai",th_body,th_alts),encoding="utf-8")
