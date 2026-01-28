import sys
from PIL import Image

PIXEL_SIZE = 10 # длина шага за 1 пикс
THRESHOLD = 128 # порог яркости

def png_to_kumir(png_path, out_path):
    img = Image.open(png_path).convert("L")
    w, h = img.size
    px = img.load()

    out = []
    out.append("использовать Черепаха;")
    out.append("алг")
    out.append("нач")
    out.append("поднять хвост")
    out.append("вправо (0)")

    for y in range(h):
        for x in range(w):
            if px[x, y] < THRESHOLD:
                out.append("опустить хвост")
            else:
                out.append("поднять хвост")

            out.append(f"вперед ({PIXEL_SIZE})")

        out.append("поднять хвост")
        out.append("влево (180)")
        out.append(f"вперед ({w * PIXEL_SIZE})")
        out.append("влево (180)")

        out.append("вправо (90)")
        out.append(f"вперед ({PIXEL_SIZE})")
        out.append("влево (90)")

    out.append("кон")

    with open(out_path, "w", encoding="utf-8-sig") as f:
        f.write("\n".join(out))


def main():
    if len(sys.argv) < 2:
        print("Использование:")
        print("  python png2kumir.py input.png [output.kum]")
        return

    input_png = sys.argv[1]

    if len(sys.argv) >= 3:
        output_kum = sys.argv[2]
    else:
        output_kum = input_png.rsplit(".", 1)[0] + ".kum"

    png_to_kumir(input_png, output_kum)
    print("Готово:", output_kum)


if __name__ == "__main__":
    main()
