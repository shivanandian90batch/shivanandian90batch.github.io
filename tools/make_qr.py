"""Generate the 13 QR codes (main site + trees 1-12) and the A4 print sheet.

Usage (from repo root):
    pip install "qrcode[pil]"
    python tools/make_qr.py
    # then open qr/print-sheet.html in Chrome and Print -> Save as PDF -> qr/QR-plates-print.pdf

Only re-run if the website address changes. Existing printed QR codes keep working otherwise.
"""
import qrcode, qrcode.image.svg, base64, io
import os, sys
OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "qr")
BASE="https://shivanandian90batch.github.io/"
items=[("site",BASE,"இணையதளம்","முதன்மை")]+[(f"tree-{n:02d}",f"{BASE}?tree={n}",f"மரம் இல. {n:02d}",f"{n:02d}") for n in range(1,13)]
cards=[]
for name,url,label,_ in items:
    q=qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=40,border=4)
    q.add_data(url); q.make(fit=True)
    q.make_image(fill_color="black",back_color="white").save(f"{OUT}/qr-{name}.png")
    s=io.BytesIO(); q.make_image(image_factory=qrcode.image.svg.SvgPathImage).save(s)
    svg=s.getvalue().decode()
    cards.append(f'<div class="card"><div class="top">பசுமைச் செயற்திட்டம் 2026</div><div class="q">{svg[svg.find("<svg"):]}</div><div class="lab">{label}</div><div class="scan">📱 ஸ்கேன் செய்து மேலும் அறிக · Scan to learn more</div><div class="url">shivanandian90batch.github.io</div><div class="by">RKM Shivananda National School · 2006 O/L – 2009 A/L Batch</div></div>')
html=f'''<!doctype html><html><head><meta charset="utf-8"><style>
@page {{ size: A4; margin: 10mm; }}
body {{ margin:0; font-family:"Noto Sans Tamil","Noto Sans",sans-serif; }}
.grid {{ display:grid; grid-template-columns:1fr 1fr; gap:6mm; }}
.card {{ border:2.5mm solid #1f6b3a; border-radius:5mm; padding:4mm; text-align:center; break-inside:avoid; height:128mm; box-sizing:border-box; display:flex; flex-direction:column; align-items:center; }}
.top {{ background:#1f6b3a; color:#fff; font-weight:700; font-size:13pt; padding:1.5mm 4mm; border-radius:3mm; }}
.q svg {{ width:72mm; height:72mm; display:block; margin:3mm auto 1mm; }}
.lab {{ font-size:22pt; font-weight:800; color:#134526; line-height:1.2; }}
.scan {{ font-size:10.5pt; margin-top:1.5mm; }}
.url {{ font-size:10pt; font-family:"Noto Sans",sans-serif; font-weight:700; color:#1f6b3a; }}
.by {{ font-size:8pt; color:#555; margin-top:auto; }}
</style></head><body><div class="grid">{"".join(cards)}</div></body></html>'''
open(f"{OUT}/print-sheet.html","w").write(html)
