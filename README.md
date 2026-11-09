# 🌳 பசுமைச் செயற்திட்டம் 2026 · Green Project 2026

Website for the **Thirukkonrai (Cassia fistula) shade-tree project** by the **2006 O/L – 2009 A/L "90 Batch"**
of **RKM Shivananda National School, Kalladi, Batticaloa**.

**Live site:** https://shivanandian90batch.github.io

QR code plates on each tree open this website. This guide is for any batch member who wants to update it.
**You do not need to know programming or install anything.** You can do it in a web browser, or ask an AI assistant
(Claude, ChatGPT, Copilot…) to do it for you; the AI instructions are in [`CLAUDE.md`](CLAUDE.md).

---

## 📌 How it works (in 30 seconds)

- The whole website is **one file**: [`index.html`](index.html).
- GitHub hosts it for free. Every time a change is saved ("committed"), the live site updates in **about 1 minute**.
- **The QR codes never need to change.** Edit the website as much as you like; the plates on the trees keep working.

### Per-tree QR codes

There are 13 QR codes:

| QR code | Opens |
|---|---|
| Main ("இணையதளம்") | https://shivanandian90batch.github.io/ |
| Tree 01 … Tree 12 | https://shivanandian90batch.github.io/?tree=1 … `?tree=12` |

When someone scans a **tree's** QR code, the `?tree=N` part makes the site show a yellow box at the top:
**"🌳 நீங்கள் நிற்பது: மரம் இல. 05"** ("You are standing at: Tree No. 05"), with that tree's planting date,
who planted it and its status. That tree's row is also highlighted in the 12-trees table.
Opening the site normally (without `?tree=`) shows no box, which is why you don't see it on the main site.

Try it: https://shivanandian90batch.github.io/?tree=5

---

## ✏️ How to update the site (in a web browser, no software needed)

You need a GitHub account and to be added as a collaborator (ask the account owner, see below).

1. Open https://github.com/shivanandian90batch/shivanandian90batch.github.io
2. Click **`index.html`**, then the **✏️ pencil icon** (top-right of the file).
3. Press **Ctrl+F** and search for **`EASY-UPDATE SECTION`**. Everything you normally change is right there:

```js
const CONTACT = {
  name:  "க. குமார்",
  phone: "+94 77 123 4567",     // also creates the WhatsApp button
  email: ""
};

const TREES = [
  { no: 1, date: "16 நவம்பர் 2026", by: "க. குமார்", status: "🌱 நடப்பட்டது" },
  ...
];

const UPDATES = [   // newest first
  { date: "நவம்பர் 2026", text: "12 மரங்களும் நடப்பட்டன!", image: "images/planting-day.jpg" },
  ...
];
```

4. Change only the text **inside the quotes `" "`**. Keep the commas, brackets and quotes as they are.
5. Click the green **Commit changes…** button, write a short note (e.g. "Tree 3 planted"), and click **Commit changes**.
6. Wait about 1 minute and refresh the live site.

**Status ideas for trees:** `🌱 நடப்பட்டது` (planted), `🌿 நன்றாக வளர்கிறது` (growing well),
`🌼 பூத்துள்ளது` (flowering), `⚠️ கவனம் தேவை` (needs attention), `⏳ விரைவில் நடப்படும்` (planting soon)

### Adding a photo

1. In the repo, open the **`images`** folder → **Add file → Upload files** → drag the photo in → **Commit changes**.
   *Tip: phone photos are large. Resize to about 1200 px wide first (e.g. with squoosh.app) so the site loads fast on mobile data.*
2. Then in `index.html`, add an `UPDATES` entry with `image: "images/your-photo-name.jpg"`.

### Made a mistake?

Nothing is lost. Open the repo → **Commits** (clock icon) → find the last good version → or just ask an AI assistant to "undo the last change".

---

## 🤖 Using an AI assistant to update it

If you use **Claude Code** (or another AI coding assistant) on a computer:

```bash
git clone https://github.com/shivanandian90batch/shivanandian90batch.github.io.git
cd shivanandian90batch.github.io
claude          # then just say e.g. "Tree 4 planted on 16 Nov by Ravi, add a news post with this photo"
```

The AI reads [`CLAUDE.md`](CLAUDE.md), which holds all the project background, rules and how-tos.

---

## 👥 Giving a batch member edit access

Account owner: **Settings → Collaborators → Add people** → enter their GitHub username → they accept the email invite.

---

## 📁 What's in this repo

| Path | What it is |
|---|---|
| `index.html` | The whole website (content + design). Edit the **EASY-UPDATE SECTION** near the bottom. |
| `images/` | Photos used on the site |
| `proposal.pdf` | The original project proposal (download button on the site) |
| `qr/` | QR code images + **`QR-plates-print.pdf`** (A4, ready to print) |
| `tools/make_qr.py` | Regenerates the QR codes (only needed if the website address ever changes) |
| `tools/bamini_to_unicode.py` | Converts old Bamini/Tharmini-font Tamil PDFs to normal Unicode Tamil |
| `CLAUDE.md` | Instructions and project memory for AI assistants |
| `.nojekyll` | Tells GitHub to serve the files as-is (don't delete) |

---

## 🖨️ Printing the QR plates

Print `qr/QR-plates-print.pdf`, or give the `qr/qr-*.png` files to a print shop.
- At least **5 × 5 cm** QR size; bigger is better.
- Outdoors in the sun, use **aluminium / acrylic, UV-printed or engraved**. Laminated paper fades within months.
- Scan each plate with a phone before fixing it to the tree.

---

Friends Forever · One Family · Proud as a Shivanandian 🌼
