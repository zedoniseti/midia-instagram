"""Render slides do Cap. 2 (1080x1350) no layout do Cap. 1. Uso: python render.py slide01 [foto.jpg]"""
import sys, pathlib, base64
from playwright.sync_api import sync_playwright
HERE = pathlib.Path(__file__).parent
OUT = HERE.parent
N = 7

def dots(i):
    return "".join(f'<span class="dot{" on" if k==i else ""}"></span>' for k in range(1, N+1))

def bg(photo):
    if photo and pathlib.Path(photo).exists():
        b = base64.b64encode(pathlib.Path(photo).read_bytes()).decode()
        return f"url(data:image/jpeg;base64,{b})"
    return "linear-gradient(160deg,#3a2a1c 0%,#5b3f27 45%,#2a1d12 100%)"

CSS = """
*{margin:0;padding:0;box-sizing:border-box}
body{width:1080px;height:1350px;overflow:hidden;font-family:Poppins;color:#fff}
.s{position:relative;width:1080px;height:1350px;background-size:cover;background-position:center}
.s:before{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(14,18,30,.92) 0%,rgba(14,18,30,.70) 30%,rgba(14,18,30,.10) 55%,rgba(14,18,30,0) 70%,rgba(14,18,30,.70) 100%)}
.cta,.h{text-shadow:0 2px 10px rgba(0,0,0,.85)}
.cta i{box-shadow:0 1px 6px rgba(0,0,0,.8)}
.c{position:absolute;inset:0;padding:80px}
.dots{display:flex;gap:14px;margin-top:6px}
.dot{width:14px;height:14px;border:2px solid #fff;border-radius:50%}
.dot.on{background:#F5C518;border-color:#F5C518}
.tag{margin-top:64px;font-weight:600;font-size:24px;letter-spacing:3px;color:#F5C518}
h1{font-family:Lora;font-weight:700;font-size:92px;line-height:1.08;margin-top:22px}
h1 em{color:#F5C518;font-style:italic}
.sub{font-size:31px;margin-top:30px;max-width:900px}
.cta{position:absolute;left:80px;bottom:92px;font-weight:700;font-size:24px;color:#F5C518;letter-spacing:.5px}
.cta i{display:block;width:108px;height:2px;background:#F5C518;margin-top:22px;position:relative}
.cta i:after{content:"";position:absolute;right:-1px;top:-6px;width:12px;height:12px;border-top:2px solid #F5C518;border-right:2px solid #F5C518;transform:rotate(45deg)}
.h{position:absolute;right:80px;bottom:82px;font-weight:600;font-size:22px}
"""

SLIDES = {
 "slide01_capa": lambda: f"""<div class="c"><div class="dots">{dots(1)}</div>
   <div class="tag">CAP. 2 · ETAPA 1</div>
   <h1>Seu terreno esconde<br>o que você <em>não vê.</em></h1>
   <div class="cta">ARRASTE PARA DESCOBRIR<i></i></div><div class="h">@eng.josedoniseti</div></div>""",
}

def render(name, photo=None):
    html = f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body><div class='s' style='background-image:{bg(photo)}'>{SLIDES[name]()}</div></body></html>"
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={"width":1080,"height":1350})
        pg.set_content(html); pg.wait_for_timeout(300)
        out = OUT / f"{name}.jpg"; pg.screenshot(path=str(out), type="jpeg", quality=92); b.close()
    print(out)

if __name__ == "__main__":
    render(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
