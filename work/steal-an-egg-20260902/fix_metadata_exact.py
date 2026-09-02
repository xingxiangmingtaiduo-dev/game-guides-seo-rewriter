from pathlib import Path
import re
root=Path(__file__).parent/'packages'
data={
'Traditional-Chinese':('偷蛋掛機攻略涵蓋偷蛋、安全逃生、區域速度檢查、寵物孵化、家園升級、跑步機訓練、AFK計時，以及長時間使用UgPhone的實用設定。','偷蛋掛機攻略、Roblox偷蛋、寵物孵化、UgPhone雲端手機','偷蛋掛機攻略、Roblox、AFK、寵物、UgPhone'),
'Portuguese':('Este guia AFK de Steal an egg cobre roubo de ovos, fugas seguras, velocidade por zona, incubação de pets, melhorias da casa, treino na esteira, tempo AFK e configuração prática do UgPhone.','Steal an egg AFK, roubar ovos no Roblox, incubar pets, UgPhone','Steal an egg, Roblox, AFK, Pets, UgPhone'),
'Spanish':('Esta guía AFK de Steal an egg explica cómo robar huevos, escapar con seguridad, comprobar la velocidad de cada zona, incubar mascotas, mejorar la base y configurar UgPhone para sesiones AFK largas.','Steal an egg AFK, robar huevos en Roblox, incubar mascotas, UgPhone','Steal an egg, Roblox, AFK, Mascotas, UgPhone'),
'Thai':('คู่มือ AFK Steal an egg นี้อธิบายการขโมยไข่ การหนีอย่างปลอดภัย การตรวจความเร็วแต่ละโซน การฟักสัตว์เลี้ยง การอัปเกรดบ้าน การฝึกบนลู่วิ่ง และการตั้งค่า UgPhone สำหรับการเล่น AFK ระยะยาว','Steal an egg AFK, ขโมยไข่ใน Roblox, ฟักสัตว์เลี้ยง, UgPhone','Steal an egg, Roblox, AFK, สัตว์เลี้ยง, UgPhone'),
'Indonesian':('Panduan AFK Steal an egg ini membahas cara mencuri telur, melarikan diri dengan aman, memeriksa kecepatan zona, menetaskan pet, meningkatkan rumah, berlatih di treadmill, dan mengatur UgPhone untuk sesi AFK panjang.','Steal an egg AFK, mencuri telur Roblox, menetaskan pet, UgPhone','Steal an egg, Roblox, AFK, Pet, UgPhone'),
'Vietnamese':('Hướng dẫn AFK Steal an egg này trình bày cách trộm trứng, chạy về an toàn, kiểm tra tốc độ từng khu vực, ấp pet, nâng cấp nhà, luyện trên máy chạy bộ và thiết lập UgPhone cho phiên AFK dài.','Steal an egg AFK, trộm trứng Roblox, ấp pet, UgPhone','Steal an egg, Roblox, AFK, Pet, UgPhone')}
for lang,(desc,secondary,tags) in data.items():
 p=root/(lang+'.md'); t=p.read_text(encoding='utf-8'); t=re.sub(r'(?m)^- Meta Description:.*$', '- Meta Description: '+desc,t); t=re.sub(r'(?m)^- Secondary Keywords:.*$', '- Secondary Keywords: '+secondary,t); t=re.sub(r'(?m)^- Tags:.*$', '- Tags: '+tags,t); p.write_text(t,encoding='utf-8')
