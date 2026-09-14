# Prompt — Generador de curso: Dibujo para Ingeniería (Moodle 4.3.12)

Prompt autorellenado a partir del PDF del programa de asignatura. Completo, listo
para generar (1) material para GitHub y (2) respaldo Moodle `.mbz` en formato
onetopic (una pestaña/un Libro por unidad, temas como capítulos).

---

```text
Actúa como generador de cursos: a partir del PDF del programa de una asignatura,
genera (1) el material del curso para GitHub y (2) un respaldo Moodle (.mbz) del
curso completo. Versión destino: Moodle 4.3.12, formato "onetopic".

================================================================
CONFIGURACIÓN
================================================================
- PDF del programa: /home/joe/Docs/UTCH/Sep-Dic2026/Dibujo para Ingenieria/DIBUJO_PARA_INGENIERÍA.pdf
- Asignatura: Dibujo para Ingeniería ; clave: E-DI-1 ; siglas: DI
- Duración declarada en el PDF: 45 h totales (15 h Saber + 30 h Saber Hacer; 3 h por semana);
  por unidad: U1 2T/2P=4h; U2 6T/12P=18h; U3 7T/16P=23h.
- Repositorio GitHub destino: joelcf86/DI-UTCH, rama main (sin PDF).
- Curso Moodle: fullname "Dibujo para Ingeniería", shortname "AUDIJCF", idnumber "E-DI-1".
- Identificadores del respaldo (sin colisiones): curso=2002, contextid_curso=20020,
  secciones: general (0)=70101 y unidades 70102..70104; course_module por Libro=
  80101..80103; book_id=2201..2203; contextid de módulos=90101..90103; enrol=25001..25003;
  course_format_options de sección desde 260001 (260001..260020, 5 por sección) y gradebook
  260101..260103; question_category "top" id=23001; capítulos: book 2201 desde 240000,
  2202 desde 240020, 2203 desde 240040; backup_id=md5("DI"+fecha).
- FORMATO DE FACHADA = respaldo real course-107 (DDP, 4.3.12) que restaura OK en la
  plataforma; replicar su estructura al detalle (raíz con completion.xml, grade_history.xml
  y gradebook.xml; questions.xml con categoría "top" con contextid; sección general 0 con
  level 0 y firsttabtext "Índice"; hiddensections=0).
- Sitio de restauración (Moodle 4.3.12, plataforma nueva):
  original_wwwroot https://moodlenuevo.utch.edu.mx  y  original_site_identifier_hash "manual"
  (al restaurar se mostrará aviso de origen distinto; se continúa normalmente).

================================================================
ENTREGABLE 1 — Material del curso para GitHub
================================================================
Genera 4 archivos Markdown en la carpeta "Dibujo para Ingenieria/":
  - Estructura_Dibujo_para_Ingenieria.md :
      · Datos generales (asignatura, clave E-DI-1, cuatrimestre 2, duración 45 h,
        3 h/semana, Lic. en Ingeniería Mecatrónica en Competencias Profesionales,
        vigente Septiembre 2024).
      · Resumen de pestañas: una fila por unidad con su nombre, horas T / P y número
        de temas oficiales.
      · Por unidad: tabla de "temas oficiales" (# | Tema | Saber | Saber hacer) y tabla
        de "contraste" con cada subtema desarrollado (X.Y.Z | Contenido breve).
      · Nota: el curso contiene solo los temas (sin evidencias/prácticas).
  - UnidadN/UnidadN_<nombre>.md (uno por unidad) con EL CONTENIDO COMPLETO de cada
    subtema del programa (definiciones, tablas, pasos guiados de SolidWorks, listas,
    ejemplos). Estructura de encabezados estricta:
        # DIBUJO PARA INGENIERÍA
        ## UNIDAD N. <nombre de la unidad>
        ### Datos generales de la unidad
        ## 1. Temario de la unidad (alineado al programa de la asignatura)   <- tabla oficial
        ## 2. Planeación sugerida del cuatrimestre (Unidad N)
        # TEMA X. <TEMA OFICIAL>
        ## X.Y <subtema desarrollado>        (numeración idéntica a la del PDF)
        ### X.Y.Z ...
    No incluyas secciones de prácticas, ejercicios ni evidencias.
  Crea el repo joelcf86/DI-UTCH si no existe y haz commit + push de los 4 .md (sin PDF).

================================================================
ENTREGABLE 2 — Respaldo Moodle (.mbz) del curso completo, Moodle 4.3.12
================================================================
Genera "Dibujo_para_Ingenieria.mbz" con la fachada de Moodle 4.3.12:

1. moodle_backup.xml (raíz del tar): información con moodle_version 2023100912,
   moodle_release "4.3.12 (Build: 20250414)", backup_version 2023100900, backup_release "4.3",
   original_wwwroot y original_site_identifier_hash según CONFIGURACIÓN,
   original_course_format onetopic; details/detail (type course, format moodle2);
contents con las secciones (1 general (0) + 3 de unidad) y las
    actividades tipo book con su directory; settings: root + una setting por
    sección (section_<id>_included/userinfo) y por módulo (book_<id>_included/userinfo).
2. Por actividad (activities/book_<id>/):
   - module.xml: <module id version="2023100900"> con los campos de 4.3:
     modulename, sectionid, sectionnumber, idnumber, added, score, indent, visible,
     visibleoncoursepage, visibleold, groupmode, groupingid, completion,
     completiongradeitemnumber, completionview, completionexpected, availability,
     showdescription, downloadcontent=0, lang=$@NULL@$, completionpassgrade=0,
     tags (vacío).
   - book.xml: raíz <activity id moduleid modulename contextid> -> <book id>: name,
     intro, introformat=1, numbering, navstyle, customtitles, timecreated,
     timemodified; <chapters> con un <chapter id> por tema/subtema (pagenum
     correlativo desde 1, subchapter=0, title "<X.Y Z>", content=HTML escapado,
     contentformat=1, hidden=0, timemodified, importsrc vacío) y <chaptertags> vacío.
3. course/course.xml: <course id contextid> con el conjunto de campos de 4.3
   (incluye showactivitydates, showcompletionconditions, pdfexportfont=$@NULL@$),
   category (id=9, con <name> y <description>), tags/customfields/courseformatoptions
   de onetopic a nivel curso:
   8 opciones (coursedisplay=0, hiddensections=0, hidetabsbar=0, tabsview=0,
   templatetopic=0, templatetopic_icons=0, usescourseindex=2,
   usessectionsnavigation=0). No incluye duplicateoptions ni opciones por sección
   en course.xml (esas van en section.xml, punto 4).
4. sections/section_<id>/section.xml con availabilityjson
   {"op":"&","c":[],"showc":[]} y course_format_options de onetopic (5 por sección:
   bgcolor, cssstyles, firsttabtext, fontcolor, level). Primera sección = general 0
   (section_70101, number 0, level 0, firsttabtext "Índice", bgcolor #1565C0);
   unidades 70102..70104 (level 1) con bgcolor por unidad: #00897B (U1),
   #6A1B9A (U2), #EF6C00 (U3).
5. course/enrolments.xml: manual (status 0, roleid 5, expirythreshold 86400), guest
   (status 1, roleid 0) y self (status 0, roleid 5, expirythreshold 0, customint1=1,
   customint4=1, customint6=1, customtext1 "Bienvenidos al Curso de Dibujo para
   Ingeniería.", enrolperiod 10368000).
6. roles.xml con role id=5 student (archetype student). En la raíz:
   completion.xml (<course_completion></course_completion>), grade_history.xml y
   gradebook.xml (con grade_category 260101, grade_item 260102 itemtype course y
   grade_setting 260103 minmaxtouse=1) — SÍ se incluyen (formato course-107).
   Auxiliares vacíos (con su tag raíz, nunca auto-cerrados): files.xml, outcomes.xml,
   scales.xml, groups.xml; questions.xml NO vacío: lleva la categoría por defecto
   "top" (id 23001) con contextid=20020, contextlevel 50, contextinstanceid=2002,
   stamp y parent=0 (contextid en questions.xml es requisito del formato course-107).
   En course/: calendar.xml, completiondefaults.xml, competencies.xml,
   filters.xml, roles.xml, contentbank.xml, inforef.xml; por actividad: calendar.xml,
   competencies.xml, filters.xml, inforef.xml, roles.xml, grade_history.xml, grades.xml.
7. .ARCHIVE_INDEX (primera línea "Moodle archive file index. Count: N"; una línea por
   archivo "f" y por directorio "d" con "/" final), moodle_backup.log, tar formato GNU
   (typeflag '0', magic "ustar ", entradas de directorio typeflag '5' sin barra final)
   + gzip. TODOS los XML con declaración EXACTA <?xml version="1.0" encoding="UTF-8"?>
   (comillas dobles) y sin auto-cierre (<a/> -> <a></a>).
8. Los ids del punto de CONFIGURACIÓN.

CONTENIDO de los capítulos (extraído de los .md del Entregable 1):
  - Primer capítulo de cada Libro: "Temario oficial de la unidad" = sección
    "## 1. Temario de la unidad..." del .md.
  - Cada tema X.Y (o X.Y.Z) = la sección "## X.Y..." (incluidas sus ### ), omitiendo
    el encabezado ## y empezando por su primer párrafo/tabla.
  - Markdown a HTML: párrafos en <p>; tablas <table>/<thead>/<tbody>; listas planas
    (solo marcador en columna 0) <ul>/<ol>; blockquotes <blockquote>; <hr>; encabezados
    internos como <h3>/<h4>; código en línea <code>. Los <br> del markdown SIEMPRE como
    <br> reales (nunca escapados).
  - Todo capítulo se envuelve en un contenedor único OSCURO estilo ONEDARK:
    fondo #21252b, texto #abb2bf, borde 1px #181a1f, border-radius 12px, padding 22px 26px;
    encabezado h2 del capítulo en #61afef con subrayado; h3 con acento izquierdo #e5c07b;
    tablas con <th> fondo #2c313a color #e5c07b y filas zebra #1f222a/#282c34;
    blockquote con borde #c678dd; inline <code> fondo #181a1f color #98c379;
    cajas <pre> estilo OneDark: fondo #282c34, color #abb2bf, borde 1px #181a1f,
    border-radius 8px, overflow-x auto, fuente 'Cascadia Code',Consolas,monospace;
    resaltado de sintaxis (fences ```vhdl / ```c / ```python) con: keywords #c678dd,
    tipos #e5c07b, strings #98c379, números #d19a66, comentarios #7f848e,
    funciones #61afef, preprocesador/constantes #e06c75, operadores #abb2bf;
    fences sin idioma: texto plano escapado.
  - El HTML va escapado dentro de <content> (cualidad de texto XML: &lt; &gt; &amp;).

VALIDACIÓN antes de entregar:
  - Abrir el .mbz como tar.gz: primer miembro .ARCHIVE_INDEX con Count coincidente y
    orden idéntico al índice; primeros 200 bytes de moodle_backup.xml detectados como
    formato moodle2 (declaración con comillas dobles + <moodle_backup> + <information>);
    todos los XML bien formados; en moodle_backup.xml las 4 secciones (general + 3
    unidades) y 3 activities; <module> con el conjunto de campos de 4.3; ningún capítulo
    vacío; questions.xml contiene la categoría "top" con contextid; raíz con
    completion.xml, grade_history.xml y gradebook.xml.

ENTREGA: (a) los .md publicados en joelcf86/DI-UTCH, (b)
"Dibujo para Ingenieria/Dibujo_Moodle/Dibujo_para_Ingenieria.mbz" listo para
Restaurar en Moodle 4.3.12 sin tocar nada más.
```