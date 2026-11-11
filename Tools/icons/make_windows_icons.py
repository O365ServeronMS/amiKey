"""Builds the Windows icons from design/amiKey-logo.jpg.

  amiKey.ico            app icon: the framed VE logo, 16-256 px
  Icons/tray-{V,E}-{black,white}.ico   tray glyphs in the logo's style (square frame + slanted letter);
                        black for a light taskbar, white for a dark one. Each size is drawn natively.

usage: python Tools/icons/make_windows_icons.py
"""
import os
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.join(os.path.dirname(__file__), "..", "..")
APP = os.path.join(ROOT, "Windows", "App")
LOGO = os.path.join(ROOT, "design", "amiKey-logo.jpg")
FONT = r"C:\Windows\Fonts\seguibli.ttf"   # Segoe UI Black Italic

# app icon: crop to the frame (it is the icon's edge), drop the background around it
logo = Image.open(LOGO).convert("RGB")
box = (200, 203, 824, 809)   # the frame's outer edges (~624 x 606, squared on resize)
app = logo.crop(box).resize((256, 256), Image.LANCZOS)
app.save(os.path.join(APP, "amiKey.ico"), sizes=[(s, s) for s in (16, 20, 24, 32, 40, 48, 64, 96, 128, 256)])

def glyph(letter, size, rgb):
    k = 8; S = size * k
    im = Image.new("RGBA", (S, S), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    w = max(1, round(size / 16)) * k                      # frame: 1 px at 16, 2 px at 32
    d.rectangle([0, 0, S - 1, S - 1], outline=rgb + (255,), width=w)
    f = ImageFont.truetype(FONT, int(S * 0.86))
    l, t, r, b = d.textbbox((0, 0), letter, font=f)
    d.text(((S - (r - l)) / 2 - l, (S - (b - t)) / 2 - t), letter, font=f, fill=rgb + (255,))
    return im.resize((size, size), Image.LANCZOS)

for letter in "VE":
    for name, rgb in (("black", (0, 0, 0)), ("white", (255, 255, 255))):
        imgs = [glyph(letter, s, rgb) for s in (16, 20, 24, 32, 40, 48, 64)]
        imgs[-1].save(os.path.join(APP, "Icons", f"tray-{letter}-{name}.ico"), sizes=[i.size for i in imgs], append_images=imgs[:-1])
print("ok")
