from pathlib import Path


ROOT = Path(__file__).parent / "packages"


def shift_markers(text: str) -> str:
    """Move existing semantic anchors 3-13 forward by one image slot."""
    text = text.replace("\n<!-- SOURCE_IMAGE:14 -->\n", "\n")
    for number in range(13, 2, -1):
        text = text.replace(
            f"<!-- SOURCE_IMAGE:{number} -->",
            f"<!-- SOURCE_IMAGE:{number + 1} -->",
        )
    return text


def update(name: str, old: str, new: str) -> None:
    path = ROOT / f"{name}.md"
    text = path.read_text(encoding="utf-8")
    if new in text:
        return
    text = shift_markers(text)
    if old not in text:
        raise ValueError(f"Expected insertion point missing in {path.name}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


update(
    "English",
    "<!-- SOURCE_IMAGE:2 -->\n\nFarther zones",
    "<!-- SOURCE_IMAGE:2 -->\n\nIf the owner catches you before the boundary, the theft fails.\n\n"
    "<!-- SOURCE_IMAGE:3 -->\n\nFarther zones",
)

path = ROOT / "English.md"
text = path.read_text(encoding="utf-8")
text = text.replace(
    "Build speed before chasing distant egg pools, and use each zone marker as a checkpoint rather than a promise of success.",
    "Build speed, and use each zone marker as a checkpoint.",
)
path.write_text(text, encoding="utf-8")

update(
    "Indonesian",
    "<!-- SOURCE_IMAGE:2 -->\n\nZona yang lebih jauh",
    "<!-- SOURCE_IMAGE:2 -->\n\nJika pemilik menangkapmu sebelum batas aman, pencurian gagal.\n\n"
    "<!-- SOURCE_IMAGE:3 -->\n\nZona yang lebih jauh",
)

update(
    "Portuguese",
    "Pegue o ovo, vire para a base e mantenha a câmera alinhada com o retorno. Se o dono alcançar você, o roubo falha.\n\n<!-- SOURCE_IMAGE:2 -->",
    "Pegue o ovo, vire para a base e mantenha a câmera alinhada com o retorno.\n\n"
    "<!-- SOURCE_IMAGE:2 -->\n\nSe o dono alcançar você, o roubo falha.\n\n"
    "<!-- SOURCE_IMAGE:3 -->",
)

update(
    "Spanish",
    "Toma el huevo, gira hacia la base y mantén la cámara alineada con el regreso. Si el dueño te alcanza, el robo falla.\n\n<!-- SOURCE_IMAGE:2 -->",
    "Toma el huevo, gira hacia la base y mantén la cámara alineada con el regreso.\n\n"
    "<!-- SOURCE_IMAGE:2 -->\n\nSi el dueño te alcanza, el robo falla.\n\n"
    "<!-- SOURCE_IMAGE:3 -->",
)

update(
    "Traditional-Chinese",
    "蛋由NPC持有，玩家會爭搶。拿蛋後對準安全區；被追上就失敗。\n\n<!-- SOURCE_IMAGE:2 -->",
    "蛋由NPC持有，玩家會爭搶。拿蛋後對準安全區。\n\n"
    "<!-- SOURCE_IMAGE:2 -->\n\n被追上就失敗。\n\n"
    "<!-- SOURCE_IMAGE:3 -->",
)

update(
    "Vietnamese",
    "Nhặt trứng, quay về căn cứ và giữ camera hướng theo đường chạy. Bị chủ trứng đuổi kịp đồng nghĩa thất bại.\n\n<!-- SOURCE_IMAGE:2 -->",
    "Nhặt trứng, quay về căn cứ và giữ camera hướng theo đường chạy.\n\n"
    "<!-- SOURCE_IMAGE:2 -->\n\nBị chủ trứng đuổi kịp đồng nghĩa thất bại.\n\n"
    "<!-- SOURCE_IMAGE:3 -->",
)

# Thai was deliberately compacted for a character-count target, so align its
# first six anchors explicitly and keep the same concise editorial style.
path = ROOT / "Thai.md"
text = path.read_text(encoding="utf-8")
old = """ไข่เป็นของ NPC

<!-- SOURCE_IMAGE:2 -->

หยิบแล้วกลับฐาน

<!-- SOURCE_IMAGE:3 -->

ถูกจับจะล้มเหลว

<!-- SOURCE_IMAGE:4 -->

โซนไกลดีกว่า

## วางแผนกลางวันอย่างไร?

กลางวันขโมย กลางคืนรีเซ็ต

<!-- SOURCE_IMAGE:5 -->"""
new = """ไข่เป็นของ NPC หยิบแล้วกลับฐาน

<!-- SOURCE_IMAGE:2 -->

ถูกจับจะล้มเหลว

<!-- SOURCE_IMAGE:3 -->

โซนไกลดีกว่า

<!-- SOURCE_IMAGE:4 -->

ป้ายบอกความเร็วแนะนำ

<!-- SOURCE_IMAGE:5 -->

## วางแผนกลางวันอย่างไร?

กลางวันขโมย กลางคืนรีเซ็ต

<!-- SOURCE_IMAGE:6 -->"""
if new not in text:
    text = text.replace("\n<!-- SOURCE_IMAGE:14 -->\n", "\n")
    for number in range(13, 5, -1):
        text = text.replace(
            f"<!-- SOURCE_IMAGE:{number} -->",
            f"<!-- SOURCE_IMAGE:{number + 1} -->",
        )
    if old not in text:
        raise ValueError("Expected Thai insertion block missing")
    text = text.replace(old, new, 1)
text = text.replace("ขโมยไข่แล้วต้องหนีกลับก่อนถูกจับ ความเร็วจึงสำคัญ ", "ขโมยไข่แล้วต้องหนีกลับ ความเร็วจึงสำคัญ ")
text = text.replace("เพิ่มเวลาเมื่อเสถียร", "เพิ่มเวลาเมื่อพร้อม")
text = text.replace("ความเร็วจึงสำคัญ ไข่ฟัก", "ความเร็วจึงสำคัญมาก ไข่ฟัก")
text = text.replace("เพิ่มความเร็วก่อนโซนไกล", "เพิ่มเร็วก่อนโซนไกล")
text = text.replace("ขายหรือรวมตัว ก่อน AFK", "ขายหรือรวม ก่อน AFK")
text = text.replace("เริ่มทดลองใช้ฟรี", "ทดลองใช้ฟรี")
path.write_text(text, encoding="utf-8")
