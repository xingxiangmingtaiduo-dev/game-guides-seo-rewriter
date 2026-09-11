from pathlib import Path

ROOT = Path(__file__).parent / "packages"


def body(name, value):
    p = ROOT / f"{name}.md"
    t = p.read_text(encoding="utf-8")
    a, b = t.index("## Article Body"), t.index("## Image Plan")
    p.write_text(t[:a] + "## Article Body\n\n" + value.strip() + "\n\n" + t[b:], encoding="utf-8")


def repl(name, old, new):
    p = ROOT / f"{name}.md"
    t = p.read_text(encoding="utf-8")
    if old in t:
        p.write_text(t.replace(old, new, 1), encoding="utf-8")


repl("Indonesian", "Perpanjang waktu hanya setelah tes singkat stabil dan mastery tetap bertambah.", "Perpanjang waktu hanya setelah tes singkat stabil, mastery tetap bertambah, dan koneksi tidak terputus.")
repl("Traditional-Chinese", "Blox Fruits要反覆擊殺敵人累積經驗、金錢與熟練度，卻沒有內建自動模式。穩定掛機取決於敵人會否擊退角色、果實能否免疫目標，以及準星能否留在重生點。本篇 **Blox Fruits掛機攻略** 整理設定、14級Monkey收益、養成與交易，也適合想把練級放到雲端的玩家。先看完整循環，再決定是否延長。對想把練級交給雲端、避免手機長時間發熱的玩家，也能作為短測清單。", "Blox Fruits要反覆擊殺敵人累積經驗、金錢與熟練度，卻沒有內建自動模式。穩定掛機取決於敵人會否擊退角色、果實能否免疫目標，以及準星能否留在重生點。本篇 **Blox Fruits掛機攻略** 整理設定、14級Monkey收益、養成與交易，也適合想把練級放到雲端的玩家。先看完整循環，再決定是否延長。")
repl("Traditional-Chinese", "Blox Fruits掛機攻略整理戰鬥設定、果實免傷、實測收益、配點、島嶼解鎖與700級交易，也說明如何用UgPhone練級。", "Blox Fruits掛機攻略整理戰鬥設定、果實免傷、實測收益、配點、島嶼解鎖與700級交易，也說明如何用UgPhone穩定練級並減少手機負擔。")

body("Thai", r'''
# คู่มือ AFK Blox Fruits: เก็บเลเวล ค่าสถานะ และเทรด

อยากฟาร์ม Blox Fruits ให้คุ้มต้องคุมจุดเกิด ศัตรู และผลไม้กันดาเมจ **คู่มือ AFK Blox Fruits** นี้สรุปค่าตั้งและผลทดสอบ Monkey เลเวล 14 ก่อนปล่อย AFK ควรดูวงจบจริง

<!-- SOURCE_IMAGE:1 -->

## Blox Fruits คืออะไร?

เกม Roblox ใช้หมัด ดาบ ปืน และผลไม้ ผลไม้เกิดทุกชั่วโมง หายใน 20 นาที ร้านสุ่มทุก 4 ชั่วโมง

## ตั้งค่า AFK อย่างไร?

เล็งจุดเกิดและเช็กว่าศัตรูผลักหรือไม่

<!-- SOURCE_IMAGE:2 -->

ตั้ง **Ability Control Scheme** เป็น **Modern**

<!-- SOURCE_IMAGE:3 -->

ปิดกล้องสั่น เปิดโหมดเร็ว ลดเอฟเฟกต์

<!-- SOURCE_IMAGE:4 -->

เลือกผลไม้ที่กันการโจมตีของเป้าหมาย แล้วทดสอบจริง

<!-- SOURCE_IMAGE:5 -->

กินผลไม้และเช็กพลัง

<!-- SOURCE_IMAGE:6 -->

วางเป้าที่จุดเกิด ตั้งจุดแตะบนสกิล และดูหลายรอบ

<!-- SOURCE_IMAGE:7 -->

## รายได้และการเติบโต

ชนะได้ EXP เงิน และความชำนาญอาวุธ

<!-- SOURCE_IMAGE:8 -->

ทดสอบ UgPhone กับ Monkey เลเวล 14 ได้ **20,082 EXP และ 7,191 เงินต่อชั่วโมง** เป็นเพียงตัวอย่าง

<!-- SOURCE_IMAGE:9 -->

คาด 24 ชั่วโมงคือ 481,968 EXP และ 172,584 เงิน แต่อาจลดเมื่อหลุดหรือพลาด

<!-- SOURCE_IMAGE:10 -->

ลงแต้มสายหลักกับป้องกัน

<!-- SOURCE_IMAGE:11 -->

ใช้เงินซื้ออุปกรณ์

<!-- SOURCE_IMAGE:12 -->

เลเวลสูงเปิดเกาะใหม่ ต้องทดสอบอีกครั้ง

<!-- SOURCE_IMAGE:13 -->

## เทรดอย่างไร?

ก่อนเลเวล 700 การทิ้งผลไม้ไม่มีระบบคุ้มครอง

<!-- SOURCE_IMAGE:14 -->

เลเวล 700 เปิดคาเฟ่เทรด ผลไม้และไอเทมบางอย่างแลกได้ แต่เงิน ดาบ และปืนแลกไม่ได้

<!-- SOURCE_IMAGE:15 -->

## ใช้ UgPhone อย่างไร?

สร้างเครื่องคลาวด์ ติดตั้ง Roblox ตั้งเป้า แล้วทดสอบดาเมจ จุดเกิด ความชำนาญ และเน็ต UgPhone ลดความร้อน แต่ไม่แก้ตำแหน่งผิด

## สรุป

เริ่มจากศัตรูและสกิลเดียว ดูหลายรอบก่อนปล่อย ทดสอบใหม่เมื่อเปลี่ยนเกาะ ผลไม้ อาวุธ หรือเป้าหมาย รายได้เป็นค่าคาดการณ์ หากต้องการรันวิธีที่อนุญาตโดยไม่ใช้มือถือค้าง ให้ **ดาวน์โหลด UgPhone และทดลองใช้ฟรี** ตรวจว่า EXP กับความชำนาญยังเพิ่ม แล้วค่อยขยายเวลา
''')
