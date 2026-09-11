from pathlib import Path
R=Path(__file__).parent/'packages'
def b(n,s):
 p=R/f'{n}.md';t=p.read_text(encoding='utf8');a,c=t.index('## Article Body'),t.index('## Image Plan');p.write_text(t[:a]+'## Article Body\n\n'+s.strip()+'\n\n'+t[c:],encoding='utf8')
b('Thai',r'''# คู่มือ AFK Blox Fruits: เก็บเลเวล ค่าสถานะ และเทรด

อยากฟาร์มให้คุ้มต้องคุมจุดเกิด ผลไม้ และตำแหน่ง **คู่มือ AFK Blox Fruits** นี้สรุปค่าตั้ง รายได้ และเทรด

<!-- SOURCE_IMAGE:1 -->
## Blox Fruits คืออะไร?
เกม Roblox ใช้หมัด ดาบ ปืน และผลไม้ ผลไม้เกิดทุกชั่วโมง
<!-- SOURCE_IMAGE:2 -->
## ตั้งค่า AFK อย่างไร?
ตั้ง **Ability Control Scheme** เป็น **Modern**
<!-- SOURCE_IMAGE:3 -->
ปิดกล้องสั่น ลดเอฟเฟกต์
<!-- SOURCE_IMAGE:4 -->
เลือกผลไม้กันการโจมตีและทดสอบจริง
<!-- SOURCE_IMAGE:5 -->
กินผลไม้แล้วเช็กพลัง
<!-- SOURCE_IMAGE:6 -->
เล็งจุดเกิด วางจุดแตะบนสกิล ดูหลายรอบ
<!-- SOURCE_IMAGE:7 -->
## รายได้และการเติบโต
Monkey เลเวล 14 บน UgPhone ได้ราว **20,082 EXP และ 7,191 เงินต่อชั่วโมง** เป็นตัวอย่าง
<!-- SOURCE_IMAGE:8 -->
<!-- SOURCE_IMAGE:9 -->
ลงแต้มสายหลัก ใช้เงินซื้ออุปกรณ์
<!-- SOURCE_IMAGE:10 -->
เลเวลสูงเปิดเกาะใหม่
<!-- SOURCE_IMAGE:11 -->
## เทรดอย่างไร?
ก่อนเลเวล 700 การทิ้งผลไม้ไม่มีระบบคุ้มครอง
<!-- SOURCE_IMAGE:12 -->
เลเวล 700 เปิดคาเฟ่ ผลไม้บางอย่างแลกได้
<!-- SOURCE_IMAGE:13 -->
<!-- SOURCE_IMAGE:14 -->
## ใช้ UgPhone อย่างไร?
สร้างเครื่องคลาวด์ ติดตั้ง Roblox ทดสอบดาเมจ จุดเกิด และเน็ต UgPhone ลดความร้อน
<!-- SOURCE_IMAGE:15 -->
## สรุป
เริ่มจากศัตรูหนึ่งตัว ดูหลายรอบก่อนปล่อย ทดสอบใหม่เมื่อเปลี่ยนเกาะหรือผลไม้ หากต้องการรันวิธีที่อนุญาต ให้ **ดาวน์โหลด UgPhone และทดลองใช้ฟรี** แล้วค่อยขยายเวลา
''')
b('Traditional-Chinese',r'''# Blox Fruits掛機攻略：穩定練級、配點與交易

Blox Fruits需反覆擊殺累積經驗、金錢與熟練度，卻沒有自動模式。穩定掛機取決於免疫、站位與準星。本篇 **Blox Fruits掛機攻略** 整理設定、14級Monkey收益、養成與交易，適合想用雲端減少手機負擔的玩家。
<!-- SOURCE_IMAGE:1 -->
## Blox Fruits是什麼？
這款Roblox動作RPG可用近戰、劍、槍與果實。果實每小時生成，20分鐘後消失；商人每4小時補貨。
## 如何設定穩定掛機？
裝備武器並對準重生敵人；被推離位置，連點就會落空。
<!-- SOURCE_IMAGE:2 -->
把 **Ability Control Scheme** 改成 **Modern**。
<!-- SOURCE_IMAGE:3 -->
關閉視角晃動、開啟快速模式並減少動效。
<!-- SOURCE_IMAGE:4 -->
選擇標示免疫攻擊的果實，實測後再離開。
<!-- SOURCE_IMAGE:5 -->
吃下果實確認能力生效。
<!-- SOURCE_IMAGE:6 -->
準星鎖定重生點，連點器放技能鍵；角度偏移就重設。
<!-- SOURCE_IMAGE:7 -->
## 收益與養成怎麼安排？
擊殺可得經驗、金錢與武器熟練度。
<!-- SOURCE_IMAGE:8 -->
UgPhone刷14級Monkey，一小時約得 **20,082經驗與7,191金錢**，僅是樣本。
<!-- SOURCE_IMAGE:9 -->
24小時推算為481,968經驗與172,584金錢，斷線或漏招會降低結果。
<!-- SOURCE_IMAGE:10 -->
屬性點集中主要輸出與防禦。
<!-- SOURCE_IMAGE:11 -->
金錢可向商人買裝備。
<!-- SOURCE_IMAGE:12 -->
升級會開放新島嶼，換區後重新測試。
<!-- SOURCE_IMAGE:13 -->
## Blox Fruits如何交易？
700級前丟果實沒有保護。
<!-- SOURCE_IMAGE:14 -->
700級解鎖咖啡館正式交易；部分果實和道具可換，Beli、碎片、劍與槍不可。
<!-- SOURCE_IMAGE:15 -->
## 如何用UgPhone執行？
建立雲手機、安裝Roblox，短測傷害、重生、熟練度與連線。UgPhone可減少發熱，但不能修正站位或繞過規則。
## 結語
先短測再長掛，更換島嶼、果實或目標後都要重測。每日收益只是估算。若要執行允許的練級流程，可 **下載UgPhone並申請免費試用**，確認穩定後再延長。
''')
