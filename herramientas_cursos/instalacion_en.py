# Generates instalacion/README_INSTALL_<X>_FOR_CLAUDE.md and instalacion/gamification_guide.md (English) from curso.json.
import os


def generar(D, CFG, lecciones):
    MODS = CFG["modulos"]; I = CFG["instalacion"]
    n = {m: len(lecciones(m)) for m in MODS}
    tot = sum(n.values()); nm = len(MODS)
    pts = (tot + 2 * nm) * 25
    sec_sup, sec_eval = nm + 1, nm + 2
    tit, short = CFG["titulo"], I["nombre_corto"]
    cat, bank = CFG["categoria"], CFG["banco"]
    rows_sec = "\n".join(f"| {i} | {t} | " + (f"Content of `1_books/{m}_resumen.html`" if i == 1 else f"`{m}_resumen.html`") + " |"
                         for i, (m, t) in enumerate(MODS.items(), 1))
    rows_book = "\n".join(f"| {m} | {n[m]} | {n[m] * 4} |" for m in MODS)
    head_q = "| " + " | ".join(MODS) + " |\n|" + "---|" * nm + "\n| " + " | ".join(str(n[m] * 3) for m in MODS) + " |"
    others = I.get("otros_cursos", "If other courses exist on the site, **do not touch them.**")
    extra = I.get("extra_readme", "")
    readme = f"""# Instructions for Claude: install "{tit}" (Moodle 3.10)

You will create the course **{tit}** on academia.desarrollatalento.com. The site runs Moodle 3.10, the Boost theme, Level Up 3.15.2 and the **Custom certificate** plugin (mod_customcert).

{others}

Work in the browser with the administrator session the person opened.

Rules:

- Use only the web interface.
- Do not use SSH.
- Do not install plugins.
- Do not change site settings.
- Do not touch other courses.
- If anything does not match these instructions, stop and ask.

## 0. Before you start

1. Confirm that no course with the short name `{short}` exists. If it does, stop and ask.
2. Check in *Site administration > Plugins > Plugins overview* whether **Custom certificate** and **Level Up** exist. Note it for the report.
3. If the site has no H5P activities yet, the first one you upload installs its libraries: upload it with the administrator account. If a library error appears, stop and report the exact message.

## 1. Create the course

| Field | Value |
|---|---|
| Full name | {tit} |
| Short name | {short} |
| Visibility | **Hide** |
| Format | Topics, {sec_eval} sections |
| Completion tracking | Yes |
| Force language | English |

## 2. Sections

| Section | Name | Description |
|---|---|---|
| General | Welcome | Link to chapter 1 of the support book and the forum "Questions and comments" |
{rows_sec}
| {sec_sup} | Support materials | "Cases, practice, glossary and where to get help." |
| {sec_eval} | Assessment and certificate | "Your certificate of completion." |

Description of the forum "Questions and comments": "{I['aviso_foro']}"

## 3. Lesson books

In each module section:

1. Create a book: name `Module N lessons`, chapter formatting "None", completion "View".
2. Book menu > **Import chapter** > `1_books/MN_libro_Moodle.zip`, type "Each HTML file represents one chapter".
3. Check that each lesson has its cover page first and 3 indented subchapters.

| Module | Chapters | Pages |
|---|---|---|
{rows_book}

## 4. Support book

In section {sec_sup}, create the book `Support materials` with the same settings and import `1_books/Apoyo_libro_Moodle.zip` (6 chapters). In the General section, add a **URL** or label to chapter 1 ("Welcome").

## 5. Glossary

In section {sec_sup}, create the glossary `Course key words` and import `3_glossary/Glosario_curso_Moodle.xml`, destination "current glossary".

## 6. Question bank and self-assessments

1. *Question bank > Import*: GIFT format, `4_questions/{bank}`. Categories *{cat}/M1* to *M{nm}* are created, with {tot * 3} questions.
2. In each module section, create the quiz `Module N self-assessment`: grade to pass 70, unlimited attempts, highest grade, shuffle answers, review with correct answer and feedback, completion "Require passing grade".
3. Add **all** questions from *{cat}/MN*, 10 per page:

{head_q}

## 7. H5P activities ({tot})

Files in `2_h5p/MN/`, in order. In each section, **after the book** and in lesson order:

1. *Add an activity > H5P*.
2. Name: `MN UYY · What would you do?`.
3. Upload `MN_UYY_what_would_you_do.h5p`.
4. Options: download no, embed no, copyright yes.
5. Grade: tracking yes, "highest grade". Completion: "Student must receive a grade".

**Final order of each section:** book, H5P in order, self-assessment.

**Check:** open 3 random activities with *Switch role to > Student*. You should see 3 cases, 3 options per case and the grade at the end.

## 8. Level Up, badges, completion and certificate

Follow `7_guides/gamification_guide.md`: sections 2 (Level Up), 3 (8 badges with `5_badges/`), 4 (completion with the {nm} self-assessments) and 5 (certificate with `6_certificate/certificate_background.png`). If Level Up or Custom certificate does not exist, do not install it: skip that step and report it.
{extra}
## {10 if extra else 9}. Final review (as a student)

- M1 U01: cover page first, two path buttons, colored terms with their meaning and "Current fact" or "Before you act, check" boxes.
- One H5P per module opens, shows 3 cases and records a grade.
- One self-assessment shows 3 options per question.
- The support book shows "See the key" in the case studies and collapsible frequently asked questions.

## {11 if extra else 10}. Report for the person

Course link; pages per book; H5P per module; questions per self-assessment; active badges; Level Up settings; certificate status; what you could not do and why; screenshots of a cover page, an H5P, a self-assessment and the certificate preview.

The course stays **hidden**. The person decides when to show it.
"""
    levels = "\n".join(f"| {i} | {nom} | {p:,} | {when} |" for i, (nom, p, when) in enumerate(I["niveles"], 1))
    bad = "\n".join(f"| {fn}.png | {nom} | {crit} | {desc} |" for (fn, tag, nom, icon), (crit, desc) in zip(CFG["insignias"], I["insignias_info"]))
    guide = f"""# Activities, points, badges and certificate guide · {tit}

This guide is for Moodle 3.10 with Level Up (block_xp) 3.15.2 and the Custom certificate plugin (mod_customcert).

The goal is to motivate without competing. Points reward progress, not perfect scores. Nobody's name is ever shown in a table.

## 1. What each module has

| Activity | How many | Completion |
|---|---|---|
| Book "Module N lessons" | 1 per module ({nm}) | View |
| H5P activity "MN UYY · What would you do?" | 1 per lesson ({tot}) | Receive a grade |
| Quiz "Module N self-assessment" | 1 per module ({nm}) | Passing grade of 70% |

**Each H5P activity:** no download button, copyright button on, embed off; attempt tracking with "Highest grade"; completion "Student must receive a grade".

**Self-assessments:** use the bank of {tot * 3} three-option questions with feedback, in categories *{cat}/M1* to *M{nm}*. Passing grade 70%, unlimited attempts, shuffled answers and review with the correct answer and feedback at the end.

## 2. Level Up: levels and points

**Rules** (*Level Up > Rules*):

1. Remove the default rules or set them to 0.
2. **For completing any activity:** 25 points, event "Course module completion updated" (`\\core\\event\\course_module_completion_updated`).
3. **For posting in the forum:** 5 points, event "Post created" (`\\mod_forum\\event\\post_created`).
4. Keep cheat guard on.

Completing the whole course gives about {pts:,} points:

| Activities | How many | Points |
|---|---|---|
| H5P activities | {tot} | {tot * 25:,} |
| Books | {nm} | {nm * 25:,} |
| Self-assessments | {nm} | {nm * 25:,} |
| **Total** | {tot + 2 * nm} | **{pts:,}** |

**Levels** (6 levels, no automatic algorithm):

| Level | Name | Points | Reached around |
|---|---|---|---|
{levels}

**Ladder:** anonymity on; show only nearby neighbors or turn it off.

## 3. Badges

*Course administration > Badges > Add a new badge*. Images in `5_badges/`. Issuer: Desarrolla Talento. Expiry: never.

| Image | Badge | Criterion (activity completion, with passing grade) | Description |
|---|---|---|---|
{bad}

When done, **enable** each badge.

## 4. Course completion

*Course administration > Course completion*: activity completion condition with **all** {nm} self-assessments. Optional: the {nm} books.

## 5. Certificate of completion (Custom certificate)

1. In the section "Assessment and certificate", add **Custom certificate**: name "Certificate of completion", A4 landscape (297 × 210 mm).
2. **Restrict access:** one "Activity completion" condition for each of the {nm} self-assessments, "must be marked complete and pass".
3. **Edit certificate:**

   | Element | Approximate position (mm) | Format |
   |---|---|---|
   | Background image | Covers the page | `6_certificate/certificate_background.png` |
   | Student name | X 0, Y 74, width 297, centered | Bold, 32 pt, color #0B1220 |
   | Date (course completion) | X 17, Y 170, width 70, centered | 12 pt, color #E4007C |
   | Code | X 210, Y 170, width 70, centered | 12 pt, color #E4007C |

4. Check the **PDF preview** and compare it with `certificate_sample.png`. Turn on "Verify certificate".

If Custom certificate is not installed, the **Full plan** badge works as a digital certificate.

## 6. What not to do

- Do not give points for viewing pages.
- Do not post names in rankings.
- Do not ask for real data to pass.
- Do not tie badges or the certificate to buying services or products.
"""
    os.makedirs(os.path.join(D, "instalacion"), exist_ok=True)
    for f in os.listdir(os.path.join(D, "instalacion")):
        if f.startswith("README_INSTALL"): os.remove(os.path.join(D, "instalacion", f))
    open(os.path.join(D, "instalacion", I["readme"]), "w").write(readme)
    open(os.path.join(D, "instalacion", "gamification_guide.md"), "w").write(guide)
    print("README and gamification guide ·", tot, "lessons ·", pts, "points")
