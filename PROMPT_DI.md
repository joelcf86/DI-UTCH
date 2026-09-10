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
  registrar secciones: general=70101, unidades 70102..70104; course_module por Libro=
  80101..80103; book_id=2201..2203; contextid de módulos=90101..90103; enrol=25001..25003;
  course_format_options desde 260001; capítulos: book 2201 desde 240000, 2202 desde 240020,
  2203 desde 240040; backup_id=md5("DI"+fecha).
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

1. moodle_backup.xml (raíz del tar): información con moodle_version 2023100900.12,
   moodle_release "4.3.12", backup_version 2023100900, backup_release "4.3",
   original_wwwroot y original_site_identifier_hash según CONFIGURACIÓN,
   original_course_format onetopic; details/detail (type course, format moodle2);
   contents con las secciones (general + 3 de unidad) y las actividades tipo book
   con su directory; settings: root + una setting por sección
   (section_<id>_included/userinfo) y por módulo (book_<id>_included/userinfo).
2. Por actividad (activities/book_<id>/):
   - module.xml: <module id version="2023100900"> con los campos de 4.3:
     modulename, sectionid, sectionnumber, idnumber, added, score, indent, visible,
     visibleoncoursepage, visibleold, groupmode, groupingid, completion,
     completiongradeitemnumber, completionview, completionexpected, availability,
     showdescription, downloadcontent=0, lang (vacío), completionpassgrade=0,
     tags (vacío).
   - book.xml: raíz <activity id moduleid modulename contextid> -> <book id>: name,
     intro, introformat=1, numbering, navstyle, customtitles, timecreated,
     timemodified; <chapters> con un <chapter id> por tema/subtema (pagenum
     correlativo desde 1, subchapter=0, title "<X.Y Z>", content=HTML escapado,
     contentformat=1, hidden=0, timemodified, importsrc vacío) y <chaptertags> vacío.
3. course/course.xml: <course id contextid> con el conjunto de campos de 4.3
   (incluye showactivitydates, showcompletionconditions, pdfexportfont vacío,
   duplicateoptions "{}"), category, tags/customfields/courseformatoptions de
   onetopic: 6 opciones para la sección general (coursedisplay=0, hiddensections=1,
   hidetabsbar=0, tabsview=0, templatetopic=0, templatetopic_icons=0) y por sección
   de unidad: bgcolor, cssstyles, firsttabtext=Índice, fontcolor, level=0.
4. sections/section_<id>/section.xml con availabilityjson
   {"op":"&","c":[],"showc":[]} y course_format_options de onetopic (5 por sección
   de unidad), igual que en el punto 3.
5. course/enrolments.xml: manual (status 0, roleid 5, expirythreshold 86400), guest
   (status 1, roleid 0) y self (status 0, roleid 5, customint4=1, customint6=1).
6. roles.xml con role id=5 student (archetype student). Auxiliares vacíos (con su tag
   raíz, nunca auto-cerrados): files.xml, questions.xml, completion.xml, outcomes.xml,
   scales.xml, grade_history.xml, gradebook.xml, groups.xml; y en course/: calendar.xml,
   completiondefaults.xml, competencies.xml, filters.xml, roles.xml, contentbank.xml,
   inforef.xml; por actividad: calendar.xml, competencies.xml, filters.xml, inforef.xml,
   roles.xml, grade_history.xml, grades.xml.
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
    todos los XML bien formados; en moodle_backup.xml las 4 secciones y 3 activities;
    <module> con el conjunto de campos de 4.3; ningún capítulo vacío.

ENTREGA: (a) los .md publicados en joelcf86/DI-UTCH, (b)
"Dibujo para Ingenieria/Dibujo_Moodle/Dibujo_para_Ingenieria.mbz" listo para
Restaurar en Moodle 4.3.12 sin tocar nada más.
```