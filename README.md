# Worlds Without Number — SRD (en español)

Traducción al español del **System Reference Document (SRD) v1.0** de
[*Worlds Without Number*](https://www.drivethrurpg.com/product/348809/Worlds-Without-Number),
el juego de rol de fantasía de Kevin Crawford (Sine Nomine Publishing).

El SRD original se distribuye bajo **CC0** (dominio público). Esta traducción se
publica igualmente bajo CC0 (véase `LICENSE`).

## Qué es

Un libro compilable con [markpublisher](https://github.com/ecruzolivera/markpublisher),
que convierte Markdown extendido en HTML y PDF paginados. El resultado incluye las
7 secciones del SRD —creación de personajes, reglas, equipo, magia, monstruos,
facciones y proyectos mayores— más el bestiario de ejemplo y un glosario.

## Requisitos

- Node.js **≥ 22.12**
- `markpublisher` (se instala desde npm)

## Compilar

```bash
npm install -g markpublisher
npx puppeteer browsers install chrome   # para generar el PDF
markpublisher build
```

El resultado se escribe en `output/` (`Worlds Without Number — SRD.html` y `.pdf`).

## Estructura

```
WWN-SRD/
├── Worlds Without Number.md   ← archivo principal (portada, glosario, TOC, includes)
├── markpublisher.toml         ← configuración de compilación
├── themes/wwn/theme.css       ← tema A4 a dos columnas
├── capitulos/                 ← capítulos traducidos (Markdown)
├── criaturas/                 ← bestiario de ejemplo
├── parciales/                 ← glosario (parcial incluido)
├── en/                        ← extracción fuente del PDF (referencia)
├── tools/                     ← pdf_to_md.py, paginate.py, translation-spec.md…
└── .github/workflows/         ← CI: genera PDF/HTML en cada release
```

## Créditos

- **Autor del SRD original**: Kevin Crawford / Sine Nomine Publishing.
- Contenido publicado bajo [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/).
- Traducción y maquetación: Ernesto Cruz Olivera.
