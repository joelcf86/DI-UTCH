#!/usr/bin/env python3
import os, re, time, hashlib, tarfile, io, shutil

BASE = os.path.dirname(os.path.abspath(__file__))
OUT_ROOT = os.path.join(BASE, "Dibujo_Moodle")
MBZ_NAME = "Dibujo_para_Ingenieria.mbz"
TS = int(time.time())
BACKUP_ID = hashlib.md5(("DI" + str(TS)).encode()).hexdigest()

STARTDATE = 1785715200
ENDDATE = STARTDATE + 14 * 7 * 86400

course_id = 2002
course_ctx = 20020
sec_ids = [70101, 70102, 70103, 70104]
sec_num = [0, 1, 2, 3]
mod_ids = [None, 80101, 80102, 80103]
book_ids = [None, 2201, 2202, 2203]
mod_ctxids = [None, 90101, 90102, 90103]
enrol_ids = [25001, 25002, 25003]
chapter_base = [None, 240000, 240020, 240040]
sec_colors = {0: "#1565C0", 1: "#00897B", 2: "#6A1B9A", 3: "#EF6C00"}

WWWROOT = "https://moodlenuevo.utch.edu.mx"
SITE_HASH = "manual"
FULLNAME = "Dibujo para Ingeniería"
SHORTNAME = "AUDIJCF"
IDNUMBER = "E-DI-1"

MOODLE_VERSION = "2023100912"
MOODLE_RELEASE = "4.3.12 (Build: 20250414)"
BACKUP_VERSION = "2023100900"
BACKUP_RELEASE = "4.3"

UNITS = [
    {"num": 1, "name": "Fundamentos de dibujo en ingeniería", "s": 2, "p": 2,
     "md": "Unidad1/Unidad1_Fundamentos_de_dibujo_en_ingenieria.md"},
    {"num": 2, "name": "Dibujo en 2D y 3D Asistido por Computadora", "s": 6, "p": 12,
     "md": "Unidad2/Unidad2_Dibujo_en_2D_y_3D_Asistido_por_Computadora.md"},
    {"num": 3, "name": "Ensambles 3D y elaboración de planos", "s": 7, "p": 16,
     "md": "Unidad3/Unidad3_Ensambles_3D_y_elaboracion_de_planos.md"},
]

XDECL = '<?xml version="1.0" encoding="UTF-8"?>'

MONO = "font-family:'Cascadia Code',Consolas,'JetBrains Mono',monospace"
INLINE_CODE = "background:#181a1f;color:#98c379;padding:2px 6px;border-radius:4px;font-size:.92em"
STRONG = "color:#c678dd;font-weight:600"
EM = "color:#abb2bf;font-style:italic"
LINK = "color:#61afef;text-decoration:none"
H2 = "color:#61afef;font-size:1.4em;line-height:1.3;margin:0 0 6px;padding-bottom:10px;border-bottom:2px solid #3e4451;letter-spacing:.02em"
H3 = "color:#e5c07b;font-size:1.2em;margin:26px 0 10px;padding:7px 12px;background:#23272f;border-left:4px solid #61afef;border-radius:0 8px 8px 0"
H4 = "color:#98c379;font-size:1.08em;margin:22px 0 8px"
P = "margin:10px 0"
TABLE = "width:100%;border-collapse:collapse;margin:16px 0;font-size:.95em;background:#21252b"
TH = "background:#2c313a;color:#e5c07b;font-weight:600;text-align:left;padding:9px 13px;border:1px solid #181a1f"
TD = "padding:8px 13px;border:1px solid #181a1f;vertical-align:top"
TR_A = "background:#23272f"
TR_B = "background:#282c34"
UL = "margin:10px 0;padding-left:26px"
LI = "margin:5px 0"
BQ = "margin:14px 0;padding:12px 16px;background:#23272f;border-left:4px solid #c678dd;border-radius:0 8px 8px 0;font-style:italic"
PRE = "background:#282c34;color:#abb2bf;border:1px solid #181a1f;border-radius:8px;padding:14px 16px;overflow-x:auto;line-height:1.55;font-size:13px"
WRAPPER = ('<div style="background:#21252b;color:#abb2bf;border:1px solid #181a1f;'
           'border-radius:12px;padding:22px 26px;font-family:\'Segoe UI\',system-ui,-apple-system,Arial,sans-serif;'
           'font-size:16px;line-height:1.65;margin:10px 0">')


def esc_text(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def esc_attr(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")

def inline(txt):
    t = txt.replace("<br>", "\x00BR\x00").replace("<br/>", "\x00BR\x00").replace("<br />", "\x00BR\x00")
    t = esc_text(t)
    t = re.sub(r"\[([^\]]+)\]\(([^)]+)\)",
               lambda m: '<a href="%s" style="%s">%s</a>' % (esc_attr(m.group(2)), LINK, m.group(1)), t)
    t = re.sub(r"`([^`]+)`", lambda m: "<code style=\"%s\">%s</code>" % (INLINE_CODE, m.group(1)), t)
    t = re.sub(r"\*\*([^*]+)\*\*", lambda m: "<strong style=\"%s\">%s</strong>" % (STRONG, m.group(1)), t)
    t = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", lambda m: "<em style=\"%s\">%s</em>" % (EM, m.group(1)), t)
    return t.replace("\x00BR\x00", "<br>")

def cell(c):
    return '<td style="%s">%s</td>' % (TD, inline(c))

def render_table(rows):
    out = ["<table style=\"%s\"><thead><tr>" % TABLE]
    for h in rows[0]:
        out.append("<th style=\"%s\">%s</th>" % (TH, inline(h)))
    out.append("</tr></thead><tbody>")
    for i, r in enumerate(rows[1:]):
        bg = TR_A if i % 2 == 0 else TR_B
        out.append("<tr style=\"%s\">%s</tr>" % (bg, "".join(cell(c) for c in r)))
    out.append("</tbody></table>")
    return "".join(out)

def is_table_row(line):
    return line.lstrip().startswith("|") and line.rstrip().endswith("|")

def is_table_sep(line):
    return "-" in line and bool(re.match(r"^\s*\|?[\s:|-]+\|?\s*$", line))

def render_blocks(lines):
    html = []
    par, lst, ol = [], [], []

    def flush_par():
        if par:
            html.append("<p style=\"%s\">%s</p>" % (P, " ".join(inline(x) for x in par)))
            del par[:]

    def flush_list():
        if lst:
            html.append("<ul style=\"%s\">%s</ul>" % (UL, "".join("<li style=\"%s\">%s</li>" % (LI, inline(x[2:].strip())) for x in lst)))
            del lst[:]
        if ol:
            html.append("<ol style=\"%s\">%s</ol>" % (UL, "".join("<li style=\"%s\">%s</li>" % (LI, inline(re.sub(r"^\d+\.\s+", "", x))) for x in ol)))
            del ol[:]

    i, n = 0, len(lines)
    pre = []
    in_pre = False
    while i < n:
        line = lines[i].rstrip()
        s = line.strip()
        if in_pre:
            if s.startswith("```"):
                html.append("<pre style=\"%s\"><code>%s</code></pre>" % (PRE, esc_text("<br>".join(pre))))
                del pre[:]
                in_pre = False
            else:
                pre.append(s)
            i += 1
            continue
        if s.startswith("```"):
            flush_par(); flush_list()
            in_pre = True
            i += 1
            continue
        if not s:
            flush_par(); flush_list()
            i += 1
            continue
        if is_table_row(line):
            flush_par(); flush_list()
            rows = []
            while i < n and is_table_row(lines[i].rstrip()):
                rr = lines[i].strip()
                if is_table_sep(rr):
                    i += 1
                    continue
                rows.append([c.strip() for c in rr.strip("|").split("|")])
                i += 1
            html.append(render_table(rows))
            continue
        if s == "---":
            flush_par(); flush_list()
            html.append("<hr>")
            i += 1
            continue
        if s.startswith("#### "):
            flush_par(); flush_list()
            html.append("<h4 style=\"%s\">%s</h4>" % (H4, inline(s[5:])))
            i += 1
            continue
        if s.startswith("### "):
            flush_par(); flush_list()
            html.append("<h3 style=\"%s\">%s</h3>" % (H3, inline(s[4:])))
            i += 1
            continue
        if s.startswith("> "):
            flush_par(); flush_list()
            q = []
            while i < n and lines[i].rstrip().strip().startswith("> "):
                q.append(lines[i].strip()[2:])
                i += 1
            html.append("<blockquote style=\"%s\">%s</blockquote>" % (BQ, " ".join(inline(x) for x in q)))
            continue
        if s.startswith("- "):
            flush_par(); flush_list()
            while i < n and lines[i].rstrip().strip().startswith("- "):
                lst.append(lines[i].strip())
                i += 1
            flush_list()
            continue
        if re.match(r"^\d+\.\s+", s):
            flush_par(); flush_list()
            while i < n and re.match(r"^\d+\.\s+", lines[i].rstrip().strip()):
                ol.append(lines[i].strip())
                i += 1
            flush_list()
            continue
        if s.startswith("# "):
            i += 1
            continue
        par.append(s)
        i += 1
    flush_par()
    flush_list()
    return "".join(html)

def parse_md(path):
    with open(path, encoding="utf-8") as f:
        lines = f.read().split("\n")
    chapters = []
    cur = None
    for ln in lines:
        s = ln.strip()
        if s.startswith("# TEMA "):
            continue
        if s.startswith("## 1. Temario de la unidad"):
            cur = {"num": None, "title": "Temario oficial de la unidad", "lines": []}
            chapters.append(cur)
            continue
        m = re.match(r"^## (\d+)\.(\d+)\s+(.*)$", s)
        if m:
            cur = {"num": m.group(1) + "." + m.group(2), "title": m.group(3).strip(), "lines": []}
            chapters.append(cur)
            continue
        if s.startswith("## "):
            cur = None
            continue
        if cur is not None:
            cur["lines"].append(ln)
    return chapters

def build_book_xml(unit):
    n = unit["num"]
    path = os.path.join(BASE, unit["md"])
    pagenum = 1
    chs = []
    for c in parse_md(path):
        body = render_blocks(c["lines"])
        html = WRAPPER + '<h2 style="%s">%s</h2>' % (H2, esc_text(c["title"])) + body + "</div>"
        cid = chapter_base[n] + (pagenum - 1)
        chs.append(
            "      <chapter id=\"%d\">\n"
            "        <pagenum>%d</pagenum>\n"
            "        <subchapter>0</subchapter>\n"
            "        <title>%s</title>\n"
            "        <content>%s</content>\n"
            "        <contentformat>1</contentformat>\n"
            "        <hidden>0</hidden>\n"
            "        <timemodified>%d</timemodified>\n"
            "        <importsrc></importsrc>\n"
            "      </chapter>"
            % (cid, pagenum, esc_text(c["title"]), esc_text(html), TS))
        pagenum += 1
    intro = ("<p><strong>Unidad %d. %s</strong></p><p>Horas: %d h de teoría + %d h de práctica. "
             "En esta unidad el Libro contiene primero el <em>temario oficial</em> de la unidad "
             "y después un capítulo por cada tema desarrollado.</p>"
             % (n, unit["name"], unit["s"], unit["p"]))
    book = (
        "<book id=\"%d\">\n"
        "  <name>%s</name>\n"
        "  <intro>%s</intro>\n"
        "  <introformat>1</introformat>\n"
        "  <numbering>1</numbering>\n"
        "  <navstyle>1</navstyle>\n"
        "  <customtitles>0</customtitles>\n"
        "  <timecreated>%d</timecreated>\n"
        "  <timemodified>%d</timemodified>\n"
        "  <chapters>\n%s\n  </chapters>\n"
        "  <chaptertags>\n  </chaptertags>\n"
        "</book>"
        % (book_ids[n], esc_text("U%d. %s" % (n, unit["name"])), esc_text(intro), TS, TS, "\n".join(chs)))
    return ("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
            "<activity id=\"%d\" moduleid=\"%d\" modulename=\"book\" contextid=\"%d\">\n%s</activity>"
            % (book_ids[n], mod_ids[n], mod_ctxids[n], book))

def build_module_xml(n):
    fields = [
        "<modulename>book</modulename>",
        "<sectionid>%d</sectionid>" % sec_ids[n],
        "<sectionnumber>%d</sectionnumber>" % n,
        "<idnumber></idnumber>",
        "<added>%d</added>" % TS,
        "<score>0</score>",
        "<indent>0</indent>",
        "<visible>1</visible>",
        "<visibleoncoursepage>1</visibleoncoursepage>",
        "<visibleold>1</visibleold>",
        "<groupmode>0</groupmode>",
        "<groupingid>0</groupingid>",
        "<completion>0</completion>",
        "<completiongradeitemnumber>$@NULL@$</completiongradeitemnumber>",
        "<completionpassgrade>0</completionpassgrade>",
        "<completionview>0</completionview>",
        "<completionexpected>0</completionexpected>",
        "<availability>$@NULL@$</availability>",
        "<showdescription>0</showdescription>",
        "<downloadcontent>1</downloadcontent>",
        "<lang>$@NULL@$</lang>",
        "<tags>\n  </tags>",
    ]
    return ("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
            "<module id=\"%d\" version=\"2023100900\">\n%s\n</module>"
            % (mod_ids[n], "\n".join(fields)))

def build_course_xml():
    opts = []
    gen = [("coursedisplay", "0"), ("hiddensections", "0"), ("hidetabsbar", "0"),
           ("tabsview", "0"), ("templatetopic", "0"), ("templatetopic_icons", "0"),
           ("usescourseindex", "2"), ("usessectionsnavigation", "0")]
    for nm, v in gen:
        opts.append("    <courseformatoption>\n      <format>onetopic</format>\n      <sectionid>0</sectionid>\n"
                    "      <name>%s</name>\n      <value>%s</value>\n    </courseformatoption>" % (nm, v))
    summary = ("<h2>Dibujo para Ingeniería</h2><p>Curso del Área de Mecatrónica: fundamentos del dibujo "
               "técnico, modelado 2D/3D asistido por computadora y elaboración de planos normalizados.</p>"
               "<p><strong>Unidades:</strong> 3 | <strong>Duración:</strong> 45 h (15 teoría + 30 práctica).</p>"
               "<p><strong>Software:</strong> SolidWorks (CAD de referencia).</p>")
    lines = [
        "<shortname>%s</shortname>" % SHORTNAME,
        "<fullname>%s</fullname>" % FULLNAME,
        "<idnumber>%s</idnumber>" % IDNUMBER,
        "<summary>%s</summary>" % esc_text(summary),
        "<summaryformat>1</summaryformat>",
        "<format>onetopic</format>",
        "<showgrades>1</showgrades>",
        "<newsitems>5</newsitems>",
        "<startdate>%d</startdate>" % STARTDATE,
        "<enddate>%d</enddate>" % ENDDATE,
        "<marker>0</marker>",
        "<maxbytes>20971520</maxbytes>",
        "<legacyfiles>0</legacyfiles>",
        "<showreports>0</showreports>",
        "<visible>1</visible>",
        "<groupmode>0</groupmode>",
        "<groupmodeforce>0</groupmodeforce>",
        "<defaultgroupingid>0</defaultgroupingid>",
        "<lang></lang>",
        "<theme></theme>",
        "<timecreated>%d</timecreated>" % TS,
        "<timemodified>%d</timemodified>" % TS,
        "<requested>0</requested>",
        "<showactivitydates>0</showactivitydates>",
        "<showcompletionconditions>1</showcompletionconditions>",
        "<pdfexportfont>$@NULL@$</pdfexportfont>",
        "<enablecompletion>1</enablecompletion>",
        "<completionnotify>0</completionnotify>",
        "<category id=\"9\">\n    <name>Formación tecnológica</name>\n    <description></description>\n  </category>",
        "<tags>\n  </tags>",
        "<customfields>\n  </customfields>",
        "<courseformatoptions>\n%s\n  </courseformatoptions>" % "\n".join(opts),
    ]
    return ("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
            "<course id=\"%d\" contextid=\"%d\">\n%s\n</course>" % (course_id, course_ctx, "\n".join(lines)))

def build_section_xml(si):
    name = "DIBUJO PARA INGENIERÍA" if si == 0 else "U%d. %s" % (si, UNITS[si - 1]["name"].upper())
    seq = "" if si == 0 else "%d" % mod_ids[si]
    summary = "" if si == 0 else ""
    if si == 0:
        summary = '&lt;h3 style="text-align: center;"&gt;&lt;br&gt;&lt;/h3&gt;'
    opts = []
    for k, nm in enumerate(("bgcolor", "cssstyles", "firsttabtext", "fontcolor", "level")):
        if nm == "bgcolor":
            v = sec_colors[si]
        elif nm == "cssstyles":
            v = ""
        elif nm == "firsttabtext":
            v = "Índice"
        elif nm == "fontcolor":
            v = "#FFF"
        else:
            v = "0" if si == 0 else "1"
        oid = 260000 + si * 5 + k + 1
        opts.append("  <course_format_options id=\"%d\">\n    <format>onetopic</format>\n    <name>%s</name>\n"
                    "    <value>%s</value>\n  </course_format_options>" % (oid, nm, v))
    fields = [
        "<number>%d</number>" % sec_num[si],
        "<name>%s</name>" % name,
        "<summary>%s</summary>" % summary,
        "<summaryformat>1</summaryformat>",
        "<sequence>%s</sequence>" % seq,
        "<visible>1</visible>",
        '<availabilityjson>{"op":"&amp;","c":[],"showc":[]}</availabilityjson>',
        "<timemodified>%d</timemodified>" % TS,
        "\n".join(opts),
    ]
    return "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<section id=\"%d\">\n%s\n</section>" % (sec_ids[si], "\n".join(fields))

def build_enrolment(eid, etype, status, roleid, threshold, customints, name, password, customtext1="$@NULL@$", enrolperiod=0):
    rows = [
        "<enrol>%s</enrol>" % etype,
        "<status>%d</status>" % status,
        "<name>%s</name>" % name,
        "<enrolperiod>%d</enrolperiod>" % enrolperiod,
        "<enrolstartdate>0</enrolstartdate>",
        "<enrolenddate>0</enrolenddate>",
        "<expirynotify>0</expirynotify>",
        "<expirythreshold>%d</expirythreshold>" % threshold,
        "<notifyall>0</notifyall>",
        "<password>%s</password>" % password,
        "<cost>$@NULL@$</cost>",
        "<currency>$@NULL@$</currency>",
        "<roleid>%d</roleid>" % roleid,
    ]
    for i in range(1, 9):
        if customints is not None and i in customints:
            v = customints[i]
        elif customints is None:
            v = "$@NULL@$"
        elif i in (1, 2, 3, 4, 5, 6):
            v = "0"
        else:
            v = "$@NULL@$"
        rows.append("<customint%d>%s</customint%d>" % (i, v, i))
    for i in range(1, 4):
        rows.append("<customchar%d>$@NULL@$</customchar%d>" % (i, i))
    rows.append("<customdec1>$@NULL@$</customdec1>")
    rows.append("<customdec2>$@NULL@$</customdec2>")
    for i in range(1, 5):
        v = customtext1 if i == 1 else "$@NULL@$"
        rows.append("<customtext%d>%s</customtext%d>" % (i, v, i))
    rows.append("<timecreated>%d</timecreated>" % TS)
    rows.append("<timemodified>%d</timemodified>" % TS)
    rows.append("<user_enrolments>\n    </user_enrolments>")
    return "    <enrol id=\"%d\">\n%s\n    </enrol>" % (eid, "\n".join(rows))

def build_enrolments_xml():
    manual = build_enrolment(enrol_ids[0], "manual", 0, 5, 86400, None, name="$@NULL@$", password="$@NULL@$")
    guest = build_enrolment(enrol_ids[1], "guest", 1, 0, 0, None, name="$@NULL@$", password="")
    selfe = build_enrolment(enrol_ids[2], "self", 0, 5, 0,
                            {1: "1", 2: "0", 3: "0", 4: "1", 5: "0", 6: "1"},
                            name="", password="$@NULL@$",
                            customtext1="Bienvenidos al Curso de Dibujo para Ingeniería.", enrolperiod=10368000)
    return ("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<enrolments>\n  <enrols>\n%s\n%s\n%s\n"
            "  </enrols>\n</enrolments>" % (manual, guest, selfe))

def build_roles_definition_xml():
    inner = ('  <role id="5">\n    <name></name>\n    <shortname>student</shortname>\n'
             "    <nameincourse>$@NULL@$</nameincourse>\n    <description></description>\n"
             "    <sortorder>5</sortorder>\n    <archetype>student</archetype>\n  </role>")
    return "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<roles_definition>\n%s\n</roles_definition>" % inner

def build_roles_xml():
    return ("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<roles>\n  <role_overrides>\n  </role_overrides>\n"
            "  <role_assignments>\n  </role_assignments>\n</roles>")

def aux(tag, inner=""):
    return "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<%s>%s</%s>" % (tag, inner, tag)

def build_groups_xml():
    return ("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<groups>\n"
            "  <groupcustomfields>\n  </groupcustomfields>\n"
            "  <groupings>\n    <groupingcustomfields>\n    </groupingcustomfields>\n  </groupings>\n</groups>")

def build_course_inforef():
    return aux("inforef",
               "\n  <groupref>\n  </groupref>\n  <roleref>\n    <role>\n      <id>5</id>\n    </role>\n  </roleref>\n"
               "  <question_categoryref>\n  </question_categoryref>")

def build_gradebook_xml():
    inner = (
        "  <attributes>\n  </attributes>\n"
        "  <grade_categories>\n"
        "    <grade_category id=\"260101\">\n"
        "      <parent>$@NULL@$</parent>\n"
        "      <depth>1</depth>\n"
        "      <path>/260101/</path>\n"
        "      <fullname>?</fullname>\n"
        "      <aggregation>13</aggregation>\n"
        "      <keephigh>0</keephigh>\n"
        "      <droplow>0</droplow>\n"
        "      <aggregateonlygraded>1</aggregateonlygraded>\n"
        "      <aggregateoutcomes>0</aggregateoutcomes>\n"
        "      <timecreated>%d</timecreated>\n"
        "      <timemodified>%d</timemodified>\n"
        "      <hidden>0</hidden>\n"
        "    </grade_category>\n"
        "  </grade_categories>\n"
        "  <grade_items>\n"
        "    <grade_item id=\"260102\">\n"
        "      <categoryid>$@NULL@$</categoryid>\n"
        "      <itemname>$@NULL@$</itemname>\n"
        "      <itemtype>course</itemtype>\n"
        "      <itemmodule>$@NULL@$</itemmodule>\n"
        "      <iteminstance>260101</iteminstance>\n"
        "      <itemnumber>$@NULL@$</itemnumber>\n"
        "      <iteminfo>$@NULL@$</iteminfo>\n"
        "      <idnumber>$@NULL@$</idnumber>\n"
        "      <calculation>$@NULL@$</calculation>\n"
        "      <gradetype>1</gradetype>\n"
        "      <grademax>0.00000</grademax>\n"
        "      <grademin>0.00000</grademin>\n"
        "      <scaleid>$@NULL@$</scaleid>\n"
        "      <outcomeid>$@NULL@$</outcomeid>\n"
        "      <gradepass>0.00000</gradepass>\n"
        "      <multfactor>1.00000</multfactor>\n"
        "      <plusfactor>0.00000</plusfactor>\n"
        "      <aggregationcoef>0.00000</aggregationcoef>\n"
        "      <aggregationcoef2>0.00000</aggregationcoef2>\n"
        "      <weightoverride>0</weightoverride>\n"
        "      <sortorder>1</sortorder>\n"
        "      <display>0</display>\n"
        "      <decimals>$@NULL@$</decimals>\n"
        "      <hidden>0</hidden>\n"
        "      <locked>0</locked>\n"
        "      <locktime>0</locktime>\n"
        "      <needsupdate>0</needsupdate>\n"
        "      <timecreated>%d</timecreated>\n"
        "      <timemodified>%d</timemodified>\n"
        "      <grade_grades>\n      </grade_grades>\n"
        "    </grade_item>\n"
        "  </grade_items>\n"
        "  <grade_letters>\n  </grade_letters>\n"
        "  <grade_settings>\n"
        "    <grade_setting id=\"260103\">\n"
        "      <name>minmaxtouse</name>\n"
        "      <value>1</value>\n"
        "    </grade_setting>\n"
        "  </grade_settings>"
        % (TS, TS, TS, TS))
    return "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<gradebook>\n%s\n</gradebook>" % inner

def build_moodle_backup_xml():
    acts = []
    for n in (1, 2, 3):
        acts.append(
            "        <activity>\n          <moduleid>%d</moduleid>\n          <sectionid>%d</sectionid>\n"
            "          <modulename>book</modulename>\n          <title>%s</title>\n"
            "          <directory>activities/book_%d</directory>\n        </activity>"
            % (mod_ids[n], sec_ids[n], esc_text("U%d. %s" % (n, UNITS[n - 1]["name"])), mod_ids[n]))
    secs = []
    for si in range(4):
        if si == 0:
            title = "DIBUJO PARA INGENIERÍA"
        else:
            title = "U%d. %s" % (si, UNITS[si - 1]["name"])
        secs.append("        <section>\n          <sectionid>%d</sectionid>\n"
                    "          <title>%s</title>\n          <directory>sections/section_%d</directory>\n"
                    "        </section>" % (sec_ids[si], esc_text(title), sec_ids[si]))
    root_settings = [
        ("filename", MBZ_NAME), ("imscc11", "0"), ("users", "0"), ("anonymize", "0"),
        ("role_assignments", "0"), ("activities", "1"), ("blocks", "1"), ("files", "1"),
        ("filters", "1"), ("comments", "0"), ("badges", "0"), ("calendarevents", "1"),
        ("userscompletion", "0"), ("logs", "0"), ("grade_histories", "0"), ("questionbank", "1"),
        ("groups", "1"), ("competencies", "1"), ("customfield", "1"), ("contentbankcontent", "1"),
        ("xapistate", "0"), ("legacyfiles", "1"),
    ]
    settings = []
    for nm, v in root_settings:
        settings.append('      <setting>\n        <level>root</level>\n        <name>%s</name>\n'
                        "        <value>%s</value>\n      </setting>" % (nm, v))
    for si in range(4):
        sd = "section_%d" % sec_ids[si]
        settings.append('      <setting>\n        <level>section</level>\n        <section>%s</section>\n'
                        "        <name>%s_included</name>\n        <value>1</value>\n      </setting>" % (sd, sd))
        settings.append('      <setting>\n        <level>section</level>\n        <section>%s</section>\n'
                        "        <name>%s_userinfo</name>\n        <value>0</value>\n      </setting>" % (sd, sd))
    for n in (1, 2, 3):
        ad = "book_%d" % mod_ids[n]
        settings.append('      <setting>\n        <level>activity</level>\n        <activity>%s</activity>\n'
                        "        <name>%s_included</name>\n        <value>1</value>\n      </setting>" % (ad, ad))
        settings.append('      <setting>\n        <level>activity</level>\n        <activity>%s</activity>\n'
                        "        <name>%s_userinfo</name>\n        <value>0</value>\n      </setting>" % (ad, ad))
    info = "\n".join([
        "<name>%s</name>" % MBZ_NAME,
        "<moodle_version>%s</moodle_version>" % MOODLE_VERSION,
        "<moodle_release>%s</moodle_release>" % MOODLE_RELEASE,
        "<backup_version>%s</backup_version>" % BACKUP_VERSION,
        "<backup_release>%s</backup_release>" % BACKUP_RELEASE,
        "<backup_date>%d</backup_date>" % TS,
        "<mnet_remoteusers>0</mnet_remoteusers>",
        "<include_files>1</include_files>",
        "<include_file_references_to_external_content>0</include_file_references_to_external_content>",
        "<original_wwwroot>%s</original_wwwroot>" % WWWROOT,
        "<original_site_identifier_hash>%s</original_site_identifier_hash>" % SITE_HASH,
        "<original_course_id>%d</original_course_id>" % course_id,
        "<original_course_format>onetopic</original_course_format>",
        "<original_course_fullname>%s</original_course_fullname>" % FULLNAME,
        "<original_course_shortname>%s</original_course_shortname>" % SHORTNAME,
        "<original_course_startdate>%d</original_course_startdate>" % STARTDATE,
        "<original_course_enddate>%d</original_course_enddate>" % ENDDATE,
        "<original_course_contextid>%d</original_course_contextid>" % course_ctx,
        "<original_system_contextid>1</original_system_contextid>",
    ])
    detail = ('    <detail backup_id="%s">\n      <type>course</type>\n      <format>moodle2</format>\n'
              "      <interactive>1</interactive>\n      <mode>10</mode>\n      <execution>1</execution>\n"
              "      <executiontime>0</executiontime>\n    </detail>" % BACKUP_ID)
    contents = ("    <activities>\n%s\n    </activities>\n    <sections>\n%s\n    </sections>\n"
                "    <course>\n      <courseid>%d</courseid>\n      <title>%s</title>\n"
                "      <directory>course</directory>\n    </course>"
                % ("\n".join(acts), "\n".join(secs), course_id, SHORTNAME))
    return ("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<moodle_backup>\n  <information>\n%s\n  </information>\n"
            "  <details>\n%s\n  </details>\n  <contents>\n%s\n  </contents>\n"
            "  <settings>\n%s\n  </settings>\n</moodle_backup>"
            % (info, detail, contents, "\n".join(settings)))

def build_completion_xml():
    return "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<course_completion>\n</course_completion>"

def build_grade_history_xml():
    return "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<grade_history>\n  <grade_grades>\n  </grade_grades>\n</grade_history>"

def main():
    books = {}
    for n in (1, 2, 3):
        books[n] = build_book_xml(UNITS[n - 1])

    files = {}
    # Orden exacto del respaldo real 4.3.12: grade_history, module, activity, competencies, calendar, inforef, grades, roles, filters
    ACT_FILES = ["grade_history.xml", "module.xml", "book.xml", "competencies.xml",
                 "calendar.xml", "inforef.xml", "grades.xml", "roles.xml", "filters.xml"]
    for n in (1, 2, 3):
        d = "activities/book_%d" % mod_ids[n]
        files[d + "/grade_history.xml"] = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<grade_history>\n  <grade_grades>\n  </grade_grades>\n</grade_history>"
        files[d + "/module.xml"] = build_module_xml(n)
        files[d + "/book.xml"] = books[n]
        files[d + "/competencies.xml"] = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<course_module_competencies>\n  <competencies>\n  </competencies>\n</course_module_competencies>"
        files[d + "/calendar.xml"] = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<events>\n</events>"
        files[d + "/inforef.xml"] = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<inforef>\n</inforef>"
        files[d + "/grades.xml"] = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<activity_gradebook>\n  <grade_items>\n  </grade_items>\n  <grade_letters>\n  </grade_letters>\n</activity_gradebook>"
        files[d + "/roles.xml"] = build_roles_xml()
        files[d + "/filters.xml"] = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<filters>\n  <filter_actives>\n  </filter_actives>\n  <filter_configs>\n  </filter_configs>\n</filters>"

    course_files = [
        ("course.xml", build_course_xml()),
        ("enrolments.xml", build_enrolments_xml()),
        ("competencies.xml", "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<course_competencies>\n  <competencies>\n  </competencies>\n  <user_competencies>\n  </user_competencies>\n</course_competencies>"),
        ("calendar.xml", "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<events>\n</events>"),
        ("inforef.xml", build_course_inforef()),
        ("contentbank.xml", "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<contents>\n</contents>"),
        ("roles.xml", build_roles_xml()),
        ("completiondefaults.xml", "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<course_completion_defaults>\n</course_completion_defaults>"),
        ("filters.xml", "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<filters>\n  <filter_actives>\n  </filter_actives>\n  <filter_configs>\n  </filter_configs>\n</filters>"),
    ]

    if os.path.exists(OUT_ROOT):
        shutil.rmtree(OUT_ROOT)
    os.makedirs(OUT_ROOT)

    order = [("activities", True)]
    for n in (1, 2, 3):
        d = "activities/book_%d" % mod_ids[n]
        order.append((d, True))
        for name in ACT_FILES:
            order.append((d + "/" + name, False))
    order.append(("completion.xml", False))
    files["completion.xml"] = build_completion_xml()
    order.append(("course", True))
    for name, content in course_files:
        files["course/" + name] = content
        order.append(("course/" + name, False))
    for name in ["files.xml", "grade_history.xml", "gradebook.xml", "groups.xml",
                 "moodle_backup.xml", "outcomes.xml", "questions.xml", "roles.xml", "scales.xml"]:
        order.append((name, False))
    files["files.xml"] = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<files>\n</files>"
    files["grade_history.xml"] = build_grade_history_xml()
    files["gradebook.xml"] = build_gradebook_xml()
    files["groups.xml"] = build_groups_xml()
    files["moodle_backup.xml"] = build_moodle_backup_xml()
    files["outcomes.xml"] = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<outcomes_definition>\n</outcomes_definition>"
    files["questions.xml"] = ("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
                              "<question_categories>\n"
                              "  <question_category id=\"23001\">\n"
                              "    <name>top</name>\n"
                              "    <contextid>%d</contextid>\n"
                              "    <contextlevel>50</contextlevel>\n"
                              "    <contextinstanceid>%d</contextinstanceid>\n"
                              "    <info></info>\n"
                              "    <infoformat>0</infoformat>\n"
                              "    <stamp>moodlenuevo.utch.edu.mx+260901000000+manual</stamp>\n"
                              "    <parent>0</parent>\n"
                              "    <sortorder>0</sortorder>\n"
                              "    <idnumber>$@NULL@$</idnumber>\n"
                              "    <question_bank_entries>\n"
                              "    </question_bank_entries>\n"
                              "  </question_category>\n"
                              "</question_categories>") % (course_ctx, course_id)
    files["roles.xml"] = build_roles_definition_xml()
    files["scales.xml"] = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<scales_definition>\n</scales_definition>"
    order.append(("sections", True))
    for si in range(4):
        d = "sections/section_%d" % sec_ids[si]
        order.append((d, True))
        files[d + "/inforef.xml"] = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<inforef>\n</inforef>"
        files[d + "/section.xml"] = build_section_xml(si)
        order.append((d + "/inforef.xml", False))
        order.append((d + "/section.xml", False))
    files["moodle_backup.log"] = ""
    order.append(("moodle_backup.log", False))

    index_lines = ["Moodle archive file index. Count: %d" % len(order)]
    for path, is_dir in order:
        if is_dir:
            index_lines.append("%s/\td\t0\t?" % path)
        else:
            data = files[path].encode("utf-8")
            index_lines.append("%s\tf\t%d\t%d" % (path, len(data), TS))
    index_data = ("\n".join(index_lines) + "\n").encode("utf-8")

    mbz_path = os.path.join(OUT_ROOT, MBZ_NAME)
    with tarfile.open(mbz_path, "w:gz", format=tarfile.GNU_FORMAT) as tar:
        def add_dir(path):
            ti = tarfile.TarInfo(path)
            ti.type = tarfile.DIRTYPE
            ti.mtime = TS
            ti.mode = 0o755
            ti.uid = 0
            ti.gid = 0
            tar.addfile(ti)

        def add_file(path, data):
            ti = tarfile.TarInfo(path)
            ti.size = len(data)
            ti.mtime = TS
            ti.mode = 0o644
            ti.uid = 0
            ti.gid = 0
            tar.addfile(ti, io.BytesIO(data))

        add_file(".ARCHIVE_INDEX", index_data)
        for path, is_dir in order:
            if is_dir:
                add_dir(path)
            else:
                add_file(path, files[path].encode("utf-8"))

    for n in (1, 2, 3):
        print("book_%d chapters: %d | book.xml bytes: %d"
              % (mod_ids[n], len(re.findall(r"<chapter id=", books[n])), len(books[n].encode("utf-8"))))
    print("Count entries:", len(order))
    print("mbz bytes:", os.path.getsize(mbz_path))
    print("mbz path:", mbz_path)

main()