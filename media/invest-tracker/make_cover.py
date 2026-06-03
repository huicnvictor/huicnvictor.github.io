from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

W, H = 1600, 1000
BG = (17, 17, 19)
SURFACE = (24, 24, 27)
SURFACE2 = (31, 31, 35)
BORDER = (39, 39, 42)
ACCENT = (59, 130, 246)
TEXT = (250, 250, 250)
TEXT2 = (161, 161, 170)
TEXT3 = (113, 113, 122)


def font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except Exception:
        return ImageFont.load_default()


INTER_B = "C:/Windows/Fonts/arialbd.ttf"
INTER_R = "C:/Windows/Fonts/arial.ttf"
MONO = "C:/Windows/Fonts/consola.ttf"

f_logo = font(INTER_B, 32)
f_nav = font(INTER_R, 26)
f_eyebrow = font(INTER_B, 22)
f_h1 = font(INTER_B, 96)
f_lede = font(INTER_R, 28)
f_card_title = font(INTER_B, 30)
f_card_sym = font(MONO, 22)
f_card_value = font(MONO, 72)
f_th_label = font(INTER_B, 18)
f_th_val = font(MONO, 28)
f_status = font(INTER_B, 22)

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img, "RGBA")

# Header logo
hx, hy = 100, 70
d.ellipse([hx, hy, hx + 26, hy + 26], fill=ACCENT)
d.text((hx + 42, hy - 5), "Invest Tracker", font=f_logo, fill=TEXT)

# Nav
nx, ny = W - 540, hy - 5
labels = ["FIRE", "Alerts", "Library"]
for i, label in enumerate(labels):
    if label == "Alerts":
        d.rounded_rectangle([nx - 14, ny - 8, nx + 100, ny + 38], radius=8, fill=(59, 130, 246, 50))
        d.text((nx, ny), label, font=f_nav, fill=ACCENT)
    else:
        d.text((nx, ny), label, font=f_nav, fill=TEXT2)
    nx += 170

# Divider
d.line([(100, hy + 70), (W - 100, hy + 70)], fill=BORDER, width=1)

# Eyebrow pill
ex, ey = 100, 210
d.rounded_rectangle([ex, ey, ex + 96, ey + 42], radius=8, fill=(59, 130, 246, 50))
d.text((ex + 22, ey + 9), "LIVE", font=f_eyebrow, fill=ACCENT)

# H1
d.text((100, ey + 64), "Price alerts", font=f_h1, fill=TEXT)

# Lede
d.text((100, ey + 200), "Scheduled checks four times per weekday. When a price crosses", font=f_lede, fill=TEXT2)
d.text((100, ey + 240), "your threshold, an email lands in your inbox.", font=f_lede, fill=TEXT2)

# Ticker card
cx, cy, cw, ch = 100, 600, W - 200, 320
d.rounded_rectangle([cx, cy, cx + cw, cy + ch], radius=14, fill=SURFACE, outline=BORDER, width=1)

ix = cx + 50
iy = cy + 40

d.text((ix, iy), "iShares NASDAQ 100 UCITS ETF", font=f_card_title, fill=TEXT)
d.text((ix + 540, iy + 11), "SXRV.DE  ·  EUR", font=f_card_sym, fill=TEXT3)

d.text((ix, iy + 56), "€892.45", font=f_card_value, fill=TEXT)

th_y = iy + 168
d.text((ix, th_y), "LOW", font=f_th_label, fill=TEXT3)
d.text((ix + 70, th_y - 4), "€820.00", font=f_th_val, fill=TEXT)

d.text((ix + 280, th_y), "HIGH", font=f_th_label, fill=TEXT3)
d.text((ix + 360, th_y - 4), "€950.00", font=f_th_val, fill=TEXT)

# Status badge right side
sx = cx + cw - 270
sy = cy + ch // 2 - 30
d.rounded_rectangle([sx, sy, sx + 220, sy + 60], radius=8, fill=SURFACE2, outline=BORDER, width=1)
# center text in badge
bbox = d.textbbox((0, 0), "IN RANGE", font=f_status)
tw = bbox[2] - bbox[0]
d.text((sx + (220 - tw) // 2, sy + 18), "IN RANGE", font=f_status, fill=TEXT2)

out = Path(__file__).resolve().parent / "cover.png"
img.save(out, "PNG")
print(f"saved: {out}")
