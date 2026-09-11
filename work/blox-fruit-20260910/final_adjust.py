from pathlib import Path

ROOT = Path(__file__).parent / "packages"


def body(name, value):
    p = ROOT / f"{name}.md"
    t = p.read_text(encoding="utf-8")
    a, b = t.index("## Article Body"), t.index("## Image Plan")
    p.write_text(t[:a] + "## Article Body\n\n" + value.strip() + "\n\n" + t[b:], encoding="utf-8")


p = ROOT / "Traditional-Chinese.md"
t = p.read_text(encoding="utf-8").replace(
    "Blox Fruits掛機攻略整理戰鬥設定、果實免傷條件、實測收益、屬性配點、島嶼解鎖與700級交易流程，並說明如何用UgPhone穩定執行。",
    "Blox Fruits掛機攻略整理戰鬥設定、果實免傷條件、實測收益、屬性配點、島嶼解鎖與700級交易流程，並說明如何用UgPhone穩定執行長時間練級。",
)
p.write_text(t, encoding="utf-8")

body("Traditional-Chinese", r'''
# Blox Fruits掛機攻略：穩定練級、配點與交易

Blox Fruits要反覆擊殺敵人，才能累積經驗、金錢與武器熟練度，但沒有內建自動模式。穩定掛機取決於敵人是否會擊退角色、果實能否免疫該目標，以及準星是否留在重生點。本篇 **Blox Fruits掛機攻略** 整理控制設定、14級Monkey收益、屬性養成與交易限制，先看完整循環，再決定是否延長。

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

先用單一敵人與技能測試，至少看完數次擊殺和重生；更換島嶼、果實、武器或目標後都要重測。每日收益只是樣本推算，遇到斷線或位移必須檢查。若要在不長時間佔用手機的情況下執行允許的練級流程，可 **下載UgPhone並申請免費試用**。確認傷害、熟練度與連線正常，再逐步延長時數。
''')

body("Indonesian", r'''
# Panduan AFK Blox Fruits: level, build, dan perdagangan

Blox Fruits menuntut pemain mengalahkan musuh berulang kali demi pengalaman, uang, dan mastery, tetapi tidak menyediakan mode otomatis. Rutinitas hanya stabil jika target tidak menginterupsi karakter, buah menahan damage musuh tersebut, dan crosshair tetap di titik respawn. **Panduan AFK Blox Fruits** ini merangkum pengaturan sumber, uji Monkey level 14, serta keputusan progres dan perdagangan. Perhatikan beberapa siklus penuh sebelum meninggalkan perangkat agar waktu farming tidak terbuang.

<!-- SOURCE_IMAGE:1 -->

## Apa itu Blox Fruits?

RPG aksi Roblox ini memakai melee, pedang, pistol, dan kemampuan buah. Buah muncul tiap jam, hilang setelah 20 menit, dan stok dealer berubah setiap empat jam.

## Bagaimana menyiapkan AFK yang stabil?

Pasang senjata yang ingin dilatih dan bidik lokasi respawn. Musuh dapat melawan serta mendorong karakter.

<!-- SOURCE_IMAGE:2 -->

Ubah **Ability Control Scheme** menjadi **Modern**.

<!-- SOURCE_IMAGE:3 -->

Matikan guncangan kamera, aktifkan Fast Mode, dan kurangi efek.

<!-- SOURCE_IMAGE:4 -->

Pilih buah yang keterangannya memberi imun terhadap target, lalu uji pada musuh tersebut.

<!-- SOURCE_IMAGE:5 -->

Makan buah dan pastikan kemampuannya aktif.

<!-- SOURCE_IMAGE:6 -->

Arahkan crosshair ke respawn dan titik clicker ke satu skill. Amati beberapa siklus; atur ulang jika sudut berubah.

<!-- SOURCE_IMAGE:7 -->

## Berapa hasil farming dan bagaimana progresnya?

Musuh memberi pengalaman dan uang; senjata yang dipakai memperoleh mastery.

<!-- SOURCE_IMAGE:8 -->

Uji UgPhone melawan Monkey level 14 mencatat sekitar **20.082 pengalaman dan 7.191 uang dalam satu jam**. Ini sampel, bukan hasil pasti.

<!-- SOURCE_IMAGE:9 -->

Proyeksi 24 jam adalah 481.968 pengalaman dan 172.584 uang, tetapi koneksi, gerakan, dan serangan meleset mengurangi hasil.

<!-- SOURCE_IMAGE:10 -->

Fokuskan poin pada damage utama dan defense.

<!-- SOURCE_IMAGE:11 -->

Gunakan uang untuk membeli perlengkapan.

<!-- SOURCE_IMAGE:12 -->

Level tinggi membuka pulau sulit; uji ulang imun dan posisi setelah pindah.

<!-- SOURCE_IMAGE:13 -->

## Bagaimana perdagangan Blox Fruits bekerja?

Sebelum level 700, menjatuhkan buah fisik tidak memiliki perlindungan transaksi.

<!-- SOURCE_IMAGE:14 -->

Pada level 700, Café membuka perdagangan resmi saat dua pemain duduk berhadapan. Buah fisik, permanen, gamepass tertentu, dan scroll bisa diperdagangkan; Beli, Fragment, pedang, dan pistol tidak.

<!-- SOURCE_IMAGE:15 -->

## Bagaimana memakai UgPhone untuk Blox Fruits?

Buat perangkat cloud, instal Roblox, pilih target aman, lalu uji damage, respawn, mastery, dan koneksi. UgPhone mengurangi panas serta baterai ponsel, tetapi tidak memperbaiki posisi buruk atau melewati aturan game.

## Kesimpulan

Mulailah dengan satu musuh dan satu skill, lalu amati beberapa respawn lengkap. Uji kembali setelah mengganti pulau, buah, senjata, atau target karena imun dan bidikan bisa berubah. Anggap proyeksi harian sebagai perkiraan dan periksa progres setelah gangguan koneksi. Untuk sesi yang diizinkan tanpa terus memakai ponsel, **unduh UgPhone dan mulai uji coba gratis**. Perpanjang waktu hanya setelah tes singkat stabil dan mastery tetap bertambah.
''')

body("Vietnamese", r'''
# Hướng dẫn AFK Blox Fruits: lên cấp, chỉ số và giao dịch

Blox Fruits yêu cầu đánh lặp kẻ địch để nhận kinh nghiệm, tiền và độ thành thạo, nhưng không có chế độ tự động. Vòng đánh chỉ ổn định khi mục tiêu không làm gián đoạn nhân vật, trái chặn sát thương của nó và tâm ngắm ở điểm hồi sinh. **Hướng dẫn AFK Blox Fruits** này tóm tắt cài đặt, thử nghiệm Monkey cấp 14 và lựa chọn tiến trình. Hãy kiểm tra nhiều vòng trước khi kéo dài phiên để tránh farm vô ích.

<!-- SOURCE_IMAGE:1 -->

## Blox Fruits là gì?

RPG hành động Roblox có cận chiến, kiếm, súng và năng lực trái. Trái xuất hiện mỗi giờ, biến mất sau 20 phút; đại lý đổi kho sau bốn giờ.

## Thiết lập AFK ổn định thế nào?

Trang bị vũ khí cần luyện và ngắm điểm hồi sinh. Kẻ địch có thể phản công, đẩy nhân vật lệch chỗ.

<!-- SOURCE_IMAGE:2 -->

Đổi **Ability Control Scheme** thành **Modern**.

<!-- SOURCE_IMAGE:3 -->

Tắt rung camera, bật Fast Mode và giảm hiệu ứng.

<!-- SOURCE_IMAGE:4 -->

Chọn trái có mô tả miễn đòn của mục tiêu rồi thử với đúng kẻ địch.

<!-- SOURCE_IMAGE:5 -->

Ăn trái và xác nhận năng lực đã bật.

<!-- SOURCE_IMAGE:6 -->

Đặt tâm ngắm vào respawn, điểm lặp trên kỹ năng. Theo dõi vài chu kỳ và chỉnh lại nếu góc đổi.

<!-- SOURCE_IMAGE:7 -->

## Thu nhập và tiến trình ra sao?

Kẻ địch cho kinh nghiệm, tiền; vũ khí đang cầm tăng độ thành thạo.

<!-- SOURCE_IMAGE:8 -->

Thử UgPhone với Monkey cấp 14 ghi khoảng **20.082 kinh nghiệm và 7.191 tiền trong một giờ**. Đây là mẫu tham khảo.

<!-- SOURCE_IMAGE:9 -->

Dự kiến 24 giờ là 481.968 kinh nghiệm và 172.584 tiền; mất mạng, lệch chỗ hoặc hụt đòn làm giảm kết quả.

<!-- SOURCE_IMAGE:10 -->

Dồn điểm vào sát thương chính và phòng thủ.

<!-- SOURCE_IMAGE:11 -->

Dùng tiền mua trang bị.

<!-- SOURCE_IMAGE:12 -->

Cấp cao mở đảo khó hơn; thử lại miễn sát thương và vị trí.

<!-- SOURCE_IMAGE:13 -->

## Giao dịch Blox Fruits thế nào?

Trước cấp 700, thả trái vật lý không có bảo vệ.

<!-- SOURCE_IMAGE:14 -->

Ở cấp 700, Café mở giao dịch khi hai người ngồi đối diện. Trái vật lý, trái vĩnh viễn, một số gamepass và cuộn có thể đổi; Beli, Fragment, kiếm và súng thì không.

<!-- SOURCE_IMAGE:15 -->

## Dùng UgPhone cho Blox Fruits ra sao?

Tạo thiết bị đám mây, cài Roblox, chọn mục tiêu và thử sát thương, hồi sinh, độ thành thạo, kết nối trong vài phút. UgPhone giảm nhiệt điện thoại nhưng không sửa vị trí kém hoặc bỏ qua luật game.

## Kết luận

Bắt đầu với một kẻ địch, một kỹ năng và vài lần hồi sinh. Thử lại khi đổi đảo, trái, vũ khí hoặc mục tiêu vì góc ngắm có thể thay đổi. Xem thu nhập ngày là ước tính và kiểm tra sau lỗi mạng. Để chạy phiên được phép mà không chiếm điện thoại, **hãy tải UgPhone và bắt đầu dùng thử miễn phí**. Chỉ kéo dài khi thử nghiệm ngắn ổn định và độ thành thạo vẫn tăng.
''')

def patch_text(name, replacements):
    p = ROOT / f"{name}.md"
    t = p.read_text(encoding="utf-8")
    for old, new in replacements:
        if old not in t:
            raise ValueError(f"Missing replacement in {name}: {old[:30]}")
        t = t.replace(old, new, 1)
    p.write_text(t, encoding="utf-8")


patch_text("Indonesian", [
    ("Tujuannya adalah menguji loop sebelum memperpanjang sesi.", "Tujuannya adalah menguji loop sebelum memperpanjang sesi, sehingga karakter tidak berhenti setelah beberapa menit. Catat mastery dan uang agar Anda dapat membandingkan hasil setiap target, lalu pindahkan farming hanya ketika posisi dan koneksi sudah terbukti stabil."),
    ("Gunakan uang untuk membeli perlengkapan.", "Gunakan uang untuk membeli perlengkapan, lalu pilih senjata yang mastery-nya memang ingin dinaikkan."),
])

patch_text("Traditional-Chinese", [
    ("Blox Fruits要反覆擊殺敵人，才能累積經驗、金錢與武器熟練度，但沒有內建自動模式。穩定掛機取決於敵人是否會擊退角色、果實能否免疫該目標，以及準星是否留在重生點。本篇 **Blox Fruits掛機攻略** 整理控制設定、14級Monkey收益、屬性養成與交易限制，先看完整循環，再決定是否延長。", "Blox Fruits要反覆擊殺敵人累積經驗、金錢與熟練度，卻沒有內建自動模式。穩定掛機取決於敵人會否擊退角色、果實能否免疫目標，以及準星能否留在重生點。本篇 **Blox Fruits掛機攻略** 整理設定、14級Monkey收益、養成與交易限制，也適合想把練級交給雲端、避免長時間佔用手機的玩家。先看完整循環，再決定是否延長。"),
    ("這款Roblox動作RPG可用近戰、劍、槍和果實能力。果實每小時生成，20分鐘後消失；商人每4小時隨機補貨。", "這款Roblox動作RPG可用近戰、劍、槍與果實。果實每小時生成，20分鐘後消失；商人每4小時補貨。"),
    ("裝備要培養的武器，對準固定重生的敵人；若被推離位置，連點仍會落空。", "裝備要培養的武器並對準重生敵人；被推離位置，連點就會落空。"),
    ("關閉視角晃動，開啟快速模式並減少動效。", "關閉視角晃動、開啟快速模式並減少動效。"),
    ("按相同速率推算24小時為481,968經驗與172,584金錢；斷線、位移和漏招會降低結果。", "同速推算24小時為481,968經驗與172,584金錢；斷線、位移或漏招會降低結果。"),
    ("確認傷害、熟練度與連線正常，再逐步延長時數。", "確認傷害、熟練度與連線正常，再延長。先驗證，再長掛。"),
])

body("Thai", r'''
# คู่มือ AFK Blox Fruits: เก็บเลเวล ค่าสถานะ และเทรด

Blox Fruits ต้องตีศัตรูซ้ำเพื่อรับ EXP เงิน และความชำนาญ แต่ไม่มีโหมดอัตโนมัติ วงจรจะนิ่งเมื่อศัตรูผลักไม่ได้ ผลไม้กันดาเมจ และเป้ายังตรงจุดเกิด **คู่มือ AFK Blox Fruits** นี้สรุปค่าตั้ง ผลทดสอบ Monkey เลเวล 14 และข้อจำกัดการเทรด

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
