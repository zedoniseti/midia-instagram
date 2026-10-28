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
h2{font-family:Lora;font-weight:700;font-size:84px;line-height:1.1;color:#F5C518;margin-top:86px}

.dark{background:radial-gradient(120% 90% at 30% 20%,#1a1d26 0%,#0f1117 70%)}
.dark:before{display:none}
.dg{position:absolute;left:0;top:480px}
.lb{font:700 24px Poppins;fill:#F5C518;letter-spacing:2px}
.lbs{font:600 24px Poppins;fill:#F5C518}
.lbr{font:600 24px Poppins;fill:#ff6b6d}
.fecho{position:absolute;left:80px;bottom:132px;font-family:Lora;font-weight:700;font-size:46px}
.fecho em{color:#ff6b6d;font-style:normal}
.h{position:absolute;right:80px;bottom:82px;font-weight:600;font-size:22px}
"""

SLIDES = {
 "slide02_erro": lambda: f"""<div class="c"><div class="dots">{dots(2)}</div>
   <h2>Pular essa etapa<br>para economizar</h2>
   <div class="sub">O barato vira trinca, recalque e fundação refeita.</div>
   <div class="h">@eng.josedoniseti</div></div>""",
 "slide02_erro_esquema": lambda: f"""<div class="c"><div class="dots">{dots(2)}</div>
   <h2>Pular essa etapa<br>para economizar</h2>
   <div class="sub">O barato vira trinca, recalque e fundação refeita.</div></div>
   
<svg class="dg" viewBox="0 0 1080 660" width="1080" height="660" xmlns="http://www.w3.org/2000/svg">
 <defs>
  <pattern id="firm" width="22" height="22" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="22" stroke="#7a5a3c" stroke-width="3"/></pattern>
  <pattern id="soft" width="18" height="18" patternUnits="userSpaceOnUse"><circle cx="5" cy="5" r="2.2" fill="#c9a06a"/><circle cx="14" cy="13" r="1.6" fill="#c9a06a"/></pattern>
  <marker id="ah" markerUnits="userSpaceOnUse" markerWidth="30" markerHeight="30" refX="6" refY="15" orient="auto"><path d="M0,0 L30,15 L0,30 z" fill="#F5C518"/></marker>
 </defs>
 <!-- solo -->
 <rect x="80" y="420" width="920" height="230" fill="#3b2a1c"/>
 <rect x="80" y="420" width="920" height="230" fill="url(#firm)" opacity=".55"/>
 <path d="M560,462 C600,436 900,436 960,462 C1005,500 995,600 930,628 C820,652 640,648 590,614 C545,575 535,500 560,462 Z" fill="#6b4c2e"/>
 <path d="M560,462 C600,436 900,436 960,462 C1005,500 995,600 930,628 C820,652 640,648 590,614 C545,575 535,500 560,462 Z" fill="url(#soft)" stroke="#F5C518" stroke-width="2.5" stroke-dasharray="10 8"/>
 <line x1="80" y1="420" x2="1000" y2="420" stroke="#9aa3b5" stroke-width="2"/>
 <!-- fundacao (lado direito afundou) -->
 <polygon points="250,412 830,448 830,478 250,442" fill="#8b93a3"/>
 <!-- paredes -->
 <polygon points="262,140 818,176 818,448 262,412" fill="#1d2333" stroke="#e8ebf2" stroke-width="4"/>
 <!-- telhado -->
 <polyline points="236,142 540,0 844,178" fill="none" stroke="#e8ebf2" stroke-width="4" stroke-linejoin="round"/>
 <line x1="236" y1="142" x2="844" y2="178" stroke="#e8ebf2" stroke-width="4"/>
 <!-- janelas e porta (acompanham a inclinacao) -->
 <polygon points="320,215 420,221 420,301 320,295" fill="none" stroke="#e8ebf2" stroke-width="3"/>
 <polygon points="640,236 740,242 740,322 640,316" fill="none" stroke="#e8ebf2" stroke-width="3"/>
 <polygon points="470,285 560,290 560,433 470,428" fill="none" stroke="#e8ebf2" stroke-width="3"/>
 <!-- trincas a 45 graus subindo em direcao ao lado que afundou -->
 <polyline points="580,440 596,420 592,404 612,384 608,368 628,346 640,330" fill="none" stroke="#ff4d4f" stroke-width="5" stroke-linejoin="round"/>
 <polyline points="740,244 756,226 752,212 772,194 780,182" fill="none" stroke="#ff4d4f" stroke-width="5" stroke-linejoin="round"/>
 <polyline points="560,292 574,274 570,262 588,244 586,232 600,214" fill="none" stroke="#ff4d4f" stroke-width="4" stroke-linejoin="round"/>
 <!-- setas -->
 <line x1="300" y1="470" x2="300" y2="486" stroke="#F5C518" stroke-width="5" marker-end="url(#ah)"/>
 <line x1="760" y1="488" x2="760" y2="548" stroke="#F5C518" stroke-width="9" marker-end="url(#ah)"/>
 <!-- rotulos -->
 <text x="120" y="560" class="lb">SOLO FIRME</text>
 <text x="612" y="612" class="lb">SOLO MOLE</text>
 <text x="796" y="522" class="lbs">afundou</text><text x="796" y="552" class="lbs">mais</text>
 <line x1="866" y1="300" x2="790" y2="210" stroke="#ff4d4f" stroke-width="2"/>
 <text x="852" y="330" class="lbr">trincas</text><text x="852" y="362" class="lbr">a 45°</text>
</svg>
   <div class="fecho">Recalque diferencial = <em>trinca.</em></div>
   <div class="h">@eng.josedoniseti</div>""",
 "slide01_capa": lambda: f"""<div class="c"><div class="dots">{dots(1)}</div>
   <div class="tag">CAP. 2 · ETAPA 1</div>
   <h1>Seu terreno esconde<br>o que você <em>não vê.</em></h1>
   <div class="cta">ARRASTE PARA DESCOBRIR<i></i></div><div class="h">@eng.josedoniseti</div></div>""",
}

def render(name, photo=None):
    html = f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body><div class='s{" dark" if name.endswith("esquema") else ""}' style='background-image:{bg(photo) if not name.endswith("esquema") else "radial-gradient(120% 90% at 30% 20%,#1a1d26 0%,#0f1117 70%)"}'>{SLIDES[name]()}</div></body></html>"
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={"width":1080,"height":1350})
        pg.set_content(html); pg.wait_for_timeout(300)
        out = OUT / f"{name}.jpg"; pg.screenshot(path=str(out), type="jpeg", quality=92); b.close()
    print(out)

if __name__ == "__main__":
    render(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
