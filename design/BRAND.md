# amiKey brand guideline

One small set of rules, used the same way in the app, the installer, the README and anything we publish.
Code that implements it: `Windows/App/Settings.cpp` (colors, `drawWordmark`), `Tools/icons/make_windows_icons.py` (icons).

## Name and tagline
- **amiKey**: lowercase "ami", capital K, one word. Never "AmiKey", "AMIKEY" or "ami Key".
- Tagline: **amiKey - Gõ tiếng Việt** (release titles, the installer, the app's display name where it fits).
- In running text the name is plain text in the surrounding font and color: "amiKey tự chuyển…".

## Wordmark
- The **ami logo** (`design/ami-logo.jpg`: blue "ami" with the red dot, without the "Always keeping trust" line and
  the ®), followed by **"Key" in orange** `#F89800`, Segoe UI bold. The logo's letters are as tall as the capitals of "Key".
  The app uses `Windows/App/Resources/ami-wordmark.png`, made by `Tools/icons/make_windows_icons.py`.
- Use it wherever the name stands alone as a logo: app window headers, About.
- Usually next to the icon, gap ≈ 0.3 × the text height.

| | Color |
|---|---|
| "ami" (logo blue) | `#0466B1` |
| the dot (logo red) | `#E91E26` |
| "Key" (orange) | `#F89800` |

## Colors
- **Brand indigo** `#4F46E5` (dark mode `#8C87FF`), hover/pressed `#4338CA`. The only accent color: buttons, links, the wordmark, highlights.
- Ink `#111318`, muted text `#5B6472`, lines `#E6EAF0`, chip/tint background `#EEF0FF` (or brand at 14% on any background).
- Status only: green for "done/added", red `#D14343` for "wrong".
- **No pink, no second accent, no gradients on text.**

## Typography
- The system font: Segoe UI on Windows. Monospace: Cascadia Mono / Consolas.
- Headlines bold; body regular. Short lines, no orphans, no split phrases.

## Icon
- `design/amiKey-logo.jpg`: the "VE" monogram in a square frame. The app icon (`Windows/App/amiKey.ico`) is this
  logo cropped to its frame and recolored to ami blue. Don't recolor it or put it on a busy background.
- Tray: `Windows/App/Icons/tray-{V,E}-{black,white}.ico`, a square frame with a slanted V (Vietnamese) or E (English),
  black on a light taskbar and white on a dark one. Rebuild all icons with `python Tools/icons/make_windows_icons.py`.

## Voice
- Vietnamese first, English second.
- Short, concrete, no hype: say what happens ("gõ "treen" ra "trên""), not adjectives.
