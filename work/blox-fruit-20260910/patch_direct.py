from pathlib import Path

ROOT = Path(__file__).parent / "packages"


def replace_body(name: str, text: str):
    p = ROOT / f"{name}.md"
    old = p.read_text(encoding="utf-8")
    a, b = old.index("## Article Body"), old.index("## Image Plan")
    p.write_text(old[:a] + "## Article Body\n\n" + text.strip() + "\n\n" + old[b:], encoding="utf-8")


def replace_once(name: str, old: str, new: str):
    p = ROOT / f"{name}.md"
    t = p.read_text(encoding="utf-8")
    if old in t:
        p.write_text(t.replace(old, new, 1), encoding="utf-8")


replace_once(
    "Indonesian",
    "Blox Fruits menuntut pemain mengalahkan musuh berulang kali demi pengalaman, uang, dan mastery, tetapi tidak menyediakan mode otomatis. Rutinitas hanya stabil jika target tidak menginterupsi karakter, buah menahan damage musuh tersebut, dan crosshair tetap di titik respawn. **Panduan AFK Blox Fruits** ini merangkum pengaturan sumber, uji Monkey level 14, serta keputusan progres dan perdagangan. Tujuannya adalah menguji loop sebelum memperpanjang sesi.",
    "Blox Fruits menuntut pemain mengalahkan musuh berulang kali demi pengalaman, uang, dan mastery, tetapi tidak menyediakan mode otomatis. Rutinitas hanya stabil jika target tidak menginterupsi karakter, buah menahan damage musuh tersebut, dan crosshair tetap di titik respawn. **Panduan AFK Blox Fruits** ini merangkum pengaturan sumber, uji Monkey level 14, serta keputusan progres dan perdagangan. Tujuannya adalah menguji loop sebelum memperpanjang sesi, sambil mencatat mastery, uang, posisi, dan koneksi agar hasil tiap target bisa dibandingkan.",
)

replace_once(
    "Traditional-Chinese",
    "Blox Fruits掛機攻略整理戰鬥設定、果實免傷條件、實測收益、屬性配點、島嶼解鎖與700級交易流程，並說明如何用UgPhone穩定執行長時間練級。",
    "Blox Fruits掛機攻略整理戰鬥設定、果實免傷條件、實測收益、屬性配點、島嶼解鎖與700級交易流程，並說明如何用UgPhone穩定執行長時間練級，讓搜尋者能快速掌握重點。",
)

replace_body("Traditional-Chinese", r'''
# Blox Fruits掛機攻略：穩定練級、配點與交易

Blox Fruits要反覆擊殺敵人，才能累積經驗、金錢與武器熟練度，但沒有內建自動模式。穩定掛機取決於敵人是否會擊退角色、果實能否免疫該目標，以及準星是否留在重生點。本篇 **Blox Fruits掛機攻略** 整理控制設定、14級Monkey收益、屬性養成與交易限制，先看完整循環，再決定是否延長。對想把練級交給雲端、避免手機長時間發熱的玩家，也能作為短測清單。

<!-- SOURCE_IMAGE:1 -->

## Blox Fruits是什麼？

這款Roblox動作RPG可用近戰、劍、槍和果實能力。果實每小時生成，20分鐘後消失；商人每4小時隨機補貨。

## 如何設定穩定掛機？

裝備要培養的武器，對準固定重生的敵人；若被推離位置，連點仍會落空。

<!-- SOURCE_IMAGE:2 -->

把 **Ability Control Scheme** 改成 **Modern**。

<!-- SOURCE_IMAGE:3 -->

關閉視角晃動，開啟快速模式並減少動效。

<!-- SOURCE_IMAGE:4 -->

在果實商店選擇標示免疫攻擊的果實，並用目前敵人實測免傷。

<!-- SOURCE_IMAGE:5 -->

吃下果實後確認能力生效。

<!-- SOURCE_IMAGE:6 -->

準星鎖定重生點，連點器放在技能鍵；觀察數輪，角度偏移就重設。

<!-- SOURCE_IMAGE:7 -->

## 收益與養成怎麼安排？

擊殺可得經驗與金錢，手上武器也會增加熟練度。

<!-- SOURCE_IMAGE:8 -->

原文用UgPhone刷14級Monkey，一小時約得 **20,082經驗與7,191金錢**，僅是樣本。

<!-- SOURCE_IMAGE:9 -->

按相同速率推算24小時為481,968經驗與172,584金錢；斷線、位移和漏招會降低結果。

<!-- SOURCE_IMAGE:10 -->

屬性點集中主要輸出與防禦，不要平均分給所有武器。

<!-- SOURCE_IMAGE:11 -->

金錢可向商人購買新裝備。

<!-- SOURCE_IMAGE:12 -->

升級會開放新島嶼；換區後重新測試免疫和站位。

<!-- SOURCE_IMAGE:13 -->

## Blox Fruits如何交易？

700級前丟出實體果實交換沒有保護，不要交出無法承受損失的物品。

<!-- SOURCE_IMAGE:14 -->

700級解鎖咖啡館後，雙方坐在白椅可正式交易。實體或永久果實、指定通行證和卷軸可交換；Beli、碎片、劍與槍不可交易。

<!-- SOURCE_IMAGE:15 -->

## 如何用UgPhone執行？

建立雲手機、安裝Roblox並套用設定。選定安全目標，短測傷害、重生、熟練度和連線。UgPhone可減少手機發熱與電量佔用，但不能修正錯誤站位，也不能繞過遊戲規則。

## 結語

先用單一敵人與技能測試，至少看完數次擊殺和重生；更換島嶼、果實、武器或目標後都要重測。每日收益只是樣本推算，遇到斷線或位移必須檢查。若要在不長時間佔用手機的情況下執行允許的練級流程，可 **下載UgPhone並申請免費試用**。確認傷害、熟練度與連線正常，再逐步延長時數，穩定後才適合長時間掛機。
''')

replace_body("Thai", r'''
# คู่มือ AFK Blox Fruits: เก็บเลเวล ค่าสถานะ และเทรด

Blox Fruits ต้องตีศัตรูซ้ำเพื่อรับ EXP เงิน และความชำนาญ แต่ไม่มีโหมดอัตโนมัติ วงจรจะนิ่งเมื่อศัตรูผลักไม่ได้ ผลไม้กันดาเมจ และเป้ายังตรงจุดเกิด **คู่มือ AFK Blox Fruits** นี้สรุปค่าตั้ง ผลทดสอบ Monkey เลเวล 14 และข้อจำกัดการเทรด ควรดูหลายรอบก่อนเพิ่มเวลา

<!-- SOURCE_IMAGE:1 -->

## Blox Fruits คืออะไร?

เกม Roblox ใช้หมัด ดาบ ปืน หรือผลไม้ ผลไม้เกิดทุกชั่วโมง หายใน 20 นาที ร้านสุ่มใหม่ทุก 4 ชั่วโมง

## ตั้งค่า AFK อย่างไร?

ใส่อาวุธ เล็งจุดเกิด และดูว่าศัตรูผลักตัวละครหรือไม่

<!-- SOURCE_IMAGE:2 -->

เปลี่ยน **Ability Control Scheme** เป็น **Modern**

<!-- SOURCE_IMAGE:3 -->

ปิดกล้องสั่น เปิดโหมดเร็ว และลดเอฟเฟกต์

<!-- SOURCE_IMAGE:4 -->

เลือกผลไม้ที่กันการโจมตี แล้วทดสอบกับศัตรูจริง

<!-- SOURCE_IMAGE:5 -->

กินผลไม้และยืนยันว่าพลังทำงาน

<!-- SOURCE_IMAGE:6 -->

เล็งจุดเกิด วางจุดแตะบนสกิล ดูหลายรอบ และจัดใหม่หากมุมเปลี่ยน

<!-- SOURCE_IMAGE:7 -->

## รายได้และการเติบโต

ชนะแล้วได้ EXP เงิน และความชำนาญของอาวุธ

<!-- SOURCE_IMAGE:8 -->

ทดสอบบน UgPhone กับ Monkey เลเวล 14 ได้ราว **20,082 EXP และ 7,191 เงินต่อชั่วโมง** ไม่ใช่อัตรารับประกัน

<!-- SOURCE_IMAGE:9 -->

คาด 24 ชั่วโมงได้ 481,968 EXP และ 172,584 เงิน แต่หลุดหรือโจมตีพลาดทำให้ลดลง

<!-- SOURCE_IMAGE:10 -->

ลงแต้มสายโจมตีหลักและป้องกัน ไม่กระจายทุกอาวุธ

<!-- SOURCE_IMAGE:11 -->

ใช้เงินซื้ออุปกรณ์จากพ่อค้า

<!-- SOURCE_IMAGE:12 -->

เลเวลสูงเปิดเกาะใหม่ จึงต้องทดสอบตำแหน่งอีกครั้ง

<!-- SOURCE_IMAGE:13 -->

## เทรดอย่างไร?

ก่อนเลเวล 700 การทิ้งผลไม้ให้กันไม่มีระบบคุ้มครอง

<!-- SOURCE_IMAGE:14 -->

เลเวล 700 เปิดคาเฟ่ ผลไม้จริง ผลไม้ถาวร เกมพาสบางชิ้น และสกรอลล์เทรดได้ แต่เงิน เศษ ดาบ และปืนไม่ได้

<!-- SOURCE_IMAGE:15 -->

## ใช้ UgPhone อย่างไร?

สร้างเครื่องคลาวด์ ติดตั้ง Roblox ใช้ค่าด้านบน แล้วทดสอบดาเมจ จุดเกิด ความชำนาญ และเน็ต UgPhone ลดความร้อนกับแบต แต่ไม่แก้จุดยืนผิดหรือข้ามกฎเกม

## สรุป

เริ่มจากศัตรูหนึ่งตัวและสกิลเดียว ดูหลายรอบก่อนปล่อยไว้ ทดสอบใหม่เมื่อเปลี่ยนเกาะ ผลไม้ อาวุธ หรือเป้าหมาย เพราะภูมิคุ้มกันและมุมอาจไม่ตรงเดิม รายได้รายวันเป็นค่าคาดการณ์ หากต้องการรันวิธีที่อนุญาตโดยไม่ใช้มือถือค้าง ให้ **ดาวน์โหลด UgPhone และทดลองใช้ฟรี** ตรวจว่า EXP กับความชำนาญยังเพิ่ม แล้วค่อยขยายเวลา
''')
