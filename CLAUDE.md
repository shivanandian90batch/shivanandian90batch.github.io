# CLAUDE.md: AI maintainer guide

Instructions and project memory for AI assistants (Claude Code, Copilot, ChatGPT, etc.) maintaining this site.
Humans: see [README.md](README.md). `AGENTS.md` points here.

## Who you're helping

Batch members of the **2006 O/L / 2009 A/L "90 Batch"** of **RKM Shivananda National School (இராமகிருஷ்ண மிஷன்
சிவானந்த தேசிய பாடசாலை), Kalladi, Uppodai, Batticaloa, Sri Lanka**. Most are **not technical**. They will
ask in plain English or Tamil ("tree 3 planted today by Ravi", "add this photo"). Do the git work for them,
explain results simply, and don't make them read diffs.

## The project

- **Green Project 2026 (பசுமைச் செயற்திட்டம் 2026):** planting **12 Thirukkonrai (திருக்கொன்றை, *Cassia fistula*,
  Golden Shower)** shade trees along the boundary wall footpath on **Vipulananthar Road (விபுலானந்தர் வீதி)**,
  beside the **Vivekananthar building block**, to shade students/public from heat and dust.
- Planting: **mid-Kārthikai (mid-November) 2026**. Tree guards (light-permeable mesh "நாற்றுப் பேணல் கூடங்கள்")
  protect the saplings. Volunteers weed and fertilise monthly and water continuously until the trees are established.
- Budget: **Rs. 50,000** (guards 3,250 × 12 = 39,000; fertiliser 500 × 4 = 2,000; watering tools 2,000 × 2 = 4,000;
  transport/misc 5,000). Saplings and the guards' labour were donated by batch members (donors chose to stay unnamed).
- Motto: **"Friends Forever · One Family · Proud as a Shivanandian"** ("நண்பர்கள் எப்போதும் – ஒரே குடும்பம்").
- `proposal.pdf` is the original proposal (Word → PDF, 8 pages, Tamil).

## Site architecture

- **Single static page:** `index.html`, served by **GitHub Pages** from `main` / root.
  Live at **https://shivanandian90batch.github.io** (repo `shivanandian90batch/shivanandian90batch.github.io`).
  Push to `main` → live in ~1 minute. No build step, no framework, no dependencies except the Google Font *Noto Sans Tamil*.
- `.nojekyll` disables Jekyll processing. Keep it.
- **All routine content lives in the `EASY-UPDATE SECTION` `<script>` at the bottom of `index.html`:**
  - `CONTACT` {name, phone, email}: phone also builds `tel:` and `wa.me` (WhatsApp) buttons.
  - `TREES` [{no, date, by, status}] × 12: renders the "எமது 12 மரங்கள்" table.
  - `UPDATES` [{date, text, image?}], **newest first**: renders the "புதிய செய்திகள்" news section.
  Prefer editing these lists over editing HTML. Values are HTML-escaped by `esc()`, so plain text only.
- **Per-tree QR mechanism:** each tree's QR encodes `https://shivanandian90batch.github.io/?tree=N` (N = 1–12).
  JS reads `?tree=` and shows the yellow `#treeBanner` ("நீங்கள் நிற்பது: மரம் இல. NN") with that tree's data,
  and adds class `here` to that table row. **Never change the URL scheme or domain**: the QR codes are
  printed on physical plates and cannot be updated. If something must move, keep the old URL working.
- Design tokens are CSS variables in `:root` (green `#1f6b3a`, gold `#f2b705`). The site is designed for phones first:
  check at ~400 px width. All Tamil must be **Unicode Tamil** (never Bamini/legacy fonts).

## How to do common tasks

| Request | Do this |
|---|---|
| "Tree N planted on DATE by NAME" | Update that `TREES` entry: `date`, `by`, `status: "🌱 நடப்பட்டது"`. Optionally add an `UPDATES` item. |
| "Add news / photo" | Resize the photo to ≤1200 px wide, JPEG quality ~80 (keep each image under ~300 KB; visitors use mobile data), save to `images/` with a descriptive kebab-case name, prepend an `UPDATES` entry. |
| "Set contact details" | Fill `CONTACT`. Phone in international format `+94 7X XXX XXXX`. |
| "Replace the proposal PDF" | Overwrite `proposal.pdf` (keep the filename; the download button links to it). |
| New QR codes needed | `pip install "qrcode[pil]"` → `python tools/make_qr.py` → print `qr/print-sheet.html` to `qr/QR-plates-print.pdf` with Chrome (headless: `google-chrome --headless=new --no-pdf-header-footer --print-to-pdf=qr/QR-plates-print.pdf qr/print-sheet.html`). Uses error correction **H**. Verify by decoding (e.g. OpenCV `QRCodeDetector`). |
| Old Bamini-font Tamil PDF/text | `pip install pymupdf` → `python tools/bamini_to_unicode.py file.pdf`. Proofread the output. |

**Status vocabulary:** `⏳ விரைவில் நடப்படும்` (planting soon) · `🌱 நடப்பட்டது` (planted) · `🌿 நன்றாக வளர்கிறது` (growing well) ·
`🌼 பூத்துள்ளது` (flowering) · `⚠️ கவனம் தேவை` (needs attention).

**Tamil date style:** `16 நவம்பர் 2026` or Tamil month names like `கார்த்திகை 2026`. Keep a consistent style within a list.

## Rules

1. **Verify before pushing:** render the page (e.g. headless Chrome screenshot at `--window-size=400,2400`, also with
   `?tree=5`) and check Tamil renders and nothing overflows. After pushing, confirm the live URL returns 200 and shows the change.
2. **Commit identity:** commit as the project account, never a personal or work email:
   `git config user.name "shivanandian90batch"` and
   `git config user.email "354330513+shivanandian90batch@users.noreply.github.com"`.
   Write commit messages that say what changed for the project ("Tree 3 planted", "Add Nov planting photos").
3. **Credentials:** never print, commit or log tokens. If a user gives you a GitHub token, read it from a file or env var
   (`GH_TOKEN`) and push with `git -c credential.helper='!gh auth git-credential' push`. Don't save it into git config.
   Recommend fine-grained tokens scoped to this repo (Contents: read/write) with short expiry.
4. **Images and copyright:** only use photos the batch took or has rights to. Two images from the original proposal were
   deliberately **left out**: a flower close-up watermarked "NParks Flora & Fauna Web" (Singapore government site) and a
   "கொன்றை மரத்தின் மருத்துவ பயன்கள்" benefits poster of unknown origin. Don't re-add them without permission/credit.
5. **Privacy:** this is a public site about a school. Don't publish students' (minors') names, faces in close-up, or
   private phone numbers without the person's consent. Donors chose to be "ஒருவரால்" (anonymous) in the proposal; respect that.
6. Keep it simple: no frameworks, trackers, analytics, ads or external scripts beyond Google Fonts.

## Known issues in the original `proposal.pdf` (fixed on the website, not yet in the PDF)

| In PDF | Should be | Where |
|---|---|---|
| ஓளி | ஒளி | Cost table row 01 |
| நமமை | நம்மை | Section 2 |
| நேரடியாக் | நேரடியாக | Section 7 |
| நடுவதற்று | நடுவதற்கு | Section 10 |
| பொதுமக்களைக் பாதுகாத்தல் | பொதுமக்களைப் பாதுகாத்தல் | Section 4 |
| சிவாநந்த / சிவானந்த mixed | one consistent spelling | throughout |
| "Growth Halts" | "Tree Guards" | Sections 2, 4 |
| "Page 0 of 8" … "Page 7 of 8" | 1–8 | footers |

The PDF also uses the legacy **Tharmini** (Bamini-style) font, so its text isn't searchable or copyable as real Tamil.
If someone provides a corrected PDF, replace `proposal.pdf` and remove the fixed rows from this table.

## History

- **2026-11-06:** proposal written (Word 2019 → PDF).
- **2026-11-09:** website built from the proposal (Tamil converted Bamini → Unicode, typos fixed), repo created,
  GitHub Pages enabled, 13 QR codes generated and verified (main + trees 1–12).
- **TODO:** contact details (`CONTACT` is empty); planting dates/planters for all 12 trees after planting; planting-day photos.
