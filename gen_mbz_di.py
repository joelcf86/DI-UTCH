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
sec_general = 70101
sec_ids = [None, 70102, 70103, 70104]
mod_ids = [None, 80101, 80102, 80103]
book_ids = [None, 2201, 2202, 2203]
mod_ctxids = [None, 90101, 90102, 90103]
enrol_ids = [25001, 25002, 25003]
chapter_base = [None, 240000, 240020, 240040]

WWWROOT = "https://moodlenuevo.utch.edu.mx"
SITE_HASH = "manual"
FULLNAME = "Dibujo para Ingeniería"
SHORTNAME = "AUDIJCF"
IDNUMBER = "E-DI-1"

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
            "  <chapter id=\"%d\">\n<pagenum>%d</pagenum>\n<subchapter>0</subchapter>\n"
            "<title>%s</title>\n<content>%s</content>\n<contentformat>1</contentformat>\n"
            "<hidden>0</hidden>\n<timemodified>%d</timemodified>\n<importsrc></importsrc>\n  </chapter>"
            % (cid, pagenum, esc_text(c["title"]), esc_text(html), TS))
        pagenum += 1
    intro = ("<p><strong>Unidad %d. %s</strong></p><p>Horas: %d h de teoría + %d h de práctica. "
             "En esta unidad el Libro contiene primero el <em>temario oficial</em> de la unidad "
             "y después un capítulo por cada tema desarrollado.</p>"
             % (n, unit["name"], unit["s"], unit["p"]))
    book = ("<book id=\"%d\">\n<name>%s</name>\n<intro>%s</intro>\n<introformat>1</introformat>\n"
            "<numbering>1</numbering>\n<navstyle>1</navstyle>\n<customtitles>0</customtitles>\n"
            "<timecreated>%d</timecreated>\n<timemodified>%d</timemodified>\n<chapters>\n%s\n</chapters>\n</book>"
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
        "<completionview>0</completionview>",
        "<completionpassgrade>0</completionpassgrade>",
        "<completionexpected>0</completionexpected>",
        "<availability>$@NULL@$</availability>",
        "<showdescription>0</showdescription>",
        "<downloadcontent>0</downloadcontent>",
        "<lang></lang>",
        "<tags></tags>",
    ]
    return ("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
            "<module id=\"%d\" version=\"2023100900\">\n%s\n</module>"
            % (mod_ids[n], "\n".join(fields)))

def build_course_xml():
    opts = []
    gen_names = ["coursedisplay", "hiddensections", "hidetabsbar", "tabsview", "templatetopic", "templatetopic_icons"]
    gen_vals = ["0", "1", "0", "0", "0", "0"]
    for nm, v in zip(gen_names, gen_vals):
        opts.append("    <courseformatoption>\n      <format>onetopic</format>\n      <sectionid>0</sectionid>\n"
                    "      <name>%s</name>\n      <value>%s</value>\n    </courseformatoption>" % (nm, v))
    for n in (1, 2, 3):
        for nm in ("bgcolor", "cssstyles", "firsttabtext", "fontcolor", "level"):
            v = "Índice" if nm == "firsttabtext" else ("0" if nm == "level" else "")
            opts.append("    <courseformatoption>\n      <format>onetopic</format>\n      <sectionid>%d</sectionid>\n"
                        "      <name>%s</name>\n      <value>%s</value>\n    </courseformatoption>"
                        % (sec_ids[n], nm, v))
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
        "<newsitems>0</newsitems>",
        "<startdate>%d</startdate>" % STARTDATE,
        "<enddate>%d</enddate>" % ENDDATE,
        "<marker>0</marker>",
        "<maxbytes>0</maxbytes>",
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
        "<showactivitydates>1</showactivitydates>",
        "<showcompletionconditions>1</showcompletionconditions>",
        "<enablecompletion>1</enablecompletion>",
        "<completionnotify>0</completionnotify>",
        "<pdfexportfont></pdfexportfont>",
        "<duplicateoptions>{}</duplicateoptions>",
        "<category id=\"9\">\n<name>Formación tecnológica</name>\n<description></description>\n</category>",
        "<tags></tags>",
        "<customfields></customfields>",
        "<courseformatoptions>\n%s\n  </courseformatoptions>" % "\n".join(opts),
    ]
    return ("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
            "<course id=\"%d\" contextid=\"%d\">\n%s\n</course>" % (course_id, course_ctx, "\n".join(lines)))

def build_section_xml(n):
    opts = []
    for k, nm in enumerate(("bgcolor", "cssstyles", "firsttabtext", "fontcolor", "level")):
        v = "Índice" if nm == "firsttabtext" else ("0" if nm == "level" else "")
        oid = 260000 + (n - 1) * 5 + 7 + k
        opts.append("  <course_format_options id=\"%d\">\n    <format>onetopic</format>\n    <name>%s</name>\n"
                    "    <value>%s</value>\n  </course_format_options>" % (oid, nm, v))
    fields = [
        "<number>%d</number>" % n,
        "<name>%d. %s</name>" % (n, UNITS[n - 1]["name"]),
        "<summary></summary>",
        "<summaryformat>1</summaryformat>",
        "<sequence>%d</sequence>" % mod_ids[n],
        "<visible>1</visible>",
        '<availabilityjson>{"op":"&amp;","c":[],"showc":[]}</availabilityjson>',
        "<timemodified>%d</timemodified>" % TS,
        "\n".join(opts),
    ]
    return "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<section id=\"%d\">\n%s\n</section>" % (sec_ids[n], "\n".join(fields))

def build_section_general_xml():
    fields = [
        "<number>0</number>",
        "<name>$@NULL@$</name>",
        "<summary></summary>",
        "<summaryformat>1</summaryformat>",
        "<sequence></sequence>",
        "<visible>1</visible>",
        "<availabilityjson>$@NULL@$</availabilityjson>",
        "<timemodified>%d</timemodified>" % TS,
    ]
    return "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<section id=\"%d\">\n%s\n</section>" % (sec_general, "\n".join(fields))

def build_enrolment(eid, etype, status, roleid, threshold, custom4, custom6, password="$@NULL@$"):
    rows = [
        "<enrol>%s</enrol>" % etype,
        "<status>%d</status>" % status,
        "<name>$@NULL@$</name>",
        "<enrolperiod>0</enrolperiod>",
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
    for i in range(1, 7):
        v = "1" if (i == 4 and custom4) or (i == 6 and custom6) else "0"
        rows.append("<customint%d>%s</customint%d>" % (i, v, i))
    rows.append("<customint7>$@NULL@$</customint7>")
    rows.append("<customint8>$@NULL@$</customint8>")
    for i in range(1, 4):
        rows.append("<customchar%d>$@NULL@$</customchar%d>" % (i, i))
    rows.append("<customdec1>$@NULL@$</customdec1>")
    rows.append("<customdec2>$@NULL@$</customdec2>")
    for i in range(1, 5):
        rows.append("<customtext%d>$@NULL@$</customtext%d>" % (i, i))
    rows.append("<timecreated>%d</timecreated>" % TS)
    rows.append("<timemodified>%d</timemodified>" % TS)
    rows.append("<user_enrolments></user_enrolments>")
    return "    <enrol id=\"%d\">\n%s\n    </enrol>" % (eid, "\n".join(rows))

def build_enrolments_xml():
    manual = build_enrolment(enrol_ids[0], "manual", 0, 5, 86400, False, False)
    guest = build_enrolment(enrol_ids[1], "guest", 1, 0, 0, False, False, password="")
    selfe = build_enrolment(enrol_ids[2], "self", 0, 5, 86400, True, True)
    return ("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<enrolments>\n  <enrols>\n%s\n%s\n%s\n"
            "  </enrols>\n</enrolments>" % (manual, guest, selfe))

def build_roles_definition_xml():
    inner = ('  <role id="5">\n    <name></name>\n    <shortname>student</shortname>\n'
             "    <nameincourse>$@NULL@$</nameincourse>\n    <description></description>\n"
             "    <sortorder>5</sortorder>\n    <archetype>student</archetype>\n  </role>")
    return "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<roles_definition>\n%s\n</roles_definition>" % inner

def build_roles_xml():
    return ("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<roles>\n  <role_overrides></role_overrides>\n"
            "  <role_assignments></role_assignments>\n</roles>")

def aux(tag, inner=""):
    return "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<%s>%s</%s>" % (tag, inner, tag)

def build_course_inforef():
    return aux("inforef",
               "\n  <groupref></groupref>\n  <roleref>\n    <role>\n      <id>5</id>\n    </role>\n  </roleref>\n"
               "  <question_categoryref></question_categoryref>")

def build_moodle_backup_xml():
    acts = []
    for n in (1, 2, 3):
        acts.append(
            "        <activity>\n          <moduleid>%d</moduleid>\n          <sectionid>%d</sectionid>\n"
            "          <modulename>book</modulename>\n          <title>%s</title>\n"
            "          <directory>activities/book_%d</directory>\n        </activity>"
            % (mod_ids[n], sec_ids[n], esc_text("U%d. %s" % (n, UNITS[n - 1]["name"])), mod_ids[n]))
    secs = ["        <section>\n          <sectionid>%d</sectionid>\n          <title>0</title>\n"
            "          <directory>sections/section_%d</directory>\n        </section>" % (sec_general, sec_general)]
    for n in (1, 2, 3):
        secs.append("        <section>\n          <sectionid>%d</sectionid>\n"
                    "          <title>%d. %s</title>\n          <directory>sections/section_%d</directory>\n"
                    "        </section>" % (sec_ids[n], n, esc_text(UNITS[n - 1]["name"]), sec_ids[n]))
    root_settings = [
        ("filename", MBZ_NAME), ("imscc11", "0"), ("users", "0"), ("anonymize", "0"),
        ("role_assignments", "0"), ("activities", "1"), ("blocks", "1"), ("files", "1"),
        ("filters", "1"), ("comments", "0"), ("badges", "0"), ("calendarevents", "1"),
        ("userscompletion", "0"), ("logs", "0"), ("grade_histories", "0"), ("questionbank", "1"),
        ("groups", "1"), ("competencies", "1"), ("customfield", "1"), ("contentbankcontent", "1"),
        ("legacyfiles", "1"),
    ]
    settings = []
    for nm, v in root_settings:
        settings.append('      <setting>\n        <level>root</level>\n        <name>%s</name>\n'
                        "        <value>%s</value>\n      </setting>" % (nm, v))
    secdirs = ["section_%d" % sec_general] + ["section_%d" % sec_ids[n] for n in (1, 2, 3)]
    for sd in secdirs:
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
        "<moodle_version>2023100900.12</moodle_version>",
        "<moodle_release>4.3.12</moodle_release>",
        "<backup_version>2023100900</backup_version>",
        "<backup_release>4.3</backup_release>",
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

def build_log():
    stamp = time.strftime("%a %b %d %H:%M:%S %Y")
    lines = [
        "[%s] [info] instantiating backup controller %s" % (stamp, BACKUP_ID),
        "[%s] [debug] setting controller status to 100" % stamp,
        "[%s] [debug] loading controller plan" % stamp,
        "[%s] [debug] setting controller status to 300" % stamp,
        "[%s] [debug] applying plan defaults" % stamp,
        "[%s] [debug] setting controller status to 400" % stamp,
        "[%s] [info] checking plan security" % stamp,
        "[%s] [debug] setting controller status to 500" % stamp,
        "[%s] [debug] saving controller to db" % stamp,
    ]
    return "\n".join(lines) + "\n"

def main():
    books = {}
    for n in (1, 2, 3):
        books[n] = build_book_xml(UNITS[n - 1])

    files = {}
    for n in (1, 2, 3):
        d = "activities/book_%d" % mod_ids[n]
        files[d + "/book.xml"] = books[n]
        files[d + "/calendar.xml"] = aux("events")
        files[d + "/competencies.xml"] = aux("course_module_competencies", "\n  <competencies></competencies>")
        files[d + "/filters.xml"] = aux("filters", "\n  <filter_actives></filter_actives>\n  <filter_configs></filter_configs>")
        files[d + "/grade_history.xml"] = aux("grade_history", "\n  <grade_grades></grade_grades>")
        files[d + "/grades.xml"] = aux("activity_gradebook", "\n  <grade_items></grade_items>\n  <grade_letters></grade_letters>")
        files[d + "/inforef.xml"] = aux("inforef")
        files[d + "/module.xml"] = build_module_xml(n)
        files[d + "/roles.xml"] = build_roles_xml()

    course_files = [
        ("calendar.xml", aux("events")),
        ("competencies.xml", aux("course_competencies", "\n  <competencies></competencies>\n  <user_competencies></user_competencies>")),
        ("completiondefaults.xml", aux("course_completion_defaults")),
        ("contentbank.xml", aux("contents")),
        ("course.xml", build_course_xml()),
        ("enrolments.xml", build_enrolments_xml()),
        ("filters.xml", aux("filters", "\n  <filter_actives></filter_actives>\n  <filter_configs></filter_configs>")),
        ("inforef.xml", build_course_inforef()),
        ("roles.xml", build_roles_xml()),
    ]
    root_files = [
        ("completion.xml", aux("course_completion")),
        ("files.xml", aux("files")),
        ("grade_history.xml", aux("grade_history", "\n  <grade_grades></grade_grades>")),
        ("gradebook.xml", aux("gradebook", "\n  <attributes></attributes>\n  <grade_categories></grade_categories>\n"
                                           "  <grade_items></grade_items>\n  <grade_letters></grade_letters>\n"
                                           "  <grade_settings></grade_settings>")),
        ("groups.xml", aux("groups")),
        ("moodle_backup.log", build_log()),
        ("moodle_backup.xml", build_moodle_backup_xml()),
        ("outcomes.xml", aux("outcomes_definition")),
        ("questions.xml", aux("question_categories")),
        ("roles.xml", build_roles_definition_xml()),
        ("scales.xml", aux("scales_definition")),
    ]

    if os.path.exists(OUT_ROOT):
        shutil.rmtree(OUT_ROOT)
    os.makedirs(OUT_ROOT)

    order = [("activities", True)]
    for n in (1, 2, 3):
        d = "activities/book_%d" % mod_ids[n]
        order.append((d, True))
        for name in ["book.xml", "calendar.xml", "competencies.xml", "filters.xml",
                     "grade_history.xml", "grades.xml", "inforef.xml", "module.xml", "roles.xml"]:
            order.append((d + "/" + name, False))
    for name, content in root_files:
        files[name] = content
        order.append((name, False))
    order.append(("course", True))
    for name, content in course_files:
        files["course/" + name] = content
        order.append(("course/" + name, False))
    order.append(("sections", True))
    for sid in [sec_general] + [sec_ids[n] for n in (1, 2, 3)]:
        d = "sections/section_%d" % sid
        order.append((d, True))
        files[d + "/inforef.xml"] = aux("inforef")
        files[d + "/section.xml"] = (build_section_general_xml() if sid == sec_general
                                     else build_section_xml(UNITS.index(next(u for u in UNITS if sec_ids[u["num"]] == sid)) + 1))
        order.append((d + "/inforef.xml", False))
        order.append((d + "/section.xml", False))

    index_lines = ["Moodle archive file index. Count: %d" % len(order)]
    sizes = {}
    for path, is_dir in order:
        if is_dir:
            index_lines.append("%s/\td\t0\t?" % path)
        else:
            data = files[path].encode("utf-8")
            sizes[path] = data
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