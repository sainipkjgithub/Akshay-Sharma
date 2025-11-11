# -*- coding: utf-8 -*-
"""
Appx File-Manager Style HTML Generator (Reusable Version)
अब यह function को दूसरी फाइल से भी call किया जा सकता है।
"""

import os, json

# --------------------- मुख्य फ़ंक्शन ---------------------
def generate_appx_html(input_file, output_file=None):
    """
    📘 Appx File-Manager HTML Generator
    ────────────────────────────────
    यह function दिए गए txt file से HTML बनाता है जो एक फाइल मैनेजर जैसा दिखता है।

    Parameters:
        input_file (str): ClassPlus डेटा फाइल (.txt) का path
        output_file (str, optional): HTML फाइल को सेव करने का path (auto-generate हो जाएगा)
    """
    def parse_input_file(filepath):
        tree = {"folders": {}, "files": []}
        count = 0

        with open(filepath, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]

        for line in lines:
            if "https" not in line:
                continue

            path, url = line.split(":", 1)
            url = url.strip()
            parts = [p.strip() for p in path.split(">")]

            title = parts[-1]
            folder_path = parts[:-1]
            final_video_url = f"https://apiv3.singodiya.tech/ClassPlus.html?url={url}"

            node = tree
            for p in folder_path:
                node = node["folders"].setdefault(p, {"folders": {}, "files": []})

            node["files"].append({
                "title": title,
                "video": final_video_url,
                "pdfs": []
            })
            count += 1

        return tree, count

    HTML_TEMPLATE = """<!doctype html>
<html lang="hi">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width,initial-scale=1" />
<title>Appx File Manager</title>
<style>
:root{--bg:#f5f7fb;--card:#ffffff;--muted:#6b7280;--accent:#2563eb;--success:#16a34a;}
*{box-sizing:border-box}
body{margin:0;font-family:Inter,Segoe UI,Roboto,Arial,sans-serif;background:var(--bg);color:#0f172a}
.header{display:flex;align-items:center;gap:12px;padding:12px 16px;background:linear-gradient(180deg,#fff,#f8fafc);box-shadow:0 1px 0 rgba(16,24,40,0.04)}
.btn{display:inline-flex;align-items:center;gap:8px;padding:8px 10px;border-radius:8px;background:transparent;border:1px solid #e6edf3;cursor:pointer}
.btn[disabled]{opacity:.5;cursor:default}
.title{font-weight:700;font-size:16px}
.container{padding:16px}
.toolbar{display:flex;align-items:center;gap:12px;margin-bottom:12px}
.breadcrumb{background:transparent;padding:6px 10px;border-radius:8px;border:1px solid #eef2f7}
.search{flex:1;display:flex}
.search input{width:100%;padding:8px 10px;border-radius:8px;border:1px solid #e6edf3}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:12px}
.card{background:var(--card);padding:12px;border-radius:10px;box-shadow:0 6px 18px rgba(14,165,233,0.03);border:1px solid rgba(15,23,42,0.03)}
.folder-card{display:flex;flex-direction:column;gap:8px;align-items:flex-start}
.folder-name{font-weight:700}
.meta{font-size:13px;color:var(--muted)}
.file-card{display:flex;flex-direction:column;gap:8px}
.file-title{font-weight:600}
.actions{display:flex;gap:8px;flex-wrap:wrap}
.action{padding:8px 10px;border-radius:8px;text-decoration:none;color:#fff;font-weight:600}
.action.video{background:var(--accent)}
.badge{background:#eef2ff;color:var(--accent);padding:4px 8px;border-radius:999px;font-size:12px}
.empty{padding:20px;text-align:center;color:var(--muted)}
.footer{padding:12px;text-align:center;font-size:13px;color:var(--muted)}
@media (max-width:600px){.grid{grid-template-columns:repeat(auto-fill,minmax(160px,1fr))}}
</style>
</head>
<body>
<div class="header">
  <button id="backBtn" class="btn">◀ Back</button>
  <div class="title">📂 Appx File Manager</div>
</div>

<div class="container">
  <div class="toolbar">
    <div class="breadcrumb" id="breadcrumb">/</div>
    <div class="search"><input id="searchInput" placeholder="Search..." /></div>
  </div>

  <div id="viewArea" class="grid"></div>
  <div id="empty" class="empty" style="display:none">कोई आइटम नहीं मिला।</div>
</div>
<div class="footer">Tip: फ़ोल्डर पर क्लिक करें — नया view खुलेगा।</div>

<script>
const TREE=%DATA%;
let path=[],currentNode=TREE;

function nodeAt(p){let n=TREE;for(const x of p){if(!n.folders[x])return null;n=n.folders[x];}return n;}
function render(){
  currentNode=nodeAt(path)||TREE;
  const view=document.getElementById('viewArea');
  view.innerHTML='';
  document.getElementById('breadcrumb').innerText=path.length?'/'+path.join(' / '):'/';
  document.getElementById('backBtn').disabled=!path.length;
  const q=document.getElementById('searchInput').value.trim().toLowerCase();
  const folders=Object.keys(currentNode.folders||{}).sort();
  for(const fname of folders){
    if(q && !fname.toLowerCase().includes(q))continue;
    const div=document.createElement('div');
    div.className='card folder-card';
    div.innerHTML=`<div class='folder-name'>📁 ${fname}</div>`;
    div.onclick=()=>{path.push(fname);render();window.scrollTo({top:0,behavior:'smooth'});}
    view.appendChild(div);
  }
  const files=currentNode.files||[];
  for(const f of files){
    const t=f.title;
    if(q && !t.toLowerCase().includes(q))continue;
    const div=document.createElement('div');
    div.className='card file-card';
    div.innerHTML=`<div class='file-title'>${t}</div>
    <div class='actions'><a class='action video' href='${f.video}' target='_blank'>▶ Open</a></div>`;
    view.appendChild(div);
  }
  document.getElementById('empty').style.display=(folders.length||files.length)?'none':'block';
}
document.getElementById('backBtn').onclick=()=>{if(path.length)path.pop();render();window.scrollTo({top:0,behavior:'smooth'});}
document.getElementById('searchInput').oninput=()=>render();
render();
</script>
</body>
</html>
"""

    try:
        tree, count = parse_input_file(input_file)
    except FileNotFoundError as e:
        print(f"❌ फ़ाइल नहीं मिली: {e}")
        return None

    html_content = HTML_TEMPLATE.replace("%DATA%", json.dumps(tree, ensure_ascii=False))

    if not output_file:
        # auto-generate output file path
        name = os.path.basename(input_file).replace(".txt", "")
        output_file = f"/storage/emulated/0/ClassPlus/V/{name}.html"

    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"✅ HTML तैयार हो गया: {output_file} (कुल {count} लिंक)")
    return output_file
