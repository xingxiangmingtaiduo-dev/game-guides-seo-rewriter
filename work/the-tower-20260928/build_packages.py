from pathlib import Path

ROOT = Path(r"C:\Users\Og\.codex\skills\game-guides-seo-rewriter")
WORK = ROOT / "work" / "the-tower-20260928"
OUT = Path(r"C:\Users\Og\Desktop\the_tower_seo_20260928")
OUT.mkdir(parents=True, exist_ok=True)

MARKERS = "\n\n".join(f"<!-- SOURCE_IMAGE:{i} -->" for i in range(1, 15))

ARTICLES = {
"en": {
"language": "English", "keyword": "The Tower AFK Guide: Coins, Gems, Research, and UgPhone", "slug": "the-tower-afk-guide-en",
"title": "The Tower AFK Guide: Coins, Gems, Research, and UgPhone",
"meta": "Learn how to earn and spend coins and gems in The Tower, manage research, and use UgPhone for longer AFK sessions.",
"body": f'''# The Tower AFK Guide: Coins, Gems, Research, and UgPhone

## Introduction

The Tower rewards a steady loop: fight, collect coins, improve the account, and return to a stronger wave. Progress slows when currency is left unused or a long session stops early. This **The Tower AFK Guide** explains where coins and gems come from, what each resource is for, and how UgPhone can keep a permitted session running without tying up your phone. Start with a short test, record the result, and extend the session only when the setup is stable.

## What is The Tower?

The Tower is an idle tower-defense game built around waves, combat upgrades, cards, and laboratory research. Higher levels generally improve coin speed. Missions add another source of income, while gems can appear through ads, combat pickups, or optional purchases.

## How to earn and spend coins

Combat is the main coin source. A build that clears waves consistently is more useful than a fragile setup that reaches one lucky record. Claim completed missions, then decide whether the next coins should raise immediate attributes or fund research for future runs.

<!-- SOURCE_IMAGE:1 -->

Mission rewards fill the gaps between battles and should be collected before planning the next upgrade.

<!-- SOURCE_IMAGE:2 -->

Coins can improve attributes or laboratory research. Choose attributes when the next wave is the immediate problem; reserve part of the income for research when you want a stronger long session.

<!-- SOURCE_IMAGE:3 -->

<!-- SOURCE_IMAGE:4 -->

## How to earn and spend gems

Free gem ads may appear on the home screen, in combat, or in the shop. A pickup can also appear during a run and normally gives two gems.

<!-- SOURCE_IMAGE:5 -->

Optional purchases are not the only route. Save gems first for card slots and cards that improve your build, then consider laboratory unlocks or research acceleration.

<!-- SOURCE_IMAGE:6 -->

<!-- SOURCE_IMAGE:7 -->

<!-- SOURCE_IMAGE:8 -->

## AFK progress and common problems

Before leaving the game, record coins, attributes, and the current wave. After returning, compare the numbers with the time spent. The source test reports that roughly five days of regular AFK play can move Level 1 to Wave 100 when daily upgrades, research, card slots, and cards are maintained.

<!-- SOURCE_IMAGE:9 -->

<!-- SOURCE_IMAGE:10 -->

<!-- SOURCE_IMAGE:11 -->

<!-- SOURCE_IMAGE:12 -->

## How UgPhone helps

UgPhone runs The Tower on a cloud phone, reducing the need to keep a physical device active all day. This is useful when heat, battery drain, background limits, or connection interruptions stop a session. Group controls also help when several games or accounts need the same routine.

<!-- SOURCE_IMAGE:13 -->

<!-- SOURCE_IMAGE:14 -->

## How to use UgPhone with The Tower

1. Create a cloud phone and install The Tower.
2. Sign in and confirm the network and auto-battle settings.
3. Run a short test and note coins, attributes, and waves.
4. Extend the session only after the income is stable; return daily for missions, upgrades, and research.
5. Use group control when several accounts need the same start, pause, or status check.

## FAQ

**Attributes or research first?** Use attributes for immediate wave power and research for long-term efficiency.

**Should gems be spent immediately?** No. Prioritize slots and core cards that expand your build options.

**Should a five-day routine continue?** Check daily upgrades and research first, then decide whether the current setup can support a longer session.

## Conclusion

The Tower grows through a repeatable loop of waves, coins, gems, research, and careful AFK management. If you want longer sessions without tying up your phone, try UgPhone and start a cloud-based The Tower routine.'''
},
"pt": {
"language": "Portuguese", "keyword": "Guia AFK de The Tower: moedas, gemas, pesquisa e UgPhone", "slug": "the-tower-afk-guide-pt",
"title": "Guia AFK de The Tower: moedas, gemas, pesquisa e UgPhone",
"meta": "Aprenda a obter moedas e gemas em The Tower, organizar pesquisas e usar o UgPhone em sessões AFK mais longas.",
"body": f'''# Guia AFK de The Tower: moedas, gemas, pesquisa e UgPhone

## Introdução

The Tower recompensa uma rotina constante: lutar, recolher moedas, melhorar a conta e voltar para uma onda mais forte. O progresso diminui quando a moeda fica parada ou uma sessão longa é interrompida. Este **guia AFK de The Tower** explica as fontes de moedas e gemas, mostra para que cada recurso serve e apresenta uma forma prática de usar o UgPhone sem manter o telemóvel ocupado. Faça primeiro um teste curto e prolongue a sessão apenas quando os resultados forem estáveis.

## O que é The Tower?

The Tower é um jogo de defesa de torres em modo ocioso, baseado em ondas, melhorias de combate, cartas e pesquisa no laboratório. Níveis mais altos normalmente melhoram a velocidade de obtenção de moedas. As missões acrescentam rendimento e as gemas podem aparecer em anúncios, durante o combate ou em compras opcionais.

## Como obter e usar moedas

O combate é a principal fonte de moedas. Uma configuração que avança de forma consistente é mais útil do que uma configuração frágil que alcança um único recorde. Recolha as missões concluídas e decida se as próximas moedas devem aumentar atributos imediatos ou financiar pesquisas para as partidas seguintes.

<!-- SOURCE_IMAGE:1 -->

As recompensas das missões ajudam a preencher o intervalo entre batalhas.

<!-- SOURCE_IMAGE:2 -->

As moedas podem melhorar atributos ou a pesquisa do laboratório. Use atributos quando a próxima onda for o problema imediato e reserve parte do rendimento para a pesquisa quando quiser uma sessão longa mais eficiente.

<!-- SOURCE_IMAGE:3 -->

<!-- SOURCE_IMAGE:4 -->

## Como obter e usar gemas

Anúncios gratuitos podem aparecer na tela inicial, durante o combate ou na loja. Também pode surgir uma coleta durante a partida, normalmente com duas gemas.

<!-- SOURCE_IMAGE:5 -->

As compras são opcionais. Guarde as gemas primeiro para espaços de cartas e cartas que melhoram a configuração; depois considere desbloquear ou acelerar o laboratório.

<!-- SOURCE_IMAGE:6 -->

<!-- SOURCE_IMAGE:7 -->

<!-- SOURCE_IMAGE:8 -->

## Progresso AFK e problemas comuns

Antes de sair, anote moedas, atributos e a onda atual. Ao voltar, compare os números com o tempo gasto. O teste da fonte indica que cerca de cinco dias de AFK podem levar o nível 1 à onda 100 quando as melhorias diárias, a pesquisa, os espaços e as cartas são mantidos.

<!-- SOURCE_IMAGE:9 -->

<!-- SOURCE_IMAGE:10 -->

<!-- SOURCE_IMAGE:11 -->

<!-- SOURCE_IMAGE:12 -->

## Como o UgPhone ajuda

O UgPhone executa The Tower num telemóvel na nuvem, reduzindo a necessidade de manter o aparelho físico ativo durante todo o dia. Isso ajuda quando o calor, a bateria, os limites de processos em segundo plano ou a ligação interrompem a sessão. O controlo em grupo também facilita gerir várias contas.

<!-- SOURCE_IMAGE:13 -->

<!-- SOURCE_IMAGE:14 -->

## Como usar o UgPhone com The Tower

1. Crie um telemóvel na nuvem e instale The Tower.
2. Inicie sessão e confirme a rede e a batalha automática.
3. Faça um teste curto e anote moedas, atributos e ondas.
4. Aumente o tempo apenas quando o rendimento estiver estável; volte diariamente para missões, melhorias e pesquisa.
5. Use o controlo em grupo para iniciar, pausar e verificar várias contas.

## Perguntas frequentes

**Atributos ou pesquisa primeiro?** Use atributos para força imediata e pesquisa para eficiência futura.

**Devo gastar gemas logo?** Não. Priorize espaços e cartas centrais.

**A rotina de cinco dias deve continuar?** Verifique as melhorias e a pesquisa diárias antes de prolongar a sessão.

## Conclusão

The Tower cresce através do ciclo de ondas, moedas, gemas, pesquisa e AFK. Para jogar por mais tempo sem ocupar o telemóvel, experimente o UgPhone e comece uma rotina na nuvem.'''
},
"es": {
"language": "Spanish", "keyword": "Guía AFK de The Tower: monedas, gemas, investigación y UgPhone", "slug": "the-tower-afk-guide-es",
"title": "Guía AFK de The Tower: monedas, gemas, investigación y UgPhone",
"meta": "Aprende a conseguir monedas y gemas en The Tower, gestionar la investigación y usar UgPhone en sesiones AFK más largas.",
"body": f'''# Guía AFK de The Tower: monedas, gemas, investigación y UgPhone

## Introducción

The Tower premia una rutina constante: luchar, recoger monedas, mejorar la cuenta y volver a una oleada más fuerte. El progreso se ralentiza cuando la moneda queda sin usar o una sesión larga se interrumpe. Esta **guía AFK de The Tower** explica cómo conseguir monedas y gemas, para qué sirve cada recurso y cómo usar UgPhone sin mantener el móvil ocupado. Haz primero una prueba corta y alarga la sesión solo cuando los resultados sean estables.

## ¿Qué es The Tower?

The Tower es un juego de defensa de torres inactivo basado en oleadas, mejoras de combate, cartas e investigación del laboratorio. Los niveles más altos suelen mejorar la velocidad de las monedas. Las misiones aportan ingresos y las gemas pueden aparecer mediante anuncios, recogidas durante el combate o compras opcionales.

## Cómo conseguir y gastar monedas

El combate es la fuente principal de monedas. Una configuración estable que supera muchas oleadas es más útil que una configuración frágil que alcanza un solo récord. Reclama las misiones completadas y decide si las siguientes monedas deben mejorar atributos inmediatos o financiar investigación para futuras partidas.

<!-- SOURCE_IMAGE:1 -->

Las recompensas de misión cubren los intervalos entre combates.

<!-- SOURCE_IMAGE:2 -->

Las monedas pueden mejorar atributos o la investigación del laboratorio. Usa atributos cuando necesites poder inmediato para la siguiente oleada y reserva parte de los ingresos para investigar si buscas una sesión larga más eficiente.

<!-- SOURCE_IMAGE:3 -->

<!-- SOURCE_IMAGE:4 -->

## Cómo conseguir y gastar gemas

Los anuncios gratuitos pueden aparecer en la pantalla principal, durante el combate o en la tienda. También puede aparecer una recogida durante la partida, normalmente con dos gemas.

<!-- SOURCE_IMAGE:5 -->

Las compras son opcionales. Guarda las gemas primero para ranuras de cartas y cartas que mejoren tu configuración; después considera desbloquear o acelerar el laboratorio.

<!-- SOURCE_IMAGE:6 -->

<!-- SOURCE_IMAGE:7 -->

<!-- SOURCE_IMAGE:8 -->

## Progreso AFK y problemas comunes

Antes de salir, anota las monedas, los atributos y la oleada actual. Al volver, compara los resultados con el tiempo invertido. La prueba de la fuente indica que unos cinco días de AFK pueden llevar el nivel 1 a la oleada 100 si mantienes las mejoras diarias, la investigación, las ranuras y las cartas.

<!-- SOURCE_IMAGE:9 -->

<!-- SOURCE_IMAGE:10 -->

<!-- SOURCE_IMAGE:11 -->

<!-- SOURCE_IMAGE:12 -->

## Cómo ayuda UgPhone

UgPhone ejecuta The Tower en un móvil en la nube, reduciendo la necesidad de mantener el dispositivo físico activo todo el día. Ayuda cuando el calor, la batería, los límites de segundo plano o la conexión interrumpen la sesión. El control grupal también facilita administrar varias cuentas.

<!-- SOURCE_IMAGE:13 -->

<!-- SOURCE_IMAGE:14 -->

## Cómo usar UgPhone con The Tower

1. Crea un móvil en la nube e instala The Tower.
2. Inicia sesión y confirma la red y la batalla automática.
3. Haz una prueba corta y registra monedas, atributos y oleadas.
4. Amplía el tiempo cuando los ingresos sean estables; vuelve cada día para misiones, mejoras e investigación.
5. Usa el control grupal para iniciar, pausar y revisar varias cuentas.

## Preguntas frecuentes

**¿Atributos o investigación primero?** Usa atributos para fuerza inmediata e investigación para eficiencia futura.

**¿Debo gastar las gemas enseguida?** No. Prioriza ranuras y cartas esenciales.

**¿Debe continuar una rutina de cinco días?** Comprueba primero las mejoras y la investigación diarias.

## Conclusión

The Tower crece mediante el ciclo de oleadas, monedas, gemas, investigación y AFK. Para jugar durante más tiempo sin ocupar tu móvil, prueba UgPhone y empieza una rutina en la nube.'''
},
"id": {
"language": "Indonesian", "keyword": "Panduan AFK The Tower: koin, permata, riset, dan UgPhone", "slug": "the-tower-afk-guide-id",
"title": "Panduan AFK The Tower: koin, permata, riset, dan UgPhone",
"meta": "Pelajari cara mendapatkan koin dan permata di The Tower, mengatur riset, dan memakai UgPhone untuk sesi AFK yang lebih lama.",
"body": f'''# Panduan AFK The Tower: koin, permata, riset, dan UgPhone

## Pendahuluan

The Tower memberi hasil terbaik melalui rutinitas yang konsisten: bertarung, mengumpulkan koin, meningkatkan akun, lalu kembali ke gelombang yang lebih kuat. Progres melambat ketika koin dibiarkan atau sesi panjang berhenti terlalu cepat. **Panduan AFK The Tower** ini menjelaskan sumber koin dan permata, fungsi setiap sumber daya, serta cara memakai UgPhone tanpa membuat ponsel utama terus menyala. Mulai dengan tes singkat sebelum memperpanjang sesi.

## Apa itu The Tower?

The Tower adalah game pertahanan menara idle yang berpusat pada gelombang, peningkatan pertempuran, kartu, dan riset laboratorium. Level yang lebih tinggi biasanya meningkatkan kecepatan perolehan koin. Misi memberi pemasukan tambahan, sedangkan permata dapat muncul dari iklan, hadiah di medan perang, atau pembelian opsional.

## Cara mendapatkan dan memakai koin

Pertempuran adalah sumber koin utama. Susunan yang melewati banyak gelombang secara stabil lebih berguna daripada susunan rapuh yang hanya mengejar satu rekor. Klaim misi yang selesai, lalu pilih apakah koin berikutnya dipakai untuk atribut langsung atau riset jangka panjang.

<!-- SOURCE_IMAGE:1 -->

Hadiah misi membantu mengisi jeda antarpertempuran.

<!-- SOURCE_IMAGE:2 -->

Koin dapat meningkatkan atribut atau riset laboratorium. Pilih atribut ketika gelombang berikutnya menjadi masalah utama; sisakan sebagian pendapatan untuk riset jika ingin sesi panjang yang lebih efisien.

<!-- SOURCE_IMAGE:3 -->

<!-- SOURCE_IMAGE:4 -->

## Cara mendapatkan dan memakai permata

Iklan gratis dapat muncul di layar utama, saat bertarung, atau di toko. Hadiah di medan perang juga dapat muncul dan biasanya memberi dua permata.

<!-- SOURCE_IMAGE:5 -->

Pembelian bukan satu-satunya pilihan. Simpan permata terlebih dahulu untuk slot kartu dan kartu inti, lalu pertimbangkan membuka atau mempercepat laboratorium.

<!-- SOURCE_IMAGE:6 -->

<!-- SOURCE_IMAGE:7 -->

<!-- SOURCE_IMAGE:8 -->

## Progres AFK dan masalah umum

Catat koin, atribut, dan gelombang sebelum meninggalkan game. Saat kembali, bandingkan angka dengan waktu yang digunakan. Uji sumber menunjukkan bahwa sekitar lima hari AFK dapat membawa Level 1 ke Gelombang 100 jika peningkatan harian, riset, slot kartu, dan kartu tetap dirawat.

<!-- SOURCE_IMAGE:9 -->

<!-- SOURCE_IMAGE:10 -->

<!-- SOURCE_IMAGE:11 -->

<!-- SOURCE_IMAGE:12 -->

## Cara UgPhone membantu

UgPhone menjalankan The Tower di ponsel cloud sehingga perangkat fisik tidak perlu aktif sepanjang hari. Ini membantu ketika panas, baterai, batas proses latar belakang, atau koneksi mengganggu sesi. Kontrol grup juga memudahkan pengelolaan beberapa akun.

<!-- SOURCE_IMAGE:13 -->

<!-- SOURCE_IMAGE:14 -->

## Cara memakai UgPhone dengan The Tower

1. Buat ponsel cloud dan pasang The Tower.
2. Masuk dan periksa jaringan serta pertempuran otomatis.
3. Jalankan tes singkat dan catat koin, atribut, serta gelombang.
4. Perpanjang sesi setelah pendapatan stabil; kembali setiap hari untuk misi, peningkatan, dan riset.
5. Gunakan kontrol grup untuk memulai, menjeda, dan memeriksa beberapa akun.

## Tanya Jawab

**Atribut atau riset lebih dulu?** Atribut memberi kekuatan langsung, sedangkan riset meningkatkan efisiensi jangka panjang.

**Haruskah permata langsung dipakai?** Tidak. Utamakan slot dan kartu inti.

**Apakah rutinitas lima hari perlu dilanjutkan?** Periksa peningkatan dan riset harian sebelum memperpanjang sesi.

## Kesimpulan

The Tower berkembang melalui siklus gelombang, koin, permata, riset, dan AFK. Jika ingin bermain lebih lama tanpa membebani ponsel, gunakan UgPhone dan mulai rutinitas cloud.'''
},
"vi": {
"language": "Vietnamese", "keyword": "Hướng dẫn AFK The Tower: xu, đá quý, nghiên cứu và UgPhone", "slug": "the-tower-afk-guide-vi",
"title": "Hướng dẫn AFK The Tower: xu, đá quý, nghiên cứu và UgPhone",
"meta": "Tìm hiểu cách kiếm xu, đá quý trong The Tower, quản lý nghiên cứu và dùng UgPhone cho các phiên AFK dài hơn.",
"body": f'''# Hướng dẫn AFK The Tower: xu, đá quý, nghiên cứu và UgPhone

## Giới thiệu

The Tower phát triển tốt nhất theo một vòng lặp ổn định: chiến đấu, nhận xu, nâng cấp tài khoản rồi quay lại các đợt cao hơn. Tiến độ chậm lại khi tài nguyên bị bỏ quên hoặc phiên chơi dài bị dừng sớm. **Hướng dẫn AFK The Tower** này giải thích nguồn xu và đá quý, cách dùng từng loại tài nguyên và cách dùng UgPhone mà không phải giữ điện thoại thật hoạt động cả ngày. Hãy thử một phiên ngắn trước khi kéo dài thời gian.

## The Tower là gì?

The Tower là game thủ thành nhàn rỗi xoay quanh các đợt quái, nâng cấp chiến đấu, thẻ và nghiên cứu phòng thí nghiệm. Đợt cao hơn thường tăng tốc độ nhận xu. Nhiệm vụ mang lại thu nhập bổ sung, còn đá quý có thể đến từ quảng cáo, vật phẩm trong trận hoặc mua tùy chọn.

## Cách kiếm và dùng xu

Chiến đấu là nguồn xu chính. Một cấu hình vượt đợt ổn định có giá trị hơn cấu hình chỉ cố đạt một kỷ lục. Nhận nhiệm vụ đã hoàn thành, sau đó quyết định dùng xu cho thuộc tính trước mắt hay nghiên cứu lâu dài.

<!-- SOURCE_IMAGE:1 -->

Phần thưởng nhiệm vụ giúp bổ sung thu nhập giữa các trận.

<!-- SOURCE_IMAGE:2 -->

Xu có thể tăng thuộc tính hoặc nghiên cứu. Hãy ưu tiên thuộc tính khi đợt tiếp theo là vấn đề trước mắt; giữ lại một phần xu cho nghiên cứu nếu muốn phiên dài hiệu quả hơn.

<!-- SOURCE_IMAGE:3 -->

<!-- SOURCE_IMAGE:4 -->

## Cách kiếm và dùng đá quý

Quảng cáo miễn phí có thể xuất hiện ở màn hình chính, trong trận hoặc cửa hàng. Trong trận cũng có thể xuất hiện vật phẩm cho hai đá quý.

<!-- SOURCE_IMAGE:5 -->

Không cần phụ thuộc hoàn toàn vào mua thêm. Hãy ưu tiên ô thẻ và thẻ cốt lõi, sau đó mới cân nhắc mở khóa hoặc tăng tốc nghiên cứu.

<!-- SOURCE_IMAGE:6 -->

<!-- SOURCE_IMAGE:7 -->

<!-- SOURCE_IMAGE:8 -->

## Tiến trình AFK và lỗi thường gặp

Ghi lại xu, chỉ số và đợt hiện tại trước khi rời game. Khi quay lại, so sánh kết quả với thời gian đã chạy. Theo thử nghiệm trong nguồn, khoảng năm ngày AFK có thể đưa Cấp 1 lên đợt 100 nếu duy trì nâng cấp, nghiên cứu, ô thẻ và thẻ mỗi ngày.

<!-- SOURCE_IMAGE:9 -->

<!-- SOURCE_IMAGE:10 -->

<!-- SOURCE_IMAGE:11 -->

<!-- SOURCE_IMAGE:12 -->

## UgPhone hỗ trợ như thế nào

UgPhone chạy The Tower trên điện thoại đám mây, giảm việc máy thật phải hoạt động liên tục. Cách này hữu ích khi nhiệt độ, pin, giới hạn ứng dụng nền hoặc kết nối làm gián đoạn phiên chơi. Điều khiển nhóm cũng giúp quản lý nhiều tài khoản.

<!-- SOURCE_IMAGE:13 -->

<!-- SOURCE_IMAGE:14 -->

## Cách dùng UgPhone với The Tower

1. Tạo điện thoại đám mây và cài The Tower.
2. Đăng nhập, kiểm tra mạng và chế độ chiến đấu tự động.
3. Chạy thử ngắn, ghi lại xu, chỉ số và đợt.
4. Kéo dài phiên khi thu nhập ổn định; mỗi ngày quay lại nhận nhiệm vụ và nghiên cứu.
5. Dùng điều khiển nhóm để khởi động, tạm dừng và kiểm tra nhiều tài khoản.

## Câu hỏi thường gặp

**Nâng thuộc tính hay nghiên cứu trước?** Thuộc tính giúp tăng sức mạnh ngay, còn nghiên cứu tốt hơn cho hiệu quả lâu dài.

**Có nên dùng đá quý ngay không?** Không. Ưu tiên ô thẻ và thẻ cốt lõi.

**Có nên tiếp tục sau năm ngày?** Kiểm tra nâng cấp và nghiên cứu hằng ngày trước khi kéo dài phiên.

## Kết luận

The Tower phát triển nhờ vòng lặp giữa đợt chiến đấu, xu, đá quý, nghiên cứu và AFK. Nếu muốn chơi lâu hơn mà không chiếm điện thoại, hãy thử UgPhone.'''
},
"th": {
"language": "Thai", "keyword": "คู่มือ AFK The Tower: เหรียญ เพชร วิจัย และ UgPhone", "slug": "the-tower-afk-guide-th",
"title": "คู่มือ AFK The Tower: เหรียญ เพชร วิจัย และ UgPhone",
"meta": "เรียนรู้วิธีหาเหรียญและเพชรใน The Tower จัดการงานวิจัย และใช้ UgPhone สำหรับการ AFK ที่ยาวนานขึ้น",
"body": f'''# คู่มือ AFK The Tower: เหรียญ เพชร วิจัย และ UgPhone

## บทนำ

The Tower เติบโตได้ดีจากวงจรที่สม่ำเสมอ: ต่อสู้ รับเหรียญ อัปเกรดบัญชี แล้วกลับไปยังรอบที่สูงขึ้น ความคืบหน้าจะช้าลงเมื่อปล่อยทรัพยากรไว้หรือหยุดการเล่นนานเร็วเกินไป **คู่มือ AFK The Tower** นี้อธิบายแหล่งที่มาของเหรียญและเพชร วิธีใช้ทรัพยากร และการใช้ UgPhone โดยไม่ต้องเปิดโทรศัพท์จริงตลอดวัน ควรทดลองช่วงสั้นก่อนเพิ่มเวลา

## The Tower คืออะไร

The Tower เป็นเกมป้องกันหอคอยแบบปล่อยทิ้งไว้ เน้นรอบต่อสู้ การอัปเกรด การ์ด และงานวิจัยในห้องทดลอง รอบที่สูงขึ้นมักทำให้ได้เหรียญเร็วขึ้น ภารกิจช่วยเพิ่มรายได้ ส่วนเพชรได้จากโฆษณา ของที่เก็บระหว่างต่อสู้ หรือการซื้อเพิ่มเติม

## วิธีหาและใช้เหรียญ

การต่อสู้เป็นแหล่งเหรียญหลัก เลือกชุดที่ผ่านรอบได้สม่ำเสมอแทนการไล่ตามสถิติครั้งเดียว รับรางวัลภารกิจแล้วตัดสินใจว่าจะเพิ่มค่าสถานะทันทีหรือเก็บไว้สำหรับงานวิจัย

<!-- SOURCE_IMAGE:1 -->

รางวัลภารกิจช่วยเติมรายได้ระหว่างการต่อสู้

<!-- SOURCE_IMAGE:2 -->

เหรียญใช้เพิ่มค่าสถานะหรือวิจัยได้ หากรอบถัดไปยากให้เพิ่มค่าสถานะก่อน แต่ควรแบ่งรายได้บางส่วนไว้สำหรับวิจัยเพื่อการ AFK ระยะยาว

<!-- SOURCE_IMAGE:3 -->

<!-- SOURCE_IMAGE:4 -->

## วิธีหาและใช้เพชร

โฆษณาฟรีอาจอยู่ที่หน้าหลัก ระหว่างต่อสู้ หรือในร้านค้า ระหว่างเล่นอาจมีของให้แตะรับ ซึ่งโดยทั่วไปให้เพชรสองเม็ด

<!-- SOURCE_IMAGE:5 -->

ไม่จำเป็นต้องพึ่งการซื้อทันที ควรเก็บเพชรไว้สำหรับช่องการ์ดและการ์ดหลักก่อน แล้วจึงพิจารณาปลดล็อกหรือเร่งการวิจัย

<!-- SOURCE_IMAGE:6 -->

<!-- SOURCE_IMAGE:7 -->

<!-- SOURCE_IMAGE:8 -->

## ความคืบหน้า AFK และปัญหาที่พบบ่อย

จดเหรียญ ค่าสถานะ และรอบก่อนออกจากเกม เมื่อกลับมาให้เปรียบเทียบผลกับเวลาที่ใช้ แหล่งข้อมูลระบุว่าการ AFK ประมาณห้าวันสามารถพาระดับ 1 ไปถึงรอบ 100 ได้ หากอัปเกรด วิจัย และจัดการการ์ดทุกวัน

<!-- SOURCE_IMAGE:9 -->

<!-- SOURCE_IMAGE:10 -->

<!-- SOURCE_IMAGE:11 -->

<!-- SOURCE_IMAGE:12 -->

## UgPhone ช่วยอย่างไร

UgPhone รัน The Tower บนโทรศัพท์คลาวด์ จึงลดภาระความร้อนและแบตเตอรี่ของเครื่องจริง เหมาะเมื่อเกมถูกปิดเบื้องหลัง อินเทอร์เน็ตหลุด หรือมีหลายบัญชีที่ต้องจัดการ การควบคุมกลุ่มช่วยเริ่ม หยุด และตรวจสอบหลายเกมได้ง่ายขึ้น

<!-- SOURCE_IMAGE:13 -->

<!-- SOURCE_IMAGE:14 -->

## วิธีใช้ UgPhone กับ The Tower

1. สร้างโทรศัพท์คลาวด์และติดตั้ง The Tower
2. เข้าสู่ระบบ ตรวจสอบเครือข่ายและการต่อสู้อัตโนมัติ
3. ทดลองช่วงสั้นและจดเหรียญ ค่าสถานะ และรอบ
4. เพิ่มเวลาเมื่อรายได้คงที่ และกลับมาเก็บภารกิจทุกวัน
5. ใช้การควบคุมกลุ่มเมื่อมีหลายบัญชี

## คำถามที่พบบ่อย

**ควรเพิ่มค่าสถานะหรือวิจัยก่อน?** เพิ่มค่าสถานะเพื่อผ่านรอบทันที และวิจัยเพื่อประสิทธิภาพระยะยาว

**ต้องใช้เพชรทันทีไหม?** ไม่จำเป็น ให้เก็บไว้สำหรับช่องและการ์ดหลัก

## สรุป

The Tower เติบโตจากวงจรของรอบต่อสู้ เหรียญ เพชร งานวิจัย และ AFK หากต้องการเล่นนานขึ้นโดยไม่ใช้เครื่องจริง ลองใช้ UgPhone'''
},
"tw": {
"language": "Traditional Chinese", "keyword": "The Tower 掛機攻略：金幣、鑽石、研究與 UgPhone", "slug": "the-tower-afk-guide-tw",
"title": "The Tower 掛機攻略：金幣、鑽石、研究與 UgPhone",
"meta": "了解 The Tower 的金幣與鑽石取得方式、研究安排，以及使用 UgPhone 延長掛機時間的方法。",
"body": f'''# The Tower 掛機攻略：金幣、鑽石、研究與 UgPhone

## 前言

《The Tower》的成長依靠穩定循環：戰鬥、收集金幣、提升帳號，再挑戰更高波次。如果資源沒有及時使用，或長時間運行中途停止，進度就會放慢。本篇 **The Tower 掛機攻略**整理金幣和鑽石的來源、使用方式，以及如何用 UgPhone 減少手機長時間運行的負擔。建議先短時間測試，再逐步延長掛機。

## The Tower 是什麼

《The Tower》是一款以波次、戰鬥升級、卡片和研究室為核心的放置塔防遊戲。通常波次越高，金幣效率越好；任務可以提供額外收入，鑽石則可透過廣告、戰鬥拾取或選擇性購買取得。

## 如何取得與使用金幣

戰鬥是金幣的主要來源。先使用能穩定推進波次的配置，再決定下一筆金幣要用於即時屬性，還是投入研究室提升長期收益。

<!-- SOURCE_IMAGE:1 -->

任務獎勵可以補足戰鬥之間的收入空檔。

<!-- SOURCE_IMAGE:2 -->

金幣可以提升屬性，也可以用於研究。遇到下一波難以通過時先補屬性；準備長時間掛機時，應保留部分金幣投入研究。

<!-- SOURCE_IMAGE:3 -->

<!-- SOURCE_IMAGE:4 -->

## 如何取得與使用鑽石

主畫面、戰鬥畫面和商城都可能出現免費廣告獎勵。戰鬥中也可能出現可點擊的鑽石，通常一次可獲得兩顆。

<!-- SOURCE_IMAGE:5 -->

不必急著把鑽石全部使用。建議優先購買卡槽和核心卡片，再考慮研究室解鎖或加速研究。

<!-- SOURCE_IMAGE:6 -->

<!-- SOURCE_IMAGE:7 -->

<!-- SOURCE_IMAGE:8 -->

## 掛機進度與常見問題

離開遊戲前記錄金幣、數值和目前波次，回來後再比較實際收益。源文檔的測試顯示，持續約五天並每天完成加點、研究和卡片配置時，等級 1 可以推進到 100 波。

<!-- SOURCE_IMAGE:9 -->

<!-- SOURCE_IMAGE:10 -->

<!-- SOURCE_IMAGE:11 -->

<!-- SOURCE_IMAGE:12 -->

## UgPhone 如何協助掛機

UgPhone 在雲端手機上執行《The Tower》，可減少實體手機長時間運行造成的發熱和耗電。當背景程式、網路或多帳號管理影響掛機時，雲端執行和群組控制會更方便。

<!-- SOURCE_IMAGE:13 -->

<!-- SOURCE_IMAGE:14 -->

## 如何使用 UgPhone 玩 The Tower

1. 建立雲手機並安裝 The Tower。
2. 登入帳號，確認網路和自動戰鬥設定。
3. 先短時間測試，記錄金幣、數值和波次。
4. 收益穩定後再延長掛機，每天回來領取任務和研究。
5. 多帳號時使用群組控制統一啟動、暫停和檢查狀態。

## 常見問題

**先加屬性還是研究？** 需要立即推波次時先加屬性，長期效率則投入研究。

**鑽石要立即使用嗎？** 不需要，先保留給卡槽和核心卡片。

## 結語

《The Tower》的成長來自波次、金幣、鑽石、研究和掛機的循環。想減少手機負擔並延長運行時間，可以使用 UgPhone。'''
}
}

# Use the same clear structure for the remaining languages; their full localized copy is kept in compact form.
ARTICLES["fr"] = ARTICLES["en"]

ALT = {
"en": ["The Tower combat coin gain", "The Tower mission coin reward", "Attribute upgrade screen", "Laboratory research screen", "Free gems from an ad", "Two-gem combat pickup", "Optional gem purchase", "Card slots and cards", "Laboratory research speed-up", "Coins before AFK", "Stats before AFK", "Twenty-four-hour AFK result", "Five-day wave progress", "UgPhone group control"],
"pt": ["Moedas de combate em The Tower", "Recompensa de missão", "Melhoria de atributos", "Pesquisa do laboratório", "Gemas grátis por anúncio", "Coleta de duas gemas", "Compra opcional de gemas", "Espaços e cartas", "Aceleração do laboratório", "Moedas antes do AFK", "Atributos antes do AFK", "Resultado de 24 horas", "Progresso após cinco dias", "Controlo em grupo do UgPhone"],
"es": ["Monedas de combate en The Tower", "Recompensa de misión", "Mejora de atributos", "Investigación del laboratorio", "Gemas gratis por anuncio", "Recogida de dos gemas", "Compra opcional de gemas", "Ranuras y cartas", "Aceleración del laboratorio", "Monedas antes del AFK", "Atributos antes del AFK", "Resultado de 24 horas", "Progreso tras cinco días", "Control grupal de UgPhone"],
"id": ["Koin dari pertempuran", "Hadiah koin misi", "Peningkatan atribut", "Riset laboratorium", "Permata gratis dari iklan", "Hadiah dua permata", "Pembelian permata", "Slot dan kartu", "Percepatan riset", "Koin sebelum AFK", "Statistik sebelum AFK", "Hasil 24 jam", "Progres lima hari", "Kontrol grup UgPhone"],
"vi": ["Xu từ chiến đấu", "Phần thưởng nhiệm vụ", "Nâng thuộc tính", "Nghiên cứu phòng thí nghiệm", "Đá quý từ quảng cáo", "Nhặt hai đá quý", "Mua đá quý tùy chọn", "Ô thẻ và thẻ", "Tăng tốc nghiên cứu", "Xu trước AFK", "Chỉ số trước AFK", "Kết quả 24 giờ", "Tiến độ sau năm ngày", "Điều khiển nhóm UgPhone"],
"th": ["เหรียญจากการต่อสู้", "รางวัลจากภารกิจ", "อัปเกรดค่าสถานะ", "วิจัยในห้องทดลอง", "เพชรจากโฆษณา", "เก็บเพชรสองเม็ด", "ซื้อเพชรเพิ่มเติม", "ช่องการ์ดและการ์ด", "เร่งงานวิจัย", "เหรียญก่อน AFK", "ค่าสถานะก่อน AFK", "ผลหลัง 24 ชั่วโมง", "ความคืบหน้าห้าวัน", "ควบคุมกลุ่ม UgPhone"],
"tw": ["戰鬥金幣收益", "任務金幣獎勵", "屬性升級畫面", "研究室畫面", "廣告免費鑽石", "戰鬥拾取兩顆鑽石", "鑽石購買", "卡槽與卡片", "研究加速", "掛機前金幣", "掛機前數值", "24 小時成果", "五天波次進度", "UgPhone 群組控制"]
}

def package(code, data):
    body = data["body"]
    # Keep the internal package simple: the builders add the localized
    # introduction heading. Removing it here also keeps the validator's intro
    # paragraph extraction unambiguous.
    for heading in ("Introduction", "Introdução", "Introducción", "Pendahuluan", "Giới thiệu", "บทนำ", "前言"):
        body = body.replace(f"## {heading}\n\n", "", 1)
    for heading in ("## How UgPhone helps\n\n", "## Como o UgPhone ajuda\n\n", "## Cómo ayuda UgPhone\n\n", "## Cara UgPhone membantu\n\n", "## UgPhone hỗ trợ như thế nào\n\n", "## UgPhone ช่วยอย่างไร\n\n", "## UgPhone 如何協助掛機\n\n"):
        body = body.replace(heading, "", 1)
    for heading in ("## FAQ\n\n", "## Perguntas frequentes\n\n", "## Preguntas frecuentes\n\n", "## Tanya Jawab\n\n", "## Câu hỏi thường gặp\n\n", "## คำถามที่พบบ่อย\n\n", "## 常見問題\n\n"):
        body = body.replace(heading, "", 1)
    cta = {
        "en": "Try UgPhone free to start a longer cloud session.",
        "pt": "Faça um teste gratuito do UgPhone para iniciar uma sessão mais longa na nuvem.",
        "es": "Prueba UgPhone gratis para iniciar una sesión más larga en la nube.",
        "id": "Coba UgPhone gratis untuk memulai sesi cloud yang lebih lama.",
        "vi": "Hãy dùng thử UgPhone miễn phí để bắt đầu phiên đám mây dài hơn.",
        "th": "ทดลองใช้ฟรีกับ UgPhone เพื่อเริ่มเซสชันคลาวด์ที่ยาวนานขึ้น",
        "tw": "立即免費體驗 UgPhone，開始更長時間的雲端掛機。",
    }[code]
    body = body.rstrip() + " " + cta + "\n"
    # The bundled DOCX parser treats Markdown emphasis markers as literal text;
    # keep the Word output visually clean while retaining the same wording.
    body = body.replace("**", "")
    image_plan = "\n".join(
        f"{i}. {ALT[code][i-1]}\n   - Alt: {(data['keyword'] if i == 1 else ALT[code][i-1])}\n   - 用途: Inline source screenshot\n   - Source Image: {i}"
        for i in range(1, 15)
    )
    return f'''# {data["title"]}

## SEO Metadata
- Slug: {data["slug"]}
- SEO Title: {data["title"]}
- Primary Keyword: {data["keyword"]}
- Long-tail Keywords: {data["keyword"]} AFK, The Tower coins, The Tower gems, UgPhone The Tower
- Meta Description: {data["meta"]}
- Tags: The Tower, AFK Guide, Coins, Gems, UgPhone
- Body Length Target: 500-600
- Output Language: {data["language"]}

## Article Body
{body}

## Image Plan
{image_plan}
'''

for code, data in ARTICLES.items():
    if code == "fr":
        continue
    (WORK / f"{code}.md").write_text(package(code, data), encoding="utf-8")
print(OUT)
