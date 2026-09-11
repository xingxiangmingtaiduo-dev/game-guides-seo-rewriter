from pathlib import Path


ROOT = Path(__file__).parent / "packages"


def replace_body(language: str, body: str) -> None:
    path = ROOT / f"{language}.md"
    text = path.read_text(encoding="utf-8")
    start = text.index("## Article Body")
    end = text.index("## Image Plan")
    text = text[:start] + "## Article Body\n\n" + body.strip() + "\n\n" + text[end:]
    path.write_text(text, encoding="utf-8")


replace_body("English", r'''
# Blox Fruits AFK Guide: Leveling, Builds, and Trading

Blox Fruits asks players to repeat enemies for experience, money, and weapon mastery, but it has no built-in automatic mode. A farming loop works only when the target cannot interrupt the character, the selected fruit blocks that enemy's damage, and the reticle stays on the respawn point. This **Blox Fruits AFK Guide** explains the source setup, its level 14 Monkey sample, and the progression and trading choices that follow. The goal is a tested routine, not an unattended guess.

<!-- SOURCE_IMAGE:1 -->

## What Is Blox Fruits?

This Roblox action RPG supports melee, swords, guns, and fruit abilities across multiple islands. Fruits spawn every hour, disappear after 20 minutes, and enter the dealer's random stock every four hours. Fruit hunting therefore follows different timing from farming a fixed enemy.

## How to Set Up Stable AFK Combat

Equip the weapon or skill you want to train and aim at the enemy's respawn point. Enemies fight back and may push the character out of position.

<!-- SOURCE_IMAGE:2 -->

Set **Ability Control Scheme** to **Modern**.

<!-- SOURCE_IMAGE:3 -->

Disable camera shake, enable Fast Mode, and reduce effects to limit movement and device load.

<!-- SOURCE_IMAGE:4 -->

At the fruit shop, choose a fruit whose description grants immunity to the target. Test it against that exact mob before leaving.

<!-- SOURCE_IMAGE:5 -->

Consume the fruit and confirm its ability is active.

<!-- SOURCE_IMAGE:6 -->

Center the reticle on the spawn and place the clicker point over one skill. Watch several defeat-and-respawn cycles; reposition if knockback changes the angle.

<!-- SOURCE_IMAGE:7 -->

## Rewards and Progression After Farming

Kills grant experience and money, while the equipped weapon earns mastery.

<!-- SOURCE_IMAGE:8 -->

The UgPhone test against level 14 Monkeys recorded about **20,082 experience and 7,191 money in one hour**. It is a sample, not a guaranteed rate.

<!-- SOURCE_IMAGE:9 -->

The matching 24-hour projection is 481,968 experience and 172,584 money. Disconnects, movement, and missed attacks reduce real returns.

<!-- SOURCE_IMAGE:10 -->

Put level points into your main damage source and defense instead of every weapon category.

<!-- SOURCE_IMAGE:11 -->

Use earned money to buy equipment from merchants.

<!-- SOURCE_IMAGE:12 -->

New levels unlock tougher islands; retest immunity and positioning after moving.

<!-- SOURCE_IMAGE:13 -->

## How Does Blox Fruits Trading Work?

Before level 700, dropping a physical fruit for another player has no protected trade window. Do not drop anything you cannot lose.

<!-- SOURCE_IMAGE:14 -->

At level 700, the Café opens formal trading when both players sit opposite each other. Physical and permanent fruits, selected gamepasses, and scrolls are tradable; Beli, Fragments, swords, and guns are not.

<!-- SOURCE_IMAGE:15 -->

## How to Use UgPhone for Blox Fruits

Create a cloud device, install Roblox, enter the game, and apply the settings above. Choose a safe target, align the reticle, then test damage, respawn timing, mastery, and connection for several minutes. UgPhone keeps a permitted loop away from the physical phone's heat and battery use, but it cannot repair poor positioning or bypass game rules.

## Conclusion

Begin with one enemy and one skill, then observe several complete respawns. Test again whenever you change islands, fruits, weapons, or targets, because immunity and alignment may no longer hold. Treat the daily reward figure as an estimate and check progress after any connection issue. For a longer permitted session without occupying your phone, **download UgPhone and start a free trial**. Extend the run only when the short test remains stable and mastery continues to increase.
''')

replace_body("Portuguese", r'''
# Guia AFK de Blox Fruits: níveis, atributos e trocas

Blox Fruits exige repetir inimigos para ganhar experiência, dinheiro e domínio, mas não possui modo automático nativo. A rotina funciona somente quando o alvo não interrompe o personagem, a fruta bloqueia o dano daquele inimigo e a mira permanece no respawn. Este **Guia AFK de Blox Fruits** resume a configuração da fonte, o teste contra Monkeys de nível 14 e as decisões de evolução e troca posteriores. O objetivo é validar o ciclo antes de aumentar seu tempo.

<!-- SOURCE_IMAGE:1 -->

## O que é Blox Fruits?

Este RPG de ação do Roblox oferece corpo a corpo, espadas, armas e poderes de frutas em várias ilhas. Frutas surgem por hora, desaparecem após 20 minutos e entram no estoque aleatório do vendedor a cada quatro horas. Caçar frutas tem outro ritmo que farmar um inimigo fixo.

## Como configurar um AFK estável?

Equipe a arma ou habilidade desejada e mire no ponto de respawn. Inimigos revidam e podem empurrar o personagem.

<!-- SOURCE_IMAGE:2 -->

Altere **Ability Control Scheme** para **Modern**.

<!-- SOURCE_IMAGE:3 -->

Desative o balanço da câmera, ative o modo rápido e reduza efeitos para diminuir movimento e carga.

<!-- SOURCE_IMAGE:4 -->

Na loja, escolha uma fruta cuja descrição conceda imunidade contra o alvo. Teste no inimigo exato antes de sair.

<!-- SOURCE_IMAGE:5 -->

Consuma a fruta e confirme que a habilidade está ativa.

<!-- SOURCE_IMAGE:6 -->

Centralize a mira no respawn e ponha o clique repetido sobre uma habilidade. Observe vários ciclos e reposicione se o empurrão mudar o ângulo.

<!-- SOURCE_IMAGE:7 -->

## Quais são os ganhos e como evoluir?

Abates rendem experiência e dinheiro; a arma equipada recebe domínio.

<!-- SOURCE_IMAGE:8 -->

O teste no UgPhone contra Monkeys de nível 14 registrou cerca de **20.082 de experiência e 7.191 de dinheiro em uma hora**. É uma amostra, não garantia.

<!-- SOURCE_IMAGE:9 -->

A projeção para 24 horas é 481.968 de experiência e 172.584 de dinheiro. Quedas, movimento e ataques perdidos reduzem o total.

<!-- SOURCE_IMAGE:10 -->

Concentre pontos no dano principal e na defesa, em vez de dividir entre todas as armas.

<!-- SOURCE_IMAGE:11 -->

Use o dinheiro para comprar equipamentos com comerciantes.

<!-- SOURCE_IMAGE:12 -->

Novos níveis liberam ilhas mais difíceis; teste novamente imunidade e posição.

<!-- SOURCE_IMAGE:13 -->

## Como funcionam as trocas?

Antes do nível 700, soltar uma fruta física para outra pessoa não oferece proteção. Não entregue algo que não possa perder.

<!-- SOURCE_IMAGE:14 -->

No nível 700, o Café libera a troca formal quando os jogadores sentam em lados opostos. Frutas físicas e permanentes, alguns gamepasses e pergaminhos são aceitos; Beli, Fragmentos, espadas e armas não.

<!-- SOURCE_IMAGE:15 -->

## Como usar o UgPhone com Blox Fruits?

Crie um dispositivo em nuvem, instale Roblox e aplique os ajustes. Escolha um alvo seguro, alinhe a mira e teste dano, respawn, domínio e conexão por alguns minutos. O UgPhone evita aquecer e ocupar o celular físico, mas não corrige uma posição ruim nem ignora regras do jogo.

## Conclusão

Comece com um inimigo e uma habilidade, observando vários reaparecimentos completos. Teste novamente ao mudar de ilha, fruta, arma ou alvo, pois imunidade e alinhamento podem falhar. Considere o total diário uma estimativa e confira o progresso após problemas de conexão. Para manter uma sessão permitida sem ocupar seu celular, **baixe o UgPhone e solicite um teste gratuito**. Aumente o tempo somente quando o teste curto estiver estável e o domínio continuar subindo.
''')

replace_body("Spanish", r'''
# Guía AFK de Blox Fruits: niveles, atributos e intercambios

Blox Fruits exige repetir enemigos para obtener experiencia, dinero y dominio, pero no incluye un modo automático. La rutina funciona solo cuando el objetivo no interrumpe al personaje, la fruta bloquea el daño de ese enemigo y la retícula permanece sobre el respawn. Esta **Guía AFK de Blox Fruits** resume la configuración de la fuente, la prueba contra Monkeys de nivel 14 y las decisiones posteriores sobre progreso e intercambio. La clave es validar el ciclo antes de ampliar su duración.

<!-- SOURCE_IMAGE:1 -->

## ¿Qué es Blox Fruits?

Este RPG de acción de Roblox ofrece combate cuerpo a cuerpo, espadas, armas y poderes de frutas en distintas islas. Las frutas aparecen cada hora, desaparecen tras 20 minutos y entran al inventario aleatorio del vendedor cada cuatro horas. Cazar frutas tiene un ritmo distinto a farmear un enemigo fijo.

## ¿Cómo configurar un AFK estable?

Equipa el arma o habilidad que quieras entrenar y apunta al respawn. Los enemigos responden y pueden empujar al personaje.

<!-- SOURCE_IMAGE:2 -->

Cambia **Ability Control Scheme** a **Modern**.

<!-- SOURCE_IMAGE:3 -->

Desactiva el movimiento de cámara, activa el modo rápido y reduce efectos para limitar carga y variaciones visuales.

<!-- SOURCE_IMAGE:4 -->

En la tienda, elige una fruta cuya descripción conceda inmunidad ante el objetivo. Pruébala contra ese enemigo antes de dejar la sesión.

<!-- SOURCE_IMAGE:5 -->

Consume la fruta y confirma que su habilidad está activa.

<!-- SOURCE_IMAGE:6 -->

Centra la retícula en el respawn y coloca el clic repetido sobre una habilidad. Observa varios ciclos y corrige la posición si un empujón cambia el ángulo.

<!-- SOURCE_IMAGE:7 -->

## ¿Cuánto produce y cómo progresa el personaje?

Las derrotas entregan experiencia y dinero; el arma equipada gana dominio.

<!-- SOURCE_IMAGE:8 -->

La prueba en UgPhone contra Monkeys de nivel 14 registró cerca de **20.082 de experiencia y 7.191 de dinero en una hora**. Es una muestra, no una garantía.

<!-- SOURCE_IMAGE:9 -->

La proyección para 24 horas es 481.968 de experiencia y 172.584 de dinero. Desconexiones, movimiento y ataques fallidos reducen el total.

<!-- SOURCE_IMAGE:10 -->

Concentra puntos en el daño principal y la defensa, sin repartirlos entre todas las armas.

<!-- SOURCE_IMAGE:11 -->

Usa el dinero para comprar equipo a los comerciantes.

<!-- SOURCE_IMAGE:12 -->

Los niveles altos abren islas difíciles; vuelve a probar inmunidad y posición.

<!-- SOURCE_IMAGE:13 -->

## ¿Cómo funcionan los intercambios?

Antes del nivel 700, soltar una fruta física para otra persona no tiene protección. No entregues algo que no puedas perder.

<!-- SOURCE_IMAGE:14 -->

Al nivel 700, el Café activa el intercambio formal cuando ambos jugadores se sientan enfrente. Se aceptan frutas físicas y permanentes, ciertos pases y pergaminos; Beli, Fragmentos, espadas y armas no.

<!-- SOURCE_IMAGE:15 -->

## ¿Cómo usar UgPhone con Blox Fruits?

Crea un dispositivo en la nube, instala Roblox y aplica los ajustes. Elige un objetivo seguro, alinea la retícula y prueba daño, respawn, dominio y conexión durante varios minutos. UgPhone evita ocupar y calentar el teléfono físico, pero no corrige una posición inestable ni permite saltarse las reglas.

## Conclusión

Empieza con un enemigo y una habilidad, observando varias reapariciones completas. Repite la prueba al cambiar de isla, fruta, arma u objetivo, porque la inmunidad y la alineación pueden dejar de funcionar. Considera la cifra diaria una estimación y revisa el progreso después de cualquier problema de conexión. Para mantener una sesión permitida sin ocupar el teléfono, **descarga UgPhone y solicita una prueba gratuita**. Amplía el tiempo solo cuando la prueba breve siga estable y el dominio continúe aumentando.
''')

replace_body("Indonesian", r'''
# Panduan AFK Blox Fruits: level, build, dan perdagangan

Blox Fruits menuntut pemain mengalahkan musuh berulang kali demi pengalaman, uang, dan mastery, tetapi tidak menyediakan mode otomatis. Rutinitas hanya stabil jika target tidak menginterupsi karakter, buah menahan damage musuh tersebut, dan crosshair tetap di titik respawn. **Panduan AFK Blox Fruits** ini merangkum pengaturan sumber, uji Monkey level 14, serta keputusan progres dan perdagangan setelahnya. Tujuannya adalah menguji loop sebelum memperpanjang sesi.

<!-- SOURCE_IMAGE:1 -->

## Apa itu Blox Fruits?

RPG aksi Roblox ini memakai melee, pedang, pistol, dan kemampuan buah di berbagai pulau. Buah muncul tiap jam, hilang setelah 20 menit, dan masuk stok acak dealer setiap empat jam. Berburu buah berbeda ritmenya dari farming musuh tetap.

## Bagaimana menyiapkan AFK yang stabil?

Pasang senjata atau skill yang ingin dilatih dan bidik lokasi respawn. Musuh dapat melawan serta mendorong karakter.

<!-- SOURCE_IMAGE:2 -->

Ubah **Ability Control Scheme** menjadi **Modern**.

<!-- SOURCE_IMAGE:3 -->

Matikan guncangan kamera, aktifkan Fast Mode, dan kurangi efek untuk menekan gerakan visual serta beban perangkat.

<!-- SOURCE_IMAGE:4 -->

Di toko, pilih buah yang keterangannya memberi imun terhadap target. Uji pada musuh tersebut sebelum meninggalkan sesi.

<!-- SOURCE_IMAGE:5 -->

Makan buah dan pastikan kemampuannya aktif.

<!-- SOURCE_IMAGE:6 -->

Arahkan crosshair ke respawn dan tempatkan titik clicker di satu skill. Amati beberapa siklus; atur ulang jika dorongan mengubah sudut.

<!-- SOURCE_IMAGE:7 -->

## Berapa hasil farming dan bagaimana progresnya?

Musuh memberi pengalaman dan uang; senjata yang dipakai memperoleh mastery.

<!-- SOURCE_IMAGE:8 -->

Uji UgPhone melawan Monkey level 14 mencatat sekitar **20.082 pengalaman dan 7.191 uang dalam satu jam**. Ini sampel, bukan hasil pasti.

<!-- SOURCE_IMAGE:9 -->

Proyeksi 24 jam adalah 481.968 pengalaman dan 172.584 uang. Putus koneksi, pergeseran, dan serangan meleset mengurangi hasil.

<!-- SOURCE_IMAGE:10 -->

Fokuskan poin pada damage utama dan defense, bukan seluruh jenis senjata.

<!-- SOURCE_IMAGE:11 -->

Gunakan uang untuk membeli perlengkapan dari pedagang.

<!-- SOURCE_IMAGE:12 -->

Level tinggi membuka pulau sulit; uji ulang imun dan posisi setelah pindah.

<!-- SOURCE_IMAGE:13 -->

## Bagaimana perdagangan Blox Fruits bekerja?

Sebelum level 700, menjatuhkan buah fisik untuk orang lain tidak memiliki perlindungan transaksi. Jangan jatuhkan barang yang tidak siap hilang.

<!-- SOURCE_IMAGE:14 -->

Pada level 700, Café membuka perdagangan resmi saat dua pemain duduk berhadapan. Buah fisik dan permanen, gamepass tertentu, serta scroll bisa diperdagangkan; Beli, Fragment, pedang, dan pistol tidak.

<!-- SOURCE_IMAGE:15 -->

## Bagaimana memakai UgPhone untuk Blox Fruits?

Buat perangkat cloud, instal Roblox, lalu terapkan pengaturan tadi. Pilih target aman, sejajarkan crosshair, dan uji damage, respawn, mastery, serta koneksi selama beberapa menit. UgPhone mengurangi panas dan penggunaan baterai ponsel fisik, tetapi tidak memperbaiki posisi buruk atau melewati aturan game.

## Kesimpulan

Mulailah dengan satu musuh dan satu skill, lalu amati beberapa respawn lengkap. Uji kembali ketika mengganti pulau, buah, senjata, atau target karena imun dan bidikan mungkin tidak lagi sesuai. Anggap proyeksi harian sebagai perkiraan dan periksa progres setelah gangguan koneksi. Untuk menjalankan sesi yang diizinkan tanpa terus memakai ponsel, **unduh UgPhone dan mulai uji coba gratis**. Perpanjang waktu hanya apabila tes singkat tetap stabil dan mastery terus bertambah.
''')

replace_body("Vietnamese", r'''
# Hướng dẫn AFK Blox Fruits: lên cấp, chỉ số và giao dịch

Blox Fruits yêu cầu đánh lặp kẻ địch để nhận kinh nghiệm, tiền và độ thành thạo, nhưng không có chế độ tự động. Vòng đánh chỉ ổn định khi mục tiêu không làm gián đoạn nhân vật, trái chặn sát thương của nó và tâm ngắm vẫn ở điểm hồi sinh. **Hướng dẫn AFK Blox Fruits** này tóm tắt cài đặt nguồn, thử nghiệm với Monkey cấp 14 và các lựa chọn tiến trình, giao dịch sau đó. Hãy kiểm tra vòng đánh trước khi kéo dài phiên.

<!-- SOURCE_IMAGE:1 -->

## Blox Fruits là gì?

RPG hành động Roblox này có cận chiến, kiếm, súng và năng lực trái trên nhiều đảo. Trái xuất hiện mỗi giờ, biến mất sau 20 phút; đại lý đổi kho ngẫu nhiên sau bốn giờ. Săn trái khác với farm một mục tiêu cố định.

## Thiết lập AFK ổn định thế nào?

Trang bị vũ khí cần luyện và ngắm điểm hồi sinh. Kẻ địch có thể phản công, đẩy nhân vật lệch vị trí.

<!-- SOURCE_IMAGE:2 -->

Đổi **Ability Control Scheme** thành **Modern**.

<!-- SOURCE_IMAGE:3 -->

Tắt rung camera, bật Fast Mode và giảm hiệu ứng để giảm tải thiết bị.

<!-- SOURCE_IMAGE:4 -->

Chọn trái có mô tả miễn đòn của mục tiêu và thử với đúng kẻ địch.

<!-- SOURCE_IMAGE:5 -->

Ăn trái rồi xác nhận năng lực đã bật.

<!-- SOURCE_IMAGE:6 -->

Đặt tâm ngắm vào respawn, điểm chạm lặp trên kỹ năng. Theo dõi vài chu kỳ và chỉnh lại nếu lực đẩy làm đổi góc.

<!-- SOURCE_IMAGE:7 -->

## Thu nhập và tiến trình ra sao?

Kẻ địch cho kinh nghiệm, tiền; vũ khí đang cầm tăng độ thành thạo.

<!-- SOURCE_IMAGE:8 -->

Thử nghiệm UgPhone với Monkey cấp 14 ghi khoảng **20.082 kinh nghiệm và 7.191 tiền trong một giờ**. Đây là mẫu, không phải mức bảo đảm.

<!-- SOURCE_IMAGE:9 -->

Dự kiến 24 giờ là 481.968 kinh nghiệm và 172.584 tiền. Mất kết nối, lệch chỗ hoặc hụt đòn làm giảm kết quả.

<!-- SOURCE_IMAGE:10 -->

Dồn điểm vào nguồn sát thương chính và phòng thủ, không chia cho mọi loại vũ khí.

<!-- SOURCE_IMAGE:11 -->

Dùng tiền mua trang bị từ thương nhân.

<!-- SOURCE_IMAGE:12 -->

Cấp cao mở đảo khó hơn; hãy thử lại miễn sát thương và vị trí.

<!-- SOURCE_IMAGE:13 -->

## Giao dịch Blox Fruits thế nào?

Trước cấp 700, thả trái vật lý không có bảo vệ. Đừng thả món đồ bạn không thể mất.

<!-- SOURCE_IMAGE:14 -->

Ở cấp 700, Café mở giao dịch khi hai người ngồi đối diện. Trái vật lý, trái vĩnh viễn, một số gamepass và cuộn có thể đổi; Beli, Fragment, kiếm và súng thì không.

<!-- SOURCE_IMAGE:15 -->

## Dùng UgPhone cho Blox Fruits ra sao?

Tạo thiết bị đám mây, cài Roblox, chọn mục tiêu an toàn và thử sát thương, hồi sinh, độ thành thạo, kết nối trong vài phút. UgPhone giảm nhiệt và thời gian chiếm dụng điện thoại thật, nhưng không sửa vị trí kém ổn định hoặc bỏ qua luật game.

## Kết luận

Bắt đầu với một kẻ địch, một kỹ năng và vài lần hồi sinh trọn vẹn. Thử lại khi đổi đảo, trái, vũ khí hoặc mục tiêu vì góc ngắm có thể không còn phù hợp. Xem con số ngày là ước tính và kiểm tra sau lỗi mạng. Để chạy phiên được phép mà không chiếm điện thoại, **hãy tải UgPhone và bắt đầu dùng thử miễn phí**. Chỉ kéo dài khi thử nghiệm ngắn ổn định và độ thành thạo vẫn tăng.
''')

replace_body("Traditional-Chinese", r'''
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

replace_body("Thai", r'''
# คู่มือ AFK Blox Fruits: เก็บเลเวล ค่าสถานะ และเทรด

Blox Fruits ต้องตีศัตรูซ้ำเพื่อรับ EXP เงิน และความชำนาญ แต่ไม่มีโหมดอัตโนมัติ วงจรจะนิ่งเมื่อศัตรูผลักไม่ได้ ผลไม้กันดาเมจ และเป้ายังตรงจุดเกิด **คู่มือ AFK Blox Fruits** นี้สรุปค่าตั้ง ผลทดสอบ Monkey เลเวล 14 และข้อจำกัดการเทรด ควรดูหลายรอบก่อนเพิ่มเวลา

<!-- SOURCE_IMAGE:1 -->

## Blox Fruits คืออะไร?

เกม Roblox นี้ใช้หมัด ดาบ ปืน หรือผลไม้ ผลไม้เกิดทุกชั่วโมง หายใน 20 นาที ร้านสุ่มใหม่ทุก 4 ชั่วโมง

## ตั้งค่า AFK อย่างไร?

ใส่อาวุธ เล็งจุดเกิด และดูว่าศัตรูผลักตัวละครหรือไม่

<!-- SOURCE_IMAGE:2 -->

เปลี่ยน **Ability Control Scheme** เป็น **Modern**

<!-- SOURCE_IMAGE:3 -->

ปิดกล้องสั่น เปิดโหมดเร็ว และลดเอฟเฟกต์

<!-- SOURCE_IMAGE:4 -->

เลือกผลไม้ที่ระบุว่ากันการโจมตี แล้วทดสอบกับศัตรูจริง

<!-- SOURCE_IMAGE:5 -->

กินผลไม้และยืนยันว่าพลังทำงาน

<!-- SOURCE_IMAGE:6 -->

เล็งจุดเกิด วางจุดแตะบนสกิล ดูหลายรอบ และจัดใหม่หากมุมเปลี่ยน

<!-- SOURCE_IMAGE:7 -->

## รายได้และการเติบโต

ชนะแล้วได้ EXP เงิน และความชำนาญของอาวุธที่ถือ

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
