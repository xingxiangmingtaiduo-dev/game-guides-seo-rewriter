from pathlib import Path
import re

ROOT=Path(__file__).parent/'packages'

def replace_body(name, body):
    p=ROOT/(name+'.md'); t=p.read_text(encoding='utf-8')
    t=re.sub(r'(?ms)(^## Article Body\s*\n).*?(?=^## Image Plan\s*$)',lambda m:m.group(1)+'\n'+body.strip()+'\n\n',t)
    p.write_text(t,encoding='utf-8')

pt='''# Guia AFK de Steal an egg: ovos, pets e velocidade

Um ovo raro não ajuda se o dono alcançar você antes da zona segura. Em Steal an egg, velocidade define as áreas acessíveis, a chance de fuga e quem chega primeiro. Na base, ovos roubados chocam pets que geram dinheiro até quando você está offline. Este **Guia AFK de Steal an egg** mostra como escolher rotas, aproveitar o ciclo diário, melhorar pets e treinar velocidade sem depender de macros frágeis. O objetivo é transformar cada roubo em progresso, não apenas correr atrás do maior ovo visível.

## O que é Steal an egg?

O jogo é PVE: os ovos pertencem a NPCs, embora os jogadores disputem quem os pega primeiro.

<!-- SOURCE_IMAGE:1 -->

Pegue o ovo, vire para a base e mantenha a câmera alinhada com o retorno. Se o dono alcançar você, o roubo falha.

<!-- SOURCE_IMAGE:2 -->

Zonas distantes oferecem ovos melhores, mas deixam menos margem para erro.

<!-- SOURCE_IMAGE:3 -->

Cada placa indica uma velocidade recomendada. Use-a como referência, nunca como garantia.

<!-- SOURCE_IMAGE:4 -->

## Como funciona o ciclo de dia e noite?

O dia dura cerca de cinco minutos e a noite, dez segundos. Roube durante o dia e use a noite para esperar a renovação. Um ovo divino gera anúncio com a zona; vá somente se sua velocidade suportar a rota e a disputa. Ovos grandes costumam ter qualidade maior, mas um ovo próximo e seguro pode render mais no longo prazo.

<!-- SOURCE_IMAGE:5 -->

## Como gerenciar ovos, pets e a base?

Coloque cada ovo roubado em casa. O tempo de eclosão varia, e a abertura final é manual.

<!-- SOURCE_IMAGE:6 -->

Use a seleção automática para equipar seus pets mais fortes e aumentar a renda offline.

<!-- SOURCE_IMAGE:7 -->

Melhore a casa para liberar mais espaços de pets e ampliar o ganho constante.

<!-- SOURCE_IMAGE:8 -->

O guia mostra os pets de cada zona. Completar coleções concede dinheiro e velocidade.

<!-- SOURCE_IMAGE:9 -->

Venda pets fracos ou excedentes para recuperar dinheiro.

<!-- SOURCE_IMAGE:10 -->

Combine três pets iguais para obter uma unidade de nível superior.

<!-- SOURCE_IMAGE:11 -->

## Qual é o melhor AFK para velocidade?

A esteira é o alvo mais previsível, pois aumenta velocidade continuamente. Observe alguns minutos e confirme que o valor ainda sobe antes de deixar a sessão.

<!-- SOURCE_IMAGE:12 -->

O multiplicador da loja de rastros melhora cada ciclo de treino.

<!-- SOURCE_IMAGE:13 -->

Macros não combinam bem com o roubo: a qualidade do ovo é aleatória, a volta exige câmera e botão de corrida pressionado, e a noite interrompe a rota.

<!-- SOURCE_IMAGE:14 -->

## Como usar o UgPhone?

Crie um dispositivo em nuvem, instale Roblox e coloque o personagem na esteira. Faça um teste curto, confira velocidade, posição e conexão, depois aumente o tempo. O UgPhone reduz calor e uso do celular físico, mas não garante ovos raros nem corrige uma rota ruim.

<!-- SOURCE_IMAGE:15 -->

## Conclusão

Treine antes de avançar para zonas distantes e compare sua velocidade com a placa local. Abra os ovos prontos, equipe os melhores pets, venda unidades fracas e combine duplicatas. Para AFK, valide primeiro se a esteira continua registrando progresso; verifique novamente após uma queda de conexão. Se quiser manter esse treino permitido na nuvem sem ocupar o celular, **baixe o UgPhone e solicite um teste gratuito**. Comece com poucos minutos e prolongue a sessão somente quando o ganho permanecer estável.'''
replace_body('Portuguese',pt)

es='''# Guía AFK de Steal an egg: huevos, mascotas y velocidad

Un huevo raro no sirve si su dueño te alcanza antes de volver a la zona segura. En Steal an egg, la velocidad determina las áreas disponibles, la posibilidad de escapar y quién llega primero. En la base, los huevos robados incuban mascotas que producen dinero incluso sin conexión. Esta **Guía AFK de Steal an egg** explica cómo elegir rutas, aprovechar el ciclo diario, mejorar mascotas y entrenar velocidad sin depender de macros frágiles. La meta es convertir cada robo en progreso, no perseguir siempre el huevo más grande.

## ¿Qué es Steal an egg?

El juego es PVE: los huevos pertenecen a NPC, aunque los jugadores compiten por recogerlos primero.

<!-- SOURCE_IMAGE:1 -->

Toma el huevo, gira hacia la base y mantén la cámara alineada con el regreso. Si el dueño te alcanza, el robo falla.

<!-- SOURCE_IMAGE:2 -->

Las zonas lejanas ofrecen huevos mejores, pero dejan menos margen para equivocarse.

<!-- SOURCE_IMAGE:3 -->

Cada cartel indica una velocidad recomendada. Úsala como referencia, no como garantía.

<!-- SOURCE_IMAGE:4 -->

## ¿Cómo funciona el ciclo de día y noche?

El día dura unos cinco minutos y la noche, diez segundos. Roba durante el día y espera la renovación por la noche. Un huevo divino genera un aviso con su zona; ve solo si tu velocidad permite completar la ruta entre la multitud. Los huevos grandes suelen tener más calidad, pero uno cercano y seguro puede dar mejores resultados constantes.

<!-- SOURCE_IMAGE:5 -->

## ¿Cómo gestionar huevos, mascotas y la base?

Coloca cada huevo robado en casa. El tiempo de incubación cambia y la apertura final es manual.

<!-- SOURCE_IMAGE:6 -->

Usa la selección automática para equipar las mascotas más fuertes y mejorar los ingresos sin conexión.

<!-- SOURCE_IMAGE:7 -->

Mejora la casa para liberar más espacios de mascotas y aumentar el ingreso estable.

<!-- SOURCE_IMAGE:8 -->

La guía muestra las mascotas de cada zona. Completar colecciones entrega dinero y velocidad.

<!-- SOURCE_IMAGE:9 -->

Vende mascotas débiles o sobrantes para recuperar dinero.

<!-- SOURCE_IMAGE:10 -->

Combina tres mascotas iguales para conseguir una unidad de nivel superior.

<!-- SOURCE_IMAGE:11 -->

## ¿Cuál es el mejor AFK para ganar velocidad?

La cinta es el objetivo más predecible porque aumenta la velocidad continuamente. Observa unos minutos y confirma que el valor sigue subiendo antes de dejar la sesión.

<!-- SOURCE_IMAGE:12 -->

El multiplicador de la tienda de rastros mejora cada ciclo de entrenamiento.

<!-- SOURCE_IMAGE:13 -->

Las macros no encajan con el robo: la calidad es aleatoria, el regreso exige controlar la cámara y mantener pulsado correr, y la noche interrumpe la ruta.

<!-- SOURCE_IMAGE:14 -->

## ¿Cómo usar UgPhone?

Crea un dispositivo en la nube, instala Roblox y coloca al personaje en la cinta. Haz una prueba breve, revisa velocidad, posición y conexión, y después amplía el tiempo. UgPhone reduce el calor y el uso del teléfono físico, pero no garantiza huevos raros ni corrige una ruta inadecuada.

<!-- SOURCE_IMAGE:15 -->

## Conclusión

Entrena antes de avanzar a zonas lejanas y compara tu velocidad con el cartel local. Abre los huevos listos, equipa las mejores mascotas, vende unidades débiles y combina duplicados. Para AFK, comprueba primero que la cinta sigue registrando progreso y revisa otra vez después de una desconexión. Si quieres mantener este entrenamiento permitido en la nube sin ocupar el teléfono, **descarga UgPhone y solicita una prueba gratuita**. Empieza con pocos minutos y prolonga la sesión solo cuando la ganancia permanezca estable.'''
replace_body('Spanish',es)

vi='''# Hướng dẫn AFK Steal an egg: trứng, pet và tốc độ

Trứng hiếm không có giá trị nếu chủ trứng bắt kịp bạn trước khi về vùng an toàn. Trong Steal an egg, tốc độ quyết định khu vực có thể vào, khả năng chạy thoát và ai chạm tới trứng trước. Tại căn cứ, trứng trộm được sẽ ấp thành pet tạo tiền ngay cả khi ngoại tuyến. **Hướng dẫn AFK Steal an egg** này kết nối các cơ chế đó: chọn đường chạy phù hợp, tận dụng chu kỳ ngày đêm, nâng pet và luyện tốc độ mà không phụ thuộc vào macro dễ lỗi. Mục tiêu là biến mỗi lần trộm thành tiến độ thực tế.

## Steal an egg là gì?

Đây là lối chơi PVE: trứng thuộc NPC, nhưng người chơi vẫn tranh nhau lấy trước.

<!-- SOURCE_IMAGE:1 -->

Nhặt trứng, quay về căn cứ và giữ camera hướng theo đường chạy. Bị chủ trứng đuổi kịp đồng nghĩa thất bại.

<!-- SOURCE_IMAGE:2 -->

Khu vực xa có nhóm trứng tốt hơn nhưng ít chỗ cho sai sót.

<!-- SOURCE_IMAGE:3 -->

Mỗi biển báo ghi tốc độ đề xuất. Hãy xem đó là mốc tham khảo, không phải bảo đảm.

<!-- SOURCE_IMAGE:4 -->

## Chu kỳ ngày đêm ảnh hưởng thế nào?

Ban ngày kéo dài khoảng năm phút, ban đêm khoảng mười giây. Hãy trộm trứng ban ngày và chờ làm mới vào ban đêm. Khi trứng thần thánh xuất hiện, thông báo sẽ chỉ khu vực; chỉ nên đến nếu tốc độ đủ xử lý đường về và đám đông. Trứng lớn thường tốt hơn, nhưng lấy trứng gần và an toàn có thể ổn định hơn.

<!-- SOURCE_IMAGE:5 -->

## Quản lý trứng, pet và căn cứ ra sao?

Đặt trứng đã lấy tại nhà. Thời gian ấp khác nhau và bạn phải tự mở khi hoàn tất.

<!-- SOURCE_IMAGE:6 -->

Dùng lựa chọn tự động để trang bị pet mạnh nhất và tăng thu nhập ngoại tuyến.

<!-- SOURCE_IMAGE:7 -->

Nâng cấp nhà để mở thêm vị trí pet và cải thiện nguồn tiền đều đặn.

<!-- SOURCE_IMAGE:8 -->

Cẩm nang cho biết pet của từng khu vực. Hoàn thành bộ sưu tập nhận tiền và tốc độ.

<!-- SOURCE_IMAGE:9 -->

Bán pet yếu hoặc dư để đổi lấy tiền.

<!-- SOURCE_IMAGE:10 -->

Ghép ba pet giống nhau để nhận một pet cấp cao hơn.

<!-- SOURCE_IMAGE:11 -->

## AFK nào phù hợp để tăng tốc độ?

Máy chạy bộ đáng tin cậy nhất vì tăng tốc độ liên tục. Theo dõi vài phút và xác nhận chỉ số vẫn tăng trước khi rời phiên.

<!-- SOURCE_IMAGE:12 -->

Hệ số từ cửa hàng đường chạy giúp mỗi chu kỳ luyện nhận nhiều tốc độ hơn.

<!-- SOURCE_IMAGE:13 -->

Macro không hợp để trộm trứng: chất lượng ngẫu nhiên, đường về cần chỉnh camera và giữ nút chạy, còn ban đêm làm gián đoạn tuyến.

<!-- SOURCE_IMAGE:14 -->

## Cách dùng UgPhone

Tạo thiết bị đám mây, cài Roblox rồi đặt nhân vật lên máy chạy bộ. Thử ngắn, kiểm tra tốc độ, vị trí và kết nối trước khi kéo dài. UgPhone giảm nhiệt và thời gian chiếm dụng điện thoại, nhưng không bảo đảm trứng hiếm hay sửa được tuyến đường kém.

<!-- SOURCE_IMAGE:15 -->

## Kết luận

Hãy luyện tốc độ trước khi tiến tới khu vực xa và so sánh chỉ số với biển báo. Mở trứng đã ấp xong, trang bị pet tốt nhất, bán pet yếu và ghép bản trùng. Với AFK, cần xác nhận máy chạy bộ vẫn ghi nhận tiến độ và kiểm tra lại sau khi mất kết nối. Nếu muốn duy trì cách luyện được phép trên đám mây mà không chiếm điện thoại, **hãy tải UgPhone và bắt đầu dùng thử miễn phí**. Chỉ tăng thời gian khi phiên thử ngắn hoạt động ổn định.'''
replace_body('Vietnamese',vi)
p=ROOT/'Vietnamese.md'; t=p.read_text(encoding='utf-8')
t=re.sub(r'(?m)^# .+$','# Hướng dẫn AFK Steal an egg: trứng, pet và tốc độ',t,count=1)
t=re.sub(r'(?m)^- SEO Title:.*$','- SEO Title: Hướng dẫn AFK Steal an egg: trứng, pet và tốc độ',t)
t=re.sub(r'(?m)^- Meta Description:.*$','- Meta Description: Hướng dẫn AFK Steal an egg về đường trộm an toàn, thu nhập pet, nâng cấp nhà, luyện máy chạy bộ và thiết lập UgPhone cho phiên dài.',t)
t=t.replace('   - Alt: Steal an egg AFK Guide gameplay overview','   - Alt: Hướng dẫn AFK Steal an egg trên trang trò chơi')
for old,new in [
    ('Trong Steal an egg, tốc độ quyết định khu vực có thể vào, khả năng chạy thoát và ai chạm tới trứng trước. ',''),
    ('Mục tiêu là biến mỗi lần trộm thành tiến độ thực tế.',''),
    ('Đây là lối chơi PVE: trứng thuộc NPC, nhưng người chơi vẫn tranh nhau lấy trước.','Trứng thuộc NPC, nhưng người chơi tranh nhau lấy trước.'),
    ('Khi trứng thần thánh xuất hiện, thông báo sẽ chỉ khu vực; chỉ nên đến nếu tốc độ đủ xử lý đường về và đám đông.','Thông báo trứng thần thánh chỉ rõ khu vực; chỉ đến khi đủ tốc độ.'),
    ('Trứng lớn thường tốt hơn, nhưng lấy trứng gần và an toàn có thể ổn định hơn.','Trứng gần và an toàn đôi khi hiệu quả hơn.'),
    ('Thời gian ấp khác nhau và bạn phải tự mở khi hoàn tất.','Bạn phải tự mở khi ấp xong.'),
    ('Tạo thiết bị đám mây, cài Roblox rồi đặt nhân vật lên máy chạy bộ.','Tạo thiết bị đám mây, cài Roblox và vào máy chạy bộ.'),
]: t=t.replace(old,new)
# Only the first image alt uses the exact primary keyword.
for n in range(10,16):
    t=t.replace(f'Hướng dẫn AFK Steal an egg trên trang trò chơi{n-10}',f'Hình lối chơi Steal an egg số {n}')
p.write_text(t,encoding='utf-8')

zh='''# Steal an egg掛機攻略：偷蛋、孵蛋與練速

《Steal an egg》的難點不是找到蛋，而是安全帶回基地。蛋由NPC守護，拿走後會立刻遭到追擊；速度不足或鏡頭沒對準回程，都可能讓冒險白費。蛋帶回家後會自行孵化，寵物則提供主要金錢收益。本篇 **Steal an egg掛機攻略** 整理區域門檻、日夜刷新、寵物培養與跑步機AFK。先把偷蛋、孵蛋、產錢和練速串成循環，再決定何時前往遠區，能減少無效嘗試，也不必為公告中的高級蛋承擔不合理風險。家園收入能支援速度養成，而速度又會打開更好的蛋池，因此穩定循環比只追一顆公告蛋更重要。

<!-- SOURCE_IMAGE:1 -->

## Steal an egg是什麼？

核心是PVE偷蛋，但玩家會爭搶同一批蛋。拿蛋後立刻轉身，鏡頭對準安全區；被蛋主人追上就算失敗。

<!-- SOURCE_IMAGE:2 -->

遠方區域的蛋池較好，追擊也更難。

<!-- SOURCE_IMAGE:3 -->

區域告示提供建議速度，達標後再嘗試。

<!-- SOURCE_IMAGE:4 -->

## 日夜刷新怎麼跑？

白天約五分鐘，可外出偷蛋；黑夜約十秒，用來等待刷新。神聖蛋會公告區域，但速度不足時，拿附近的安全蛋更有效率。

<!-- SOURCE_IMAGE:5 -->

## 孵蛋與寵物怎麼管理？

蛋放進家園後會倒數孵化，完成時要手動開蛋。

<!-- SOURCE_IMAGE:6 -->

一鍵裝備最佳寵物，可提高離線收入。

<!-- SOURCE_IMAGE:7 -->

升級家園能增加寵物數量。

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

蹤跡商店的速度倍數可提高訓練收益。

<!-- SOURCE_IMAGE:13 -->

偷蛋不適合固定宏：蛋品質隨機、回程要調鏡頭並長按移動，黑夜也會中斷路線。

<!-- SOURCE_IMAGE:14 -->

## 如何用UgPhone訓練？

建立雲手機並安裝Roblox，把角色放上跑步機。短測速度、位置與連線後再延長；UgPhone可減少手機發熱與佔用，但不保證稀有蛋。

<!-- SOURCE_IMAGE:15 -->

## 結語

先在跑步機累積速度，再依告示逐步向外推進；不要為公告蛋跳過無法承擔的路線。孵化完成後手動開蛋，最強寵物優先上場，多餘角色出售或合成。掛機前要短測，確認速度持續增加；黑夜、斷線或角色離開跑步機後都要重新檢查。短測能避免整晚停在無效狀態。若想把允許的跑步機訓練放在雲端，避免長時間佔用手機，可立即下載UgPhone並申請免費試用，確認穩定後再延長時數。'''
replace_body('Traditional-Chinese',zh)
p=ROOT/'Traditional-Chinese.md'; t=p.read_text(encoding='utf-8')
t=re.sub(r'(?m)^# .+$','# Steal an egg掛機攻略：偷蛋、孵蛋與練速',t,count=1)
t=re.sub(r'(?m)^- SEO Title:.*$','- SEO Title: Steal an egg掛機攻略：偷蛋、孵蛋與練速',t)
t=re.sub(r'(?m)^- Meta Description:.*$','- Meta Description: Steal an egg掛機攻略整理安全偷蛋路線、日夜刷新、區域速度門檻、寵物離線收益、家園升級、出售與合成，也說明跑步機訓練、宏指令限制、雲手機設定，以及使用UgPhone長時間掛機前的速度短測、角色位置、網路連線和收益檢查流程，幫助玩家減少整晚無效運行。',t)
for old,new in [
    ('蛋帶回家後會自行孵化，寵物則提供主要金錢收益。','蛋會孵化成能產錢的寵物。'),
    ('先把偷蛋、孵蛋、產錢和練速串成循環，再決定何時前往遠區，能減少無效嘗試，也不必為公告中的高級蛋承擔不合理風險。','先串起偷蛋、孵蛋、產錢和練速，再前往遠區，可減少無效嘗試。'),
    ('核心是PVE偷蛋，但玩家會爭搶同一批蛋。','蛋由NPC持有，玩家會爭搶。'),
    ('拿蛋後立刻轉身，鏡頭對準安全區；被蛋主人追上就算失敗。','拿蛋後對準安全區；被追上就失敗。'),
    ('白天約五分鐘，可外出偷蛋；黑夜約十秒，用來等待刷新。','白天偷蛋，黑夜等待刷新。'),
    ('神聖蛋會公告區域，但速度不足時，拿附近的安全蛋更有效率。','神聖蛋會公告區域，速度不足就拿近處的蛋。'),
    ('建立雲手機並安裝Roblox，把角色放上跑步機。','建立雲手機、安裝Roblox，再站上跑步機。'),
]: t=t.replace(old,new)
p.write_text(t,encoding='utf-8')

th='''# คู่มือ AFK Steal an egg: ไข่ สัตว์เลี้ยง และความเร็ว

ขโมยไข่แล้วต้องหนีกลับก่อนถูกจับ ความเร็วจึงสำคัญ ไข่ฟักเป็นสัตว์เลี้ยงสร้างเงิน **คู่มือ AFK Steal an egg** นี้สรุปเส้นทางและลู่วิ่ง

<!-- SOURCE_IMAGE:1 -->

## Steal an egg คืออะไร?

ไข่เป็นของ NPC แต่ผู้เล่นแย่งกัน

<!-- SOURCE_IMAGE:2 -->

หยิบแล้วกลับฐาน

<!-- SOURCE_IMAGE:3 -->

ถูกจับจะล้มเหลว

<!-- SOURCE_IMAGE:4 -->

โซนไกลให้ไข่ดีกว่า

## วางแผนกลางวันอย่างไร?

กลางวันขโมย กลางคืนรอรีเซ็ต

<!-- SOURCE_IMAGE:5 -->

## จัดการไข่และสัตว์เลี้ยงอย่างไร?

วางไข่รอฟัก

<!-- SOURCE_IMAGE:6 -->

เปิดแล้วเลือกตัวดี

<!-- SOURCE_IMAGE:7 -->

อัปบ้านเพิ่มช่อง

<!-- SOURCE_IMAGE:8 -->

สะสมรับรางวัล

<!-- SOURCE_IMAGE:9 -->

ขายตัวเกิน

<!-- SOURCE_IMAGE:10 -->

รวมสามตัว

<!-- SOURCE_IMAGE:11 -->

## AFK บนลู่วิ่งคุ้มไหม?

ลู่วิ่งเพิ่มความเร็ว ตรวจค่าก่อน AFK

<!-- SOURCE_IMAGE:12 -->

ตัวคูณเพิ่มผลฝึก

<!-- SOURCE_IMAGE:13 -->

มาโครต้องหมุนกล้อง จึงไม่เหมาะ

<!-- SOURCE_IMAGE:14 -->

## ใช้ UgPhone อย่างไร?

ติดตั้ง Roblox บนคลาวด์ แล้วขึ้นลู่วิ่ง ทดสอบก่อนเพิ่มเวลา UgPhone ลดความร้อน แต่ไม่รับประกันไข่หายาก

<!-- SOURCE_IMAGE:15 -->

## สรุป

เพิ่มความเร็วก่อนเข้าโซนไกล เปิดไข่ เลือกตัวทำเงินดี แล้วขายหรือรวมตัวซ้ำ ก่อน AFK ตรวจว่าค่ายังเพิ่มและเน็ตไม่ขาด หากต้องการฝึกโดยไม่เปิดโทรศัพท์ไว้นาน ให้ดาวน์โหลด UgPhone และเริ่มทดลองใช้ฟรี แล้วเพิ่มเวลาเมื่อระบบเสถียร'''
replace_body('Thai',th)

# Final metric-specific tightening for compact CJK and Thai briefs.
p=ROOT/'Traditional-Chinese.md'; t=p.read_text(encoding='utf-8')
t=t.replace('《Steal an egg》的難點','《Steal an egg》的真正難點')
for old,new in [
    ('遠方區域的蛋池較好，追擊也更難。','遠區蛋池較好，追擊更難。'),
    ('區域告示提供建議速度，達標後再嘗試。','告示提供建議速度，達標再嘗試。'),
    ('寵物指引列出各區收藏，完成可領金錢與速度。','指引列出各區收藏，完成可領獎勵。'),
    ('蹤跡商店的速度倍數可提高訓練收益。','商店速度倍數可提高收益。'),
    ('偷蛋不適合固定宏：蛋品質隨機、回程要調鏡頭並長按移動，黑夜也會中斷路線。','偷蛋不適合固定宏：品質隨機、回程要調鏡頭，黑夜也會中斷。'),
]: t=t.replace(old,new)
p.write_text(t,encoding='utf-8')

p=ROOT/'Thai.md'; t=p.read_text(encoding='utf-8')
for old,new in [
    ('ไข่เป็นของ NPC แต่ผู้เล่นแย่งกัน','ไข่เป็นของ NPC'),
    ('โซนไกลให้ไข่ดีกว่า','โซนไกลไข่ดี'),
    ('กลางวันขโมย กลางคืนรอรีเซ็ต','กลางวันขโมย กลางคืนรีเซ็ต'),
    ('ลู่วิ่งเพิ่มความเร็ว ตรวจค่าก่อน AFK','ลู่วิ่งเพิ่มความเร็ว'),
    ('มาโครต้องหมุนกล้อง จึงไม่เหมาะ','มาโครต้องหมุนกล้อง'),
    ('ติดตั้ง Roblox บนคลาวด์ แล้วขึ้นลู่วิ่ง ทดสอบก่อนเพิ่มเวลา UgPhone ลดความร้อน แต่ไม่รับประกันไข่หายาก','ติดตั้ง Roblox บนคลาวด์ แล้วขึ้นลู่วิ่ง ทดสอบก่อนเพิ่มเวลา UgPhone ลดความร้อน'),
    ('เพิ่มความเร็วก่อนเข้าโซนไกล เปิดไข่ เลือกตัวทำเงินดี แล้วขายหรือรวมตัวซ้ำ ก่อน AFK ตรวจว่าค่ายังเพิ่มและเน็ตไม่ขาด หากต้องการฝึกโดยไม่เปิดโทรศัพท์ไว้นาน ให้ดาวน์โหลด UgPhone และเริ่มทดลองใช้ฟรี แล้วเพิ่มเวลาเมื่อระบบเสถียร','เพิ่มความเร็วก่อนเข้าโซนไกล เปิดไข่ เลือกตัวทำเงินดี แล้วขายหรือรวมตัวซ้ำ ก่อน AFK ตรวจค่าและเน็ต หากต้องการฝึกบนคลาวด์ ให้ดาวน์โหลด UgPhone และเริ่มทดลองใช้ฟรี แล้วเพิ่มเวลาเมื่อระบบเสถียร'),
    ('ติดตั้ง Roblox บนคลาวด์ แล้วขึ้นลู่วิ่ง','ติดตั้ง Roblox บนคลาวด์และขึ้นลู่วิ่ง'),
    ('ทดสอบก่อนเพิ่มเวลา','ทดสอบก่อน'),
    ('เลือกตัวทำเงินดี แล้วขายหรือรวมตัวซ้ำ','เลือกตัวดี ขายหรือรวมตัวซ้ำ'),
    ('แล้วเพิ่มเวลาเมื่อระบบเสถียร','แล้วเพิ่มเวลาเมื่อเสถียร'),
    ('ไข่ฟักเป็นสัตว์เลี้ยงสร้างเงิน','ไข่ฟักเป็นสัตว์เลี้ยง'),
    ('โซนไกลไข่ดี','โซนไกลดีกว่า'),
    ('อัปบ้านเพิ่มช่อง','อัปบ้าน'),
    ('ตัวคูณเพิ่มผลฝึก','ตัวคูณเพิ่มผล'),
    ('เพิ่มความเร็วก่อนเข้าโซนไกล','เพิ่มความเร็วก่อนโซนไกล'),
    ('ขายหรือรวมตัวซ้ำ','ขายหรือรวมตัว'),
    ('ก่อน AFK ตรวจค่าและเน็ต','ก่อน AFK ตรวจเน็ต'),
    ('แล้วเพิ่มเวลาเมื่อเสถียร','เพิ่มเวลาเมื่อเสถียร'),
]: t=t.replace(old,new)
p.write_text(t,encoding='utf-8')
