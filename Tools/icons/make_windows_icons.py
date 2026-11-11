"""Builds the Windows icons and the wordmark image from the logos in design/.

  amiKey.ico                          app icon: the framed VE logo recolored to ami blue, 16-256 px
  Icons/tray-{V,E}-{light,dark}.ico   tray glyphs in the logo's style (square frame + slanted letter) in ami blue,
                                      for a light / a dark taskbar (a lighter blue there). Each size is drawn natively.
  Resources/ami-wordmark.png          the "ami" of design/ami-logo.jpg (no tagline, no (R)) on transparency;
                                      the app draws it followed by "Key" in orange.

usage: python Tools/icons/make_windows_icons.py
"""
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageOps

ROOT = os.path.join(os.path.dirname(__file__), "..", "..")
APP = os.path.join(ROOT, "Windows", "App")
FONT = r"C:\Windows\Fonts\seguibli.ttf"   # Segoe UI Black Italic
AMI_BLUE = (4, 102, 177)                  # sampled from design/ami-logo.jpg

# app icon: the VE logo cropped to its frame, its greys mapped onto ami blue
logo = Image.open(os.path.join(ROOT, "design", "amiKey-logo.jpg")).convert("RGB")
box = (200, 203, 824, 809)   # the frame's outer edges (~624 x 606, squared on resize)
gray = ImageOps.grayscale(logo.crop(box).resize((256, 256), Image.LANCZOS))
app = ImageOps.colorize(gray, black=(0, 38, 84), mid=AMI_BLUE, white=(255, 255, 255), midpoint=110)
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

os.makedirs(os.path.join(APP, "Icons"), exist_ok=True)
for letter in "VE":
    for name, rgb in (("light", AMI_BLUE), ("dark", (90, 174, 240))):
        imgs = [glyph(letter, s, rgb) for s in (16, 20, 24, 32, 40, 48, 64)]
        imgs[-1].save(os.path.join(APP, "Icons", f"tray-{letter}-{name}.ico"), sizes=[i.size for i in imgs], append_images=imgs[:-1])

# wordmark: "ami" (letters + red dot) without the tagline below and the (R) to the right; white background -> alpha
ami = np.array(Image.open(os.path.join(ROOT, "design", "ami-logo.jpg")).convert("RGB").crop((36, 24, 304, 166))).astype(float)
bg = 248.0
alpha = np.clip((bg - ami.min(axis=2) - 6) / 150.0, 0, 1)
rgb = np.where(alpha[..., None] > 0, (ami - (1 - alpha[..., None]) * bg) / np.maximum(alpha[..., None], 1e-3), 0)
out = np.dstack([np.clip(rgb, 0, 255), alpha * 255]).astype(np.uint8)
im = Image.fromarray(out, "RGBA"); im = im.crop(im.getbbox())
im.save(os.path.join(APP, "Resources", "ami-wordmark.png"))
print("ok", im.size)
