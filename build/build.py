"""Genera las páginas de servicios a partir de content.py.
Uso: python3 build/build.py  (desde la carpeta fisiohiru)
"""
import html, os
from content import PAGES

OUT = os.path.join(os.path.dirname(__file__), "..", "web")


def t(pair, tag="span"):
    """Texto bilingüe como dos spans con lang."""
    eu, es = (html.escape(x, quote=False) for x in pair)
    if eu == es:
        return eu
    return f'<{tag} lang="eu">{eu}</{tag}><{tag} lang="es">{es}</{tag}>'


HEAD = """<!doctype html>
<html lang="eu">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{title} · Hiru Fisioterapia</title>
<meta name="description" content="{desc}">
<link rel="icon" href="assets/logo.png">
<script>(()=>{{const r=document.documentElement,q=new URLSearchParams(location.search),t=q.get("theme");if(t)r.dataset.theme=t;if(!q.has("static"))r.classList.add("js");try{{const l=localStorage.getItem("hiru-lang");if(l)r.lang=l}}catch(e){{}}}})()</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400;12..96,600;12..96,700&family=Hanken+Grotesk:ital,wght@0,400;0,500;0,600;1,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://unpkg.com/@phosphor-icons/web@2.1.1/src/regular/style.css">
<link rel="stylesheet" href="https://unpkg.com/@phosphor-icons/web@2.1.1/src/fill/style.css">
<link rel="stylesheet" href="assets/styles.css">
<link rel="preload" as="image" href="assets/{img}">
</head>
<body>
"""

NAV = """<header class="nav" id="nav">
  <div class="wrap">
    <a href="index.html" class="logo" aria-label="Hiru Fisioterapia"><img src="assets/logo.png" alt="Hiru Fisioterapia" width="143" height="62"></a>
    <nav class="nav-links" id="navLinks">
      <a href="index.html#zerbitzuak" aria-current="page"><span lang="eu">Zerbitzuak</span><span lang="es">Servicios</span></a>
      <a href="index.html#ekintzak"><span lang="eu">Ekintzak</span><span lang="es">Actividades</span></a>
      <a href="index.html#taldea"><span lang="eu">Taldea</span><span lang="es">Equipo</span></a>
      <a href="index.html#instalazioak"><span lang="eu">Instalazioak</span><span lang="es">Instalaciones</span></a>
      <a href="index.html#kontaktua"><span lang="eu">Kontaktua</span><span lang="es">Contacto</span></a>
    </nav>
    <div class="nav-right">
      <div class="lang" role="group" aria-label="Hizkuntza / Idioma">
        <button type="button" data-lang="eu" aria-pressed="true">EU</button>
        <button type="button" data-lang="es" aria-pressed="false">ES</button>
      </div>
      <a href="tel:+34943049797" class="btn btn-primary"><i class="ph ph-phone"></i><span><span lang="eu">Hitzordua</span><span lang="es">Pedir cita</span></span></a>
      <button class="menu-btn" id="menuBtn" aria-label="Menu" aria-expanded="false"><i class="ph ph-list"></i></button>
    </div>
  </div>
</header>
"""

FOOT = """<footer>
  <div class="wrap">
    <a href="index.html"><img class="foot-logo" src="assets/logo.png" alt="Hiru Fisioterapia"></a>
    <nav>
      <a href="#"><span lang="eu">Pribatutasun politika</span><span lang="es">Política de privacidad</span></a>
      <a href="#">Cookies</a>
      <a href="#"><span lang="eu">Lege oharra</span><span lang="es">Aviso legal</span></a>
    </nav>
    <span>© 2026 Hiru Fisioterapia</span>
  </div>
</footer>
<script src="assets/main.js"></script>
</body>
</html>
"""


def service_block(s, i):
    out = [f'<article class="svc-sec rv" id="{s["id"]}">']
    out.append(f'<h2>{t(s["title"])}</h2>')
    out.append(f'<p class="sec-lead">{t(s["lead"])}</p>')
    if s.get("img"):
        out.append(f'<figure class="sec-img"><img src="assets/{s["img"]}" alt="" loading="lazy"></figure>')
    out.append('<div class="sec-body">' + "".join(f"<p>{t(p)}</p>" for p in s["body"]) + "</div>")
    if s.get("list"):
        items = "".join(f'<li><i class="ph ph-check"></i>{t(x, "span")}</li>' for x in s["list"])
        out.append(f'<div class="sec-list"><h3>{t(s["list_title"])}</h3><ul class="checks">{items}</ul></div>')
    if s.get("note"):
        items = "".join(f"<li>{t(x)}</li>" for x in s["note"])
        out.append(f'<aside class="sec-note"><h3><i class="ph ph-warning-circle"></i>{t(s["note_title"])}</h3><ul>{items}</ul></aside>')
    out.append("</article>")
    return "\n".join(out)


def page(p):
    others = [o for o in PAGES if o is not p]
    n = len(p["services"])
    toc = "".join(f'<li><a href="#{s["id"]}">{t(s["title"])}</a></li>' for s in p["services"])
    more = "".join(
        f'''<a class="more-card rv" style="--i:{i}" href="{o["file"]}">
          <div class="ph"><img src="assets/{o["img"]}" alt="" loading="lazy"></div>
          <h3>{t(o["title"])} <i class="ph ph-arrow-up-right"></i></h3>
        </a>''' for i, o in enumerate(others))

    body = f"""<main>
  <section class="page-hero">
    <div class="wrap">
      <div>
        <nav class="crumbs rv" aria-label="breadcrumb">
          <a href="index.html"><span lang="eu">Hasiera</span><span lang="es">Inicio</span></a><i class="ph ph-caret-right"></i>
          <a href="index.html#zerbitzuak"><span lang="eu">Zerbitzuak</span><span lang="es">Servicios</span></a>
        </nav>
        <h1 class="rv" style="--i:1">{t(p["title"])}</h1>
        <p class="lead rv" style="--i:2">{t(p["lead"])}</p>
        <div class="hero-ctas rv" style="--i:3">
          <a href="tel:+34943049797" class="btn btn-primary"><i class="ph ph-phone"></i><span lang="eu">Hitzordua eskatu</span><span lang="es">Pedir cita</span></a>
          <span class="count-pill"><i class="ph ph-{p["icon"]}"></i>{n} <span lang="eu">zerbitzu</span><span lang="es">servicios</span></span>
        </div>
      </div>
      <figure class="page-hero-img rv" style="--i:1"><img src="assets/{p["img"]}" alt="" fetchpriority="high"></figure>
    </div>
  </section>

  <section class="svc-page">
    <div class="wrap">
      <aside class="toc">
        <p class="toc-title"><span lang="eu">Atal honetan</span><span lang="es">En esta página</span></p>
        <ul>{toc}</ul>
        <a href="tel:+34943049797" class="toc-call"><i class="ph ph-phone"></i><span><small><span lang="eu">Zalantzarik?</span><span lang="es">¿Dudas?</span></small>943 049 797</span></a>
      </aside>
      <div class="svc-sections">
{chr(10).join(service_block(s, i) for i, s in enumerate(p["services"]))}
      </div>
    </div>
  </section>

  <section class="cta-band">
    <div class="wrap">
      <div class="cta-card rv">
        <div>
          <h2><span lang="eu">Ez dakizu zein den zuretzat egokiena?</span><span lang="es">¿No sabes qué tratamiento es el tuyo?</span></h2>
          <p><span lang="eu">Kontatu zer gertatzen zaizun eta lehen saioan baloratuko dugu.</span><span lang="es">Cuéntanos qué te pasa y lo valoramos en la primera sesión.</span></p>
        </div>
        <div class="cta-actions">
          <a href="tel:+34943049797" class="btn btn-primary"><i class="ph ph-phone"></i>943 049 797</a>
          <a href="mailto:hiru@fisiohiru.com" class="btn btn-ghost-inv"><i class="ph ph-envelope-simple"></i>hiru@fisiohiru.com</a>
        </div>
      </div>
    </div>
  </section>

  <section class="more">
    <div class="wrap">
      <h2 class="rv"><span lang="eu">Beste zerbitzuak</span><span lang="es">Otros servicios</span></h2>
      <div class="more-grid">{more}</div>
    </div>
  </section>
</main>
"""
    head = HEAD.format(title=p["title"][0], desc=html.escape(p["lead"][1]), img=p["img"])
    return head + NAV + body + FOOT


for p in PAGES:
    with open(os.path.join(OUT, p["file"]), "w") as f:
        f.write(page(p))
    print("ok", p["file"])
