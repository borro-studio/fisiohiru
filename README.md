# Hiru Fisioterapia · web

Rediseño de fisiohiru.com (borrador). Web estática bilingüe EU/ES.

- `web/` — la web (HTML/CSS/JS estático, listo para subir al hosting)
- `build/` — `content.py` (textos de las páginas de servicios) y `build.py` (genera las páginas)

Regenerar páginas de servicio y legales (textos en `build/content.py` y `build/content_legal.py`):

```
python3 build/build.py
```

Publicar la vista previa (GitHub Pages, rama `gh-pages`):

```
git subtree push --prefix web origin gh-pages
```

> Borrador: las páginas llevan `noindex`. Quitarlo antes de publicar en el dominio real.

## Sin cookies ni recursos externos

Fuentes (`web/assets/fonts`) e iconos se sirven en local. `web/assets/icons.css` y `fonts/Phosphor.woff2` solo incluyen los iconos usados: si se añade un icono nuevo hay que regenerarlos a partir de `build/vendor/`. El mapa de Google solo se carga al pulsar "Ver mapa".

## Pendiente del cliente

- Titular legal y NIF (`build/content_legal.py` → `DATA`)
- Confirmar dirección (Plazaola 4 o 5)
