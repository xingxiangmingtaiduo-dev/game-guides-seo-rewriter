from pathlib import Path

R = Path(__file__).parent / 'packages'

def rep(n, o, x):
    p = R / f'{n}.md'
    t = p.read_text(encoding='utf-8')
    p.write_text(t.replace(o, x, 1), encoding='utf-8')

rep('Indonesian', 'Gunakan uang untuk membeli perlengkapan dari pedagang dan pilih senjata yang mastery-nya memang ingin dinaikkan.', 'Gunakan uang untuk membeli perlengkapan dari pedagang dan pilih senjata yang mastery-nya ingin dinaikkan. Bandingkan hasil tiap target, cek koneksi, lalu ubah lokasi hanya setelah loop aman.')
rep('Traditional-Chinese', '每日收益只是樣本推算，遇到斷線或位移必須檢查。', '每日收益只是樣本推算，遇到斷線或位移必須檢查角色、技能與連線。')
rep('Traditional-Chinese', 'Blox Fruits掛機攻略整理戰鬥設定、果實免傷、實測收益、配點、島嶼解鎖、700級交易與UgPhone練級。', 'Blox Fruits掛機攻略整理戰鬥設定、果實免傷、收益、配點、島嶼、交易與UgPhone練級流程，方便查找。')
rep('Thai', 'รายได้เป็นค่าคาดการณ์ หากต้องการรันวิธีที่อนุญาตโดยไม่ใช้มือถือค้าง ให้ **ดาวน์โหลด UgPhone และทดลองใช้ฟรี** ตรวจว่า EXP กับความชำนาญยังเพิ่ม แล้วค่อยขยายเวลา', 'รายได้เป็นค่าคาดการณ์ หากต้องการรันวิธีที่อนุญาต ให้ **ดาวน์โหลด UgPhone และทดลองใช้ฟรี** ตรวจว่า EXP ยังเพิ่ม แล้วค่อยขยายเวลา')
rep('Thai', 'เลเวล 700 เปิดคาเฟ่เทรด ผลไม้และไอเทมบางอย่างแลกได้ แต่เงิน เศษ ดาบ และปืนแลกไม่ได้', 'เลเวล 700 เปิดคาเฟ่ ผลไม้บางอย่างแลกได้ แต่เงิน ดาบ และปืนแลกไม่ได้')
rep('Thai', 'เกม Roblox ใช้หมัด ดาบ ปืน หรือผลไม้ ผลไม้เกิดทุกชั่วโมง หายใน 20 นาที ร้านสุ่มทุก 4 ชั่วโมง', 'เกม Roblox ใช้หมัด ดาบ ปืน ผลไม้เกิดทุกชั่วโมงและหายใน 20 นาที')
