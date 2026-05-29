# CLAUDE.md — videoispezionecannafumaria.it

## Descrizione e scopo

Sito dedicato al servizio di **ispezione videoscopica della canna fumaria** con telecamera HD. Fornisce relazione tecnica con foto e referto scritto al cliente. Il servizio è collegato e complementare a quello di spazzacamino di Eurospazzacamino.  
Sito HTML/CSS statico, pubblicato via GitHub Pages.

**Dominio:** https://www.videoispezionecannafumaria.it  
**Repository:** https://github.com/antonymos5/videoispezionecannafumaria.it

---

## Brand

- **Azienda:** Verde Oliva S.r.l.s.
- **P.IVA:** IT10927440965
- **Telefono:** 333 645 3219
- **Indirizzo:** Via Colombera 2, 26831 Casalmaiocco (LO)
- **Colori brand:** Nero `#0d0f12`, carbone `#171a20`, ambra/arancio `#f59e0b`
- **Font:** Barlow Condensed (titoli) + Barlow (corpo)

---

## Struttura cartelle

```
videoispezionecannafumaria.it/
├── index.html                  # Homepage principale
├── cookie.html                 # Cookie policy
├── google2a5f68fcbab4234d.html # Verifica Google Search Console
├── genera_pagine_citta.py      # Script Python per generare pagine comunali
├── CNAME                       # Dominio custom GitHub Pages
├── lodi/                       # Pagine geo-localizzate per comune
├── casalmaiocco/
├── sant-angelo-lodigiano/
├── codogno/
├── [altri ~60 comuni]/         # Una cartella per comune servito
└── ...
```

**Script generatore:** `genera_pagine_citta.py` — usare per creare o aggiornare pagine comunali in batch; non modificare le pagine generate manualmente senza poi aggiornare lo script.

---

## Zone geografiche target

Lodi (capoluogo), **Casalmaiocco** (sede operativa), e tutto il **Lodigiano**:  
Sant'Angelo Lodigiano, Codogno, Lodi Vecchio, San Martino in Strada, Tavazzano con Villavesco, Sordio, Massalengo, Marudo, Livraga, Brembio, Graffignana, San Colombano al Lambro, Secugnago, Turano Lodigiano, Valera Fratta, Borghetto Lodigiano, più comuni del milanese limitrofo (San Donato, San Giuliano, Paullo, Segrate, Pioltello, ecc.).

---

## Regole SEO specifiche

### Keyword primario del sito
- `videoispezione canna fumaria Lodi` — keyword principale homepage.
- `ispezione videoscopica canna fumaria [comune]` — keyword primario pagine geo.

### Pagine geo (cartelle comuni)
- `<title>`: `Videoispezione Canna Fumaria [Comune] | Ispezione Professionale – 333 645 3219`
- `<meta name="description">`: includere comune, telecamera HD, relazione tecnica, telefono.
- Canonical: `<link rel="canonical" href="https://www.videoispezionecannafumaria.it/[comune]/"/>`
- Schema.org `LocalBusiness` + `Service` con `areaServed` specifico per comune.
- H1 formato: `Videoispezione Canna Fumaria a [Comune]`
- Menzione obbligatoria: "relazione tecnica con foto", "telecamera HD", "referto scritto".

### Homepage
- Differenziazione chiave rispetto a eurospazzacamino.it: enfatizzare diagnosi tecnica, non solo pulizia.
- Structured data: `LocalBusiness` + `Service` (serviceType: "Ispezione Videoscopica").
- Interlink verso eurospazzacamino.it come servizio complementare (anchor: "pulizia canna fumaria Lodi").

### Contenuti
- Mai duplicare content tra pagine comunali: ogni `index.html` deve avere nome comune in H1, nel body e nei meta.
- Usare termini tecnici: "endoscopio", "videocamera flessibile", "condotto fumario", "norma UNI 10683".
- Highlight del vantaggio: "scopri ostruzioni, crepe, depositi di fuliggine prima che diventino pericolosi".

### Regole generali
- Immagini: `alt` descrittivo con keyword + comune. Formato WebP preferito.
- Velocità: nessun JS framework. CSS inline o in `<style>`.
- `sitemap.xml`: mantenere aggiornato includendo tutte le pagine comunali.
- `robots.txt`: `Allow: /` — nessuna pagina indicizzabile esclusa.
- La pagina `google2a5f68fcbab4234d.html` non va mai eliminata.

---

## Workflow GitHub

```bash
# Staging delle modifiche
git add <file>
# oppure
git add .

# Commit con messaggio descrittivo
git commit -m "descrizione della modifica"

# Pubblicazione
git push origin main
```

**Convenzioni commit:**
- `feat: aggiungi pagina videoispezione [comune]`
- `fix: correggi canonical [comune]`
- `seo: aggiorna meta description homepage`
- `script: aggiorna genera_pagine_citta.py`
- `style: aggiorna tema colori`

---

## Note operative

- Il sito è su **GitHub Pages** — push su `main` pubblica automaticamente.
- Lo script `genera_pagine_citta.py` genera le pagine comunali in automatico: eseguirlo dopo modifiche al template.
- Il servizio di videoispezione è **complementare** allo spazzacamino: linkare sempre a eurospazzacamino.it.
- Il numero **333 645 3219** deve essere sempre cliccabile: `<a href="tel:+393336453219">`.
- Enfatizzare la **relazione tecnica scritta** come elemento differenziante rispetto alla concorrenza.
- Non eliminare `google2a5f68fcbab4234d.html` (verifica Search Console).
