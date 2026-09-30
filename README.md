# Hiru Fisioterapia · web

Rediseño de fisiohiru.com (borrador). Web estática bilingüe EU/ES.

- `web/` — la web (HTML/CSS/JS estático, listo para subir al hosting)
- `build/` — `content.py` (textos de las páginas de servicios) y `build.py` (genera las páginas)

Regenerar páginas de servicio:

```
python3 build/build.py
```

Publicar la vista previa (GitHub Pages, rama `gh-pages`):

```
git subtree push --prefix web origin gh-pages
```

> Borrador: las páginas llevan `noindex`. Quitarlo antes de publicar en el dominio real.
