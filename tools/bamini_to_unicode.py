"""Convert legacy Bamini/Tharmini-font Tamil text in a PDF to proper Unicode Tamil.

The original proposal PDF was typed in the old "Tharmini" font, so copy/paste gives
gibberish like `gRikr; nraw;jpl;lk;`. This script reads the PDF and prints Unicode Tamil.

Usage:
    pip install pymupdf
    python tools/bamini_to_unicode.py proposal.pdf > proposal-unicode.txt

Always proofread the output; a few rare letters may need manual fixing.
"""
import sys, re, pymupdf

# Bamini/Tharmini legacy -> Unicode Tamil
MULTI = [
    ("J}", "தூ"), ("E}", "நூ"), ("Y}", "லூ"), ("W}", "றூ"), ("D}", "னூ"),
    ("G+", "பூ"), ("R+", "சூ"), ("T+", "வூ"), ("A+", "யூ"),
    ("hp", "ரி"), ("hP", "ரீ"), ("h;", "ர்"),
]
CONS = {"f":"க","q":"ங","r":"ச","Q":"ஞ","l":"ட","z":"ண","j":"த","e":"ந","g":"ப",
        "k":"ம","a":"ய","u":"ர","y":"ல","t":"வ","o":"ழ","s":"ள","w":"ற","d":"ன",
        "[":"ஜ","]":"ஸ","\\":"ஷ","^":"ஹ"}
SINGLE = {"m":"அ","M":"ஆ",",":"இ","<":"ஈ","c":"உ","C":"ஊ","v":"எ","V":"ஏ","I":"ஐ",
          "x":"ஒ","X":"ஓ","/":"ஃ",
          "F":"கு","$":"கூ","R":"சு","#":"சூ","L":"டு","_":"டூ","Z":"ணு","J":"து",
          "E":"நு","G":"பு","K":"மு","%":"மூ","A":"யு","U":"ரு","&":"ரூ","Y":"லு",
          "T":"வு","O":"ழு","*":"ழூ","S":"ளு","W":"று","D":"னு","B":"ஙு","b":"டி",
          "h":"ா","p":"ி","P":"ீ",";":"்","H":"ர்",">":",",
          }
SIGNS = {"n":"ெ","N":"ே","i":"ை"}
ALLCONS = set(CONS.values())

def conv(s):
    for a, b in MULTI:
        s = s.replace(a, "\x00" + b + "\x01")
    out = []
    parts = re.split(r"(\x00[^\x01]*\x01)", s)
    for part in parts:
        if part.startswith("\x00"):
            out.append(part[1:-1]); continue
        for ch in part:
            if ch in CONS: out.append(CONS[ch])
            elif ch in SINGLE: out.append(SINGLE[ch])
            elif ch in SIGNS: out.append("\x02" + SIGNS[ch])
            else: out.append(ch)
    t = "".join(out)
    # move prefix sign after the following consonant (+ optional sha/ssa cluster)
    t = re.sub(r"\x02(.)([க-ஹ])", lambda m: m.group(2) + m.group(1), t)
    t = t.replace("\x02", "")
    t = t.replace("ொ", "ொ").replace("ொ", "ொ").replace("ோ", "ோ")
    return t

doc = pymupdf.open(sys.argv[1])
for pno, page in enumerate(doc):
    print(f"\n===== PAGE {pno+1} =====")
    for b in page.get_text("dict")["blocks"]:
        for l in b.get("lines", []):
            line = ""
            for sp in l["spans"]:
                txt = sp["text"]
                line += conv(txt) if "Tharmini" in sp["font"] else txt
            if line.strip(): print(line)
