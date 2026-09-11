from pathlib import Path
ROOT=Path(__file__).parent/'packages'
def body(n,s):
 p=ROOT/f'{n}.md'; t=p.read_text(encoding='utf-8'); a,b=t.index('## Article Body'),t.index('## Image Plan'); p.write_text(t[:a]+'## Article Body\n\n'+s.strip()+'\n\n'+t[b:],encoding='utf-8')
def rep(n,o,x):
 p=ROOT/f'{n}.md'; t=p.read_text(encoding='utf-8'); p.write_text(t.replace(o,x,1),encoding='utf-8')
rep('Traditional-Chinese','Blox Fruits要反覆擊殺敵人累積經驗、金錢與熟練度，卻沒有內建自動模式。穩定掛機取決於敵人會否擊退角色、果實能否免疫目標，以及準星能否留在重生點。本篇 **Blox Fruits掛機攻略** 整理設定、14級Monkey收益、養成與交易，也適合想把練級放到雲端的玩家。先看完整循環，再決定是否延長。','Blox Fruits需反覆擊殺敵人累積經驗、金錢與熟練度，卻沒有內建自動模式。穩定掛機取決於敵人是否擊退、果實能否免疫目標，以及準星能否留在重生點。本篇 **Blox Fruits掛機攻略** 整理設定、14級Monkey收益、養成與交易，適合想把練級放到雲端的玩家。先看完整循環，再決定是否延長。遊戲資料、收益與操作限制都集中在下文，方便新手逐項確認。')
rep('Traditional-Chinese','Blox Fruits掛機攻略整理戰鬥設定、果實免傷、實測收益、配點、島嶼解鎖與700級交易，也說明如何用UgPhone穩定練級並減少手機負擔。','Blox Fruits掛機攻略整理戰鬥設定、果實免傷、實測收益、配點、島嶼解鎖、700級交易與UgPhone練級。')
rep('Indonesian','Perpanjang waktu hanya setelah tes singkat stabil dan mastery tetap bertambah.','Perpanjang waktu hanya setelah tes singkat stabil, mastery tetap bertambah, koneksi aman, dan posisi karakter tidak bergeser.')
rep('Indonesian','Mulailah dengan satu musuh dan satu skill, lalu amati beberapa respawn lengkap.','Mulailah dengan satu musuh dan satu skill, lalu amati beberapa respawn lengkap. Catat uang, pengalaman, dan mastery agar hasil target dapat dibandingkan.')
body('Thai',r'''
# คู่มือ AFK Blox Fruits: เก็บเลเวล ค่าสถานะ และเทรด

อยากฟาร์ม Blox Fruits ให้คุ้มต้องคุมจุดเกิด ศัตรู และผลไม้กันดาเมจ **คู่มือ AFK Blox Fruits** นี้สรุปค่าตั้ง ผลทดสอบ และการเทรด เริ่มจากการดูวงจบจริงก่อนปล่อยไว้

<!-- SOURCE_IMAGE:1 -->

## Blox Fruits คืออะไร?

เกม Roblox ใช้หมัด ดาบ ปืน และผลไม้ ผลไม้เกิดทุกชั่วโมง

<!-- SOURCE_IMAGE:2 -->

## ตั้งค่า AFK อย่างไร?

เล็งจุดเกิดและเช็กแรงผลัก

<!-- SOURCE_IMAGE:3 -->

ตั้ง **Ability Control Scheme** เป็น **Modern**

<!-- SOURCE_IMAGE:4 -->

ปิดกล้องสั่น ลดเอฟเฟกต์

<!-- SOURCE_IMAGE:5 -->

เลือกผลไม้กันการโจมตีแล้วลองจริง

<!-- SOURCE_IMAGE:6 -->

วางจุดแตะบนสกิลและดูหลายรอบ

<!-- SOURCE_IMAGE:7 -->

## รายได้และการเติบโต

Monkey เลเวล 14 บน UgPhone ได้ราว **20,082 EXP และ 7,191 เงินต่อชั่วโมง** เป็นตัวอย่างเท่านั้น

<!-- SOURCE_IMAGE:8 -->

<!-- SOURCE_IMAGE:9 -->

ลงแต้มสายหลักและป้องกัน ใช้เงินซื้ออุปกรณ์

<!-- SOURCE_IMAGE:10 -->

เลเวลสูงเปิดเกาะใหม่

<!-- SOURCE_IMAGE:11 -->

## เทรดอย่างไร?

ก่อนเลเวล 700 การทิ้งผลไม้ไม่มีระบบคุ้มครอง

<!-- SOURCE_IMAGE:12 -->

เมื่อถึง 700 คาเฟ่เปิดเทรด ผลไม้และไอเทมบางอย่างแลกได้

<!-- SOURCE_IMAGE:13 -->

<!-- SOURCE_IMAGE:14 -->

## ใช้ UgPhone อย่างไร?

สร้างเครื่องคลาวด์ ติดตั้ง Roblox ตั้งเป้า แล้วทดสอบดาเมจ จุดเกิด และเน็ต UgPhone ลดความร้อน แต่ไม่แก้ตำแหน่งผิด

<!-- SOURCE_IMAGE:15 -->

## สรุป

เริ่มจากศัตรูหนึ่งตัว ดูหลายรอบก่อนปล่อย ทดสอบใหม่เมื่อเปลี่ยนเกาะ ผลไม้ อาวุธ หรือเป้าหมาย รายได้เป็นค่าคาดการณ์ หากต้องการรันวิธีที่อนุญาตโดยไม่ใช้มือถือค้าง ให้ **ดาวน์โหลด UgPhone และทดลองใช้ฟรี** ตรวจว่า EXP กับความชำนาญยังเพิ่ม แล้วค่อยขยายเวลา
''')
