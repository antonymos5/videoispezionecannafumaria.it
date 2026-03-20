#!/usr/bin/env python3
"""
genera_pagine_citta.py — videoispezionecannafumaria.it
Brand: Videoispezioni | Tel: 333 645 3219 | Verde Oliva S.r.l.s
Genera 63 pagine città → /nome-citta/index.html
"""

import os, re

TELEFONO_DISPLAY = "333 645 3219"
TELEFONO_HREF    = "+393336453219"
EMAIL            = "info@videoispezionecannafumaria.it"
PIVA             = "10927440965"
DOMINIO          = "https://www.videoispezionecannafumaria.it"
ANNO             = "2025"

COMUNI = [
    ("Lodi","Lodi"),("Lodi Vecchio","Lodi"),("Casalpusterlengo","Lodi"),
    ("Sant'Angelo Lodigiano","Lodi"),("Codogno","Lodi"),("Castiglione d'Adda","Lodi"),
    ("Casalmaiocco","Lodi"),("Borghetto Lodigiano","Lodi"),("Maleo","Lodi"),
    ("Somaglia","Lodi"),("Fombio","Lodi"),("Guardamiglio","Lodi"),
    ("Senna Lodigiana","Lodi"),("San Martino in Strada","Lodi"),
    ("Tavazzano con Villavesco","Lodi"),("Montanaso Lombardo","Lodi"),
    ("Mulazzano","Lodi"),("Cornegliano Laudense","Lodi"),("Corno Giovine","Lodi"),
    ("Ospedaletto Lodigiano","Lodi"),("Secugnago","Lodi"),("Turano Lodigiano","Lodi"),
    ("Abbadia Cerreto","Lodi"),("Camairago","Lodi"),("Livraga","Lodi"),
    ("Massalengo","Lodi"),("Cervignano d'Adda","Lodi"),("Graffignana","Lodi"),
    ("Castiraga Vidardo","Lodi"),("Brembio","Lodi"),("Orio Litta","Lodi"),
    ("Pieve Fissiraga","Lodi"),("Villanova del Sillaro","Lodi"),
    ("Borgo San Giovanni","Lodi"),("Caselle Landi","Lodi"),
    ("Cavenago d'Adda","Lodi"),("Bertonico","Lodi"),("Crespiatica","Lodi"),
    ("Mairago","Lodi"),("Marudo","Lodi"),("Miradolo Terme","Lodi"),
    ("Salerano sul Lambro","Lodi"),("Terranova dei Passerini","Lodi"),
    ("Valera Fratta","Lodi"),("Dresano","Lodi"),
    ("Paullo","Milano"),("Melegnano","Milano"),("Vizzolo Predabissi","Milano"),
    ("San Zenone al Lambro","Milano"),("Zelo Buon Persico","Milano"),
    ("Spino d'Adda","Cremona"),("Pandino","Cremona"),("Rivolta d'Adda","Cremona"),
    ("Crema","Cremona"),("Soncino","Cremona"),("Pizzighettone","Cremona"),
    ("Corte de' Cortesi con Cignone","Cremona"),
    ("Pavia","Pavia"),("Belgioioso","Pavia"),("Landriano","Pavia"),
    ("Vigevano","Pavia"),("Mortara","Pavia"),("Voghera","Pavia"),
]

def slugify(n):
    s = n.lower().replace("'","-").replace("'","-")
    for a,b in [("à","a"),("á","a"),("è","e"),("é","e"),("ê","e"),
                ("ì","i"),("í","i"),("ò","o"),("ó","o"),("ù","u"),("ú","u")]:
        s = s.replace(a,b)
    s = re.sub(r"[^a-z0-9]+","-",s).strip("-")
    return s

def prep(n):
    return "ad" if n[0].lower() in "aeiou" else "a"

def genera(nome, provincia):
    sl  = slugify(nome)
    pr  = prep(nome)
    url = f"{DOMINIO}/{sl}/"
    PRP = pr.capitalize()

    return f"""<!DOCTYPE html>
<html lang="it">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width,initial-scale=1.0"/>
  <title>Ispezione Videoscopica Canna Fumaria {PRP} {nome} | Videoispezioni</title>
  <meta name="description" content="Ispezione videoscopica canna fumaria {pr} {nome} ({provincia}). Relazione tecnica con foto inclusa. Chiama il {TELEFONO_DISPLAY} — intervento rapido."/>
  <meta name="robots" content="index,follow"/>
  <link rel="canonical" href="{url}"/>
  <meta property="og:title" content="Ispezione Videoscopica Canna Fumaria {PRP} {nome} | Videoispezioni"/>
  <meta property="og:description" content="Controllo professionale canna fumaria con telecamera HD {pr} {nome}. Relazione tecnica inclusa. {TELEFONO_DISPLAY}"/>
  <meta property="og:type" content="website"/>
  <meta property="og:url" content="{url}"/>
  <link rel="preconnect" href="https://fonts.googleapis.com"/>
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
  <link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@400;700;800&family=Barlow:wght@300;400;500&display=swap" rel="stylesheet"/>
  <style>
    *,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
    :root{{--nero:#0d0f12;--carbone:#171a20;--grigio:#242830;--bordo:#2e333d;--testo:#c8cdd8;--chiaro:#e8ecf4;--bianco:#f4f6fb;--ambra:#f59e0b;--ambra2:#d97706;--font-h:'Barlow Condensed',sans-serif;--font-b:'Barlow',sans-serif}}
    html{{scroll-behavior:smooth}}
    body{{background:var(--nero);color:var(--testo);font-family:var(--font-b);font-size:17px;line-height:1.65;-webkit-font-smoothing:antialiased}}
    a{{color:var(--ambra);text-decoration:none}}
    a:hover{{text-decoration:underline}}
    .container{{width:92%;max-width:1080px;margin:0 auto}}
    .tag{{display:inline-block;background:rgba(245,158,11,.12);color:var(--ambra);border:1px solid rgba(245,158,11,.3);font-family:var(--font-h);font-size:.85rem;letter-spacing:.12em;text-transform:uppercase;padding:.3em .9em;border-radius:2px}}
    .btn{{display:inline-flex;align-items:center;gap:.5em;font-family:var(--font-h);font-weight:700;font-size:1.05rem;letter-spacing:.05em;text-transform:uppercase;padding:.75em 1.6em;border-radius:6px;cursor:pointer;border:none;transition:all .2s;text-decoration:none}}
    .btn-primary{{background:var(--ambra);color:var(--nero)}}
    .btn-primary:hover{{background:var(--ambra2);text-decoration:none;color:var(--nero);transform:translateY(-2px)}}
    section{{padding:70px 0}}

    .topbar{{background:var(--carbone);border-bottom:1px solid var(--bordo);padding:.55em 0;font-size:.86rem}}
    .topbar .container{{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:.4em}}
    .topbar-right{{display:flex;gap:1.4em}}
    .topbar-right a{{color:var(--chiaro);font-weight:500}}

    header{{position:sticky;top:0;z-index:100;background:rgba(13,15,18,.96);backdrop-filter:blur(12px);border-bottom:1px solid var(--bordo);padding:.9em 0}}
    .nav{{display:flex;align-items:center;justify-content:space-between}}
    .logo{{font-family:var(--font-h);font-size:1.4rem;font-weight:800;color:var(--bianco);letter-spacing:.03em}}
    .logo span{{color:var(--ambra)}}
    .logo small{{font-size:.7rem;font-weight:400;color:#646b7a;display:block;letter-spacing:.08em;text-transform:uppercase;margin-top:-.2em}}

    .hero{{background:radial-gradient(ellipse 70% 55% at 65% 45%,rgba(245,158,11,.08) 0%,transparent 65%),linear-gradient(160deg,#0d0f12 45%,#130f00 100%);border-bottom:1px solid var(--bordo);padding:80px 0 70px}}
    .breadcrumb{{font-size:.83rem;color:#555c6b;margin-bottom:1rem}}
    .breadcrumb a{{color:#646b7a}}
    .breadcrumb a:hover{{color:var(--ambra);text-decoration:none}}
    .hero-grid{{display:grid;grid-template-columns:1fr 370px;gap:3rem;align-items:start}}
    .hero h1{{font-family:var(--font-h);font-size:clamp(2.2rem,5vw,3.4rem);font-weight:800;line-height:1.07;color:var(--bianco);margin:.8rem 0 1.2rem}}
    .hero h1 em{{font-style:normal;color:var(--ambra)}}
    .hero-sub{{font-size:1.05rem;color:var(--testo);margin-bottom:1.8rem;font-weight:300;line-height:1.7;max-width:520px}}
    .trust-row{{display:flex;gap:1.4rem;flex-wrap:wrap;margin-top:1.4rem;font-size:.87rem}}
    .trust-row span{{color:var(--testo)}}
    .trust-row span::before{{content:'✓ ';color:var(--ambra);font-weight:700}}

    .contact-card{{background:var(--carbone);border:1px solid var(--bordo);border-radius:12px;padding:1.8rem;position:relative}}
    .contact-card::before{{content:'';position:absolute;top:0;left:0;right:0;height:3px;background:linear-gradient(90deg,var(--ambra),var(--ambra2));border-radius:12px 12px 0 0}}
    .contact-card h3{{font-family:var(--font-h);font-weight:700;font-size:1.05rem;color:var(--bianco);margin-bottom:1rem;text-transform:uppercase;letter-spacing:.05em}}
    .check-list{{list-style:none;display:flex;flex-direction:column;gap:.6rem;margin-bottom:1.3rem}}
    .check-list li{{display:flex;align-items:flex-start;gap:.7em;font-size:.92rem}}
    .check-list li::before{{content:'✓';color:var(--ambra);font-weight:700;flex-shrink:0}}
    .card-divider{{height:1px;background:var(--bordo);margin:1rem 0}}
    .tel-link{{display:block;font-family:var(--font-h);font-size:1.75rem;font-weight:800;color:var(--bianco);text-align:center;letter-spacing:.03em;margin-bottom:.3rem}}
    .tel-link:hover{{color:var(--ambra);text-decoration:none}}
    .orari{{text-align:center;font-size:.8rem;color:#7a8090}}

    .servizi{{background:var(--carbone)}}
    .section-header{{text-align:center;margin-bottom:2.6rem}}
    .section-header h2{{font-family:var(--font-h);font-size:clamp(1.8rem,4vw,2.6rem);font-weight:800;color:var(--bianco);margin-top:.5rem;line-height:1.1}}
    .section-header p{{margin-top:.7rem;color:var(--testo);max-width:540px;margin-inline:auto}}
    .servizi-grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:1.4rem}}
    .serv-card{{background:var(--grigio);border:1px solid var(--bordo);border-radius:10px;padding:1.8rem;transition:transform .2s,border-color .2s}}
    .serv-card:hover{{transform:translateY(-4px);border-color:rgba(245,158,11,.4)}}
    .serv-icon{{width:48px;height:48px;background:rgba(245,158,11,.1);border:1px solid rgba(245,158,11,.22);border-radius:10px;display:flex;align-items:center;justify-content:center;margin-bottom:1rem;font-size:1.4rem}}
    .serv-card h3{{font-family:var(--font-h);font-size:1.15rem;font-weight:700;color:var(--bianco);margin-bottom:.5rem;text-transform:uppercase;letter-spacing:.04em}}
    .serv-card p{{font-size:.92rem;color:var(--testo);line-height:1.6}}

    .perche{{background:var(--nero)}}
    .perche-inner{{max-width:720px;margin:0 auto;text-align:center}}
    .perche-inner h2{{font-family:var(--font-h);font-size:clamp(1.8rem,4vw,2.6rem);font-weight:800;color:var(--bianco);margin:.6rem 0 1rem}}
    .feature-grid{{display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin:1.8rem 0;text-align:left}}
    .feat{{background:var(--carbone);border:1px solid var(--bordo);border-radius:8px;padding:1.2rem}}
    .feat-icon{{font-size:1.25rem;margin-bottom:.5rem}}
    .feat h4{{font-family:var(--font-h);font-size:.98rem;font-weight:700;text-transform:uppercase;color:var(--bianco);letter-spacing:.04em;margin-bottom:.25rem}}
    .feat p{{font-size:.87rem;color:var(--testo)}}

    .cta-box{{background:var(--carbone);border:1px solid rgba(245,158,11,.25);border-radius:12px;padding:2.4rem;text-align:center;margin-top:2rem}}
    .cta-box h2{{font-family:var(--font-h);font-size:clamp(1.6rem,3.5vw,2.2rem);font-weight:800;color:var(--bianco);margin-bottom:.7rem}}
    .cta-box p{{color:var(--testo);margin-bottom:1.5rem}}
    .cta-tel{{display:inline-block;font-family:var(--font-h);font-size:2.4rem;font-weight:800;color:var(--ambra);letter-spacing:.03em;margin-bottom:.4rem}}
    .cta-tel:hover{{color:var(--bianco);text-decoration:none}}

    footer{{background:var(--carbone);border-top:1px solid var(--bordo);padding:1.8rem 0;font-size:.83rem;color:#555c6b}}
    .footer-inner{{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:1rem}}
    .footer-links{{display:flex;gap:1.2rem;flex-wrap:wrap}}
    .footer-links a{{color:#646b7a}}
    .footer-links a:hover{{color:var(--ambra);text-decoration:none}}

    #cookie-banner{{position:fixed;bottom:0;left:0;right:0;z-index:9999;background:var(--carbone);border-top:2px solid var(--ambra);padding:1rem 1.4rem;display:flex;gap:1rem;align-items:center;flex-wrap:wrap}}
    #cookie-banner p{{flex:1;font-size:.84rem;color:var(--testo);min-width:200px}}
    #cookie-banner p a{{color:var(--ambra)}}
    .cb{{font-family:var(--font-h);font-weight:700;font-size:.87rem;text-transform:uppercase;letter-spacing:.06em;padding:.5em 1.2em;border-radius:4px;cursor:pointer;border:none}}
    .cb-ok{{background:var(--ambra);color:var(--nero)}}
    .cb-no{{background:transparent;color:var(--testo);border:1px solid var(--bordo)}}

    @media(max-width:900px){{.hero-grid{{grid-template-columns:1fr}}.servizi-grid{{grid-template-columns:1fr 1fr}}}}
    @media(max-width:600px){{section{{padding:50px 0}}.servizi-grid{{grid-template-columns:1fr}}.feature-grid{{grid-template-columns:1fr}}}}
  </style>
</head>
<body>

<div class="topbar">
  <div class="container">
    <span>📍 {nome} ({provincia}) — Intervento in giornata</span>
    <div class="topbar-right">
      <a href="tel:{TELEFONO_HREF}">📞 {TELEFONO_DISPLAY}</a>
      <a href="mailto:{EMAIL}">✉ Scrivi</a>
    </div>
  </div>
</div>

<header>
  <div class="container nav">
    <a href="/" class="logo">Video<span>ispezioni</span><small>canna fumaria · lodi e provincia</small></a>
    <a href="tel:{TELEFONO_HREF}" class="btn btn-primary">📞 Chiama Subito</a>
  </div>
</header>

<section class="hero">
  <div class="container">
    <div class="breadcrumb"><a href="/">Home</a> › <a href="/">Ispezione Videoscopica</a> › {nome}</div>
    <div class="hero-grid">
      <div>
        <span class="tag">Provincia di {provincia}</span>
        <h1>Ispezione Videoscopica<br>Canna Fumaria<br><em>{PRP} {nome}</em></h1>
        <p class="hero-sub">Controllo professionale della canna fumaria con telecamera HD {pr} {nome}. Rilasciamo relazione tecnica scritta con foto al termine di ogni intervento. Personale qualificato, risposta rapida.</p>
        <a href="tel:{TELEFONO_HREF}" class="btn btn-primary">📞 {TELEFONO_DISPLAY}</a>
        <div class="trust-row">
          <span>Relazione tecnica inclusa</span>
          <span>Foto documentazione</span>
          <span>Intervento in giornata</span>
          <span>Pulizia su richiesta</span>
        </div>
      </div>
      <div class="contact-card">
        <h3>✅ Incluso nel servizio</h3>
        <ul class="check-list">
          <li>Ispezione con telecamera HD professionale</li>
          <li>Relazione tecnica scritta dettagliata</li>
          <li>Documentazione fotografica del condotto</li>
          <li>Rilevamento crepe, distacchi e ostruzioni</li>
          <li>Consulenza sugli interventi necessari</li>
          <li>Collegamento diretto servizio pulizia</li>
        </ul>
        <div class="card-divider"></div>
        <a href="tel:{TELEFONO_HREF}" class="tel-link">📞 {TELEFONO_DISPLAY}</a>
        <p class="orari">Lun–Sab 8:00–18:00 · Risposta immediata</p>
      </div>
    </div>
  </div>
</section>

<section class="servizi">
  <div class="container">
    <div class="section-header">
      <span class="tag">Servizi {PRP} {nome}</span>
      <h2>Cosa facciamo per te</h2>
      <p>Ispezione, documentazione e pulizia: tutto in un unico intervento {pr} {nome}.</p>
    </div>
    <div class="servizi-grid">
      <div class="serv-card"><div class="serv-icon">🎥</div><h3>Ispezione Videoscopica</h3><p>Telecamera HD inserita nel condotto fumario {pr} {nome}. Rilievo in tempo reale di crepe, ostruzioni e anomalie strutturali con registrazione video inclusa.</p></div>
      <div class="serv-card"><div class="serv-icon">📋</div><h3>Relazione Tecnica + Foto</h3><p>Referto scritto dettagliato con fotografie del condotto. Valido per assicurazioni, condomini e pratiche di conformità impianto {pr} {nome}.</p></div>
      <div class="serv-card"><div class="serv-icon">🔗</div><h3>Pulizia & Spazzacamino</h3><p>Se l'ispezione rileva depositi, organizziamo subito il servizio di pulizia professionale {pr} {nome}. Un operatore, un appuntamento, soluzione completa.</p></div>
    </div>
  </div>
</section>

<section class="perche">
  <div class="container">
    <div class="perche-inner">
      <span class="tag">Perché sceglierci</span>
      <h2>Il tecnico di fiducia<br>{PRP} {nome}</h2>
      <p>Interveniamo direttamente {pr} {nome} e in tutta la provincia di {provincia} con attrezzatura professionale e risposta rapida.</p>
      <div class="feature-grid">
        <div class="feat"><div class="feat-icon">📍</div><h4>Locale</h4><p>Interveniamo {pr} {nome} rapidamente, senza attese.</p></div>
        <div class="feat"><div class="feat-icon">🎯</div><h4>Telecamera HD</h4><p>Testata rotativa 360° con LED integrati. Nessun punto cieco.</p></div>
        <div class="feat"><div class="feat-icon">📄</div><h4>Documentazione</h4><p>Relazione scritta valida per usi assicurativi e condominiali.</p></div>
        <div class="feat"><div class="feat-icon">🔧</div><h4>Servizio completo</h4><p>Dall'ispezione alla pulizia, unico operatore di fiducia.</p></div>
      </div>
    </div>
    <div class="cta-box">
      <h2>Prenota l'ispezione {PRP} {nome}</h2>
      <p>Contattaci oggi per un appuntamento rapido. Disponibili in giornata.</p>
      <a href="tel:{TELEFONO_HREF}" class="cta-tel">📞 {TELEFONO_DISPLAY}</a><br>
      <small style="color:#7a8090">Lun–Sab 8:00–18:00 · Verde Oliva S.r.l.s – P.IVA IT{PIVA}</small>
    </div>
  </div>
</section>

<footer>
  <div class="container footer-inner">
    <span>© {ANNO} Verde Oliva S.r.l.s – P.IVA IT{PIVA} · Marchio Videoispezioni</span>
    <div class="footer-links">
      <a href="/">Home</a>
      <a href="/privacy.html">Privacy Policy</a>
      <a href="/cookie.html">Cookie Policy</a>
    </div>
  </div>
</footer>

<div id="cookie-banner">
  <p>Usiamo cookie tecnici e, previo consenso, analitici. <a href="/privacy.html">Privacy Policy</a> · <a href="/cookie.html">Cookie Policy</a>.</p>
  <button class="cb cb-no" onclick="r()">Solo necessari</button>
  <button class="cb cb-ok" onclick="a()">Accetta tutti</button>
</div>

<script type="application/ld+json">
{{
  "@context":"https://schema.org",
  "@type":"LocalBusiness",
  "name":"Videoispezioni – Ispezione Videoscopica Canna Fumaria {nome}",
  "description":"Ispezione videoscopica canna fumaria {pr} {nome} ({provincia}). Relazione tecnica con foto inclusa.",
  "url":"{url}",
  "telephone":"{TELEFONO_HREF}",
  "vatID":"IT{PIVA}",
  "legalName":"Verde Oliva S.r.l.s",
  "address":{{"@type":"PostalAddress","addressLocality":"{nome}","addressRegion":"{provincia[:2].upper()}","addressCountry":"IT"}},
  "areaServed":{{"@type":"City","name":"{nome}"}}
}}
</script>
<script>
  (function(){{if(localStorage.getItem('cc'))document.getElementById('cookie-banner').style.display='none';}})();
  function a(){{localStorage.setItem('cc','all');document.getElementById('cookie-banner').style.display='none';}}
  function r(){{localStorage.setItem('cc','min');document.getElementById('cookie-banner').style.display='none';}}
</script>
</body>
</html>
"""

def main():
    base = os.path.dirname(os.path.abspath(__file__))
    tot  = 0
    for nome, provincia in COMUNI:
        sl = slugify(nome)
        os.makedirs(os.path.join(base, sl), exist_ok=True)
        fp = os.path.join(base, sl, "index.html")
        with open(fp,"w",encoding="utf-8") as f:
            f.write(genera(nome, provincia))
        tot += 1
        print(f"  ✓  /{sl}/  ({nome})")
    print(f"\n✅ {tot} pagine generate in '{base}'")
    print("📁 Pronto per GitHub Pages — carica tutta la cartella nel repository")

if __name__=="__main__":
    main()
