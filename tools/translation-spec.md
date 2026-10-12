# Especificación de traducción — Worlds Without Number SRD v1.0

Reglas y glosario interno para traducir el SRD al español de forma consistente.
Este archivo es una referencia de trabajo (no forma parte del libro).

## Reglas de formato (OBLIGATORIAS)

1. **Jerarquía de encabezados**: usar `#` para el título del capítulo, `##` para
   las secciones de nivel `X.0.0`/`X.Y.0`, `###` para `X.Y.Z`. Conservar el
   número original entre paréntesis o prefijo cuando ayude (p. ej. `## 1.1 Atributos`).

2. **Directivas markpublisher**: cada capítulo empieza con `# Título`.
   Usar `<!-- layout:twocol -->` por defecto; `<!-- layout:singlecol -->` para
   tablas anchas (armas, armaduras); `<!-- wide -->`/`<!-- /wide -->` para
   intros o tablas que deban abarcar ambas columnas; `<!-- pagebreak -->` entre
   bloques grandes. No añadir `<!-- pagebreak -->` innecesarios dentro de un
   flujo continuo.

3. **Tablas**: markdown `| … |` con cabeceras centradas (`:--:`) cuando la
   columna sea corta/numérica. Conservar TODAS las filas y columnas exactas.

4. **Bloques de estadísticas**: usar etiquetas en negrita (`**CA** 12, **PG** 5,
**DG** 1d6, **Bono de ataque** +2, **Choque** 2/CA 15…`).

5. **Fidelidad numérica total**: no resumir. Cada valor, rango, tirada, nivel y
   entrada de tabla se conserva. `d6`/`d20` se conservan como notación.

6. **Nombres propios y de marca**: conservar nombres de hechizos, artes y
   lugares propios; traducir solo el texto descriptivo. Los nombres de clases y
   habilidades usan SIEMPRE la traducción del glosario interno de abajo.

7. **Sin comentarios ni notas** salvo los de esta especificación.

## Glosario interno (EN → ES) — NORMATIVO

### Atributos

| EN           | ES           | Abrev. |
| ------------ | ------------ | ------ |
| Strength     | Fuerza       | FUE    |
| Dexterity    | Destreza     | DES    |
| Constitution | Constitución | CON    |
| Intelligence | Inteligencia | INT    |
| Wisdom       | Sabiduría    | SAB    |
| Charisma     | Carisma      | CAR    |

### Habilidades

| EN         | ES             |
| ---------- | -------------- |
| Administer | Administración |
| Connect    | Trato          |
| Convince   | Persuasión     |
| Craft      | Artesanía      |
| Exert      | Atletismo       |
| Heal       | Sanar          |
| Know       | Saber          |
| Lead       | Liderazgo      |
| Magic      | Magia          |
| Notice     | Percepción     |
| Perform    | Actuación      |
| Pray       | Plegaria       |
| Punch      | Pelea          |
| Ride       | Montar         |
| Sail       | Navegar        |
| Shoot      | Disparo        |
| Sneak      | Sigilo         |
| Stab       | Apuñalar       |
| Survive    | Supervivencia  |
| Trade      | Comercio       |
| Work       | Trabajo        |

### Clases

| EN            | ES                    |
| ------------- | --------------------- |
| Warrior       | Guerrero              |
| Expert        | Experto               |
| Mage          | Mago                  |
| Adventurer    | Aventurero            |
| Accursed      | Maldito               |
| Bard          | Bardo                 |
| Beastmaster   | Señor de las bestias  |
| Blood Priest  | Sacerdote de sangre   |
| Duelist       | Duelista              |
| Elementalist  | Elementalista         |
| Healer        | Sanador               |
| High Mage     | Alto mago             |
| Invoker       | Invocador             |
| Mageslayer    | Mata-magos            |
| Necromancer   | Nigromante            |
| Skinshifter   | Cambiapieles          |
| Thought Noble | Noble del pensamiento |
| Vowed         | Consagrado            |
| Wise          | Sabio                 |
| Partial class | Clase parcial         |
| Full class    | Clase completa        |

### Términos de sistema

| EN                       | ES                         |
| ------------------------ | -------------------------- |
| Armor Class (AC)         | Clase de Armadura (CA)     |
| Hit Points (HP)          | Puntos de Golpe (PG)       |
| Hit Dice (HD)            | Dados de Golpe (DG)        |
| Attack Bonus             | Bono de ataque             |
| Saving Throw             | Tirada de salvación        |
| System Strain            | Tensión del sistema        |
| Effort                   | Esfuerzo                     |
| Commit Effort            | Dedicar Esfuerzo             |
| Fray die                 | Dado de desgaste           |
| Focus / Foci             | Foco / Focos               |
| Art / Arts               | Arte / Artes               |
| Instinct                 | Instinto                   |
| Morale (ML)              | Moral (ML)                 |
| Encumbrance              | Carga                      |
| Renown                   | Renombre                   |
| Scene                    | Escena                     |
| Round                    | Ronda                      |
| Turn                     | Turno                      |
| Main Action              | Acción principal           |
| Move Action              | Acción de movimiento       |
| On Turn Action           | Acción en el turno         |
| Instant Action           | Acción instantánea         |
| Skill check              | Prueba de habilidad        |
| Shock                    | Choque                     |
| Silver piece (sp)        | Pieza de plata (pp)        |
| Gold piece (gp)          | Pieza de oro (po)          |
| Copper piece (cp)        | Pieza de cobre (pc)        |
| Mortally Wounded         | Herido de muerte           |
| Non-Lethal Damage        | Daño no letal              |
| Trauma                   | Trauma                     |
| Killing Blow             | Golpe letal                |
| Veteran’s Luck           | Suerte del veterano        |
| Execution Attack         | Ataque de ejecución        |
| Faction                  | Facción                    |
| Asset                    | Activo                     |
| Cunning / Force / Wealth | Astucia / Fuerza / Riqueza |
| Faction Turn             | Turno de facción           |
| Major Project            | Proyecto mayor             |
| High Magic               | Alta magia                 |
| Mage                     | Mago                       |
| Arcane Tradition         | Tradición arcana           |
| Working (magical)        | Obra (mágica)              |
| Prepared spell           | Conjuro preparado          |
| Spell                    | Conjuro / hechizo          |
| Reaction Roll            | Tirada de reacción         |
| Morale Check             | Prueba de moral            |
| Instinct Check           | Prueba de instinto         |

### Focos (Focus) — nombres comunes

| EN                 | ES                  |
| ------------------ | ------------------- |
| Alert              | Alerta              |
| Authority          | Autoridad           |
| Armsmaster         | Maestro de armas    |
| Artisan            | Artesano            |
| Assassin           | Asesino             |
| Barbarian          | Bárbaro             |
| Crossbowman        | Ballestero          |
| Cultured           | Culto               |
| Deadeye            | Ojo certero         |
| Diplomatic Grace   | Gracia diplomática  |
| Die Hard           | Duro de matar       |
| Gifted Chirurgeon  | Cirujano dotado     |
| Healer’s Eye       | Ojo del sanador     |
| Impervious Defense | Defensa impermeable |
| Ironhide           | Piel de hierro      |
| Loreseeker         | Buscador de saber   |
| Polymath           | Polímata            |
| Rifter             | Rifter              |
| Rider              | Jinete              |
| Shocking Assault   | Asalto impactante   |
| Specialist         | Especialista        |
| Wanderer           | Errante             |

> Nota: traducir el resto de Focos, Artes y nombres de hechizos de forma
> consistente caso a caso; anotar aquí las nuevas decisiones para mantener la
> uniformidad entre capítulos.
