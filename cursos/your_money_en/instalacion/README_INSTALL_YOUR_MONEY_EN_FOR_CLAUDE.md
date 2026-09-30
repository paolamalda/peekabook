# Instructions for Claude: install "Your Money, Your Family, Your Future" (Moodle 3.10)

You will create the course **Your Money, Your Family, Your Future** on academia.desarrollatalento.com. The site runs Moodle 3.10, the Boost theme, Level Up 3.15.2 and the **Custom certificate** plugin (mod_customcert).

If other courses exist on the site, **do not touch them.**

Work in the browser with the administrator session the person opened.

Rules:

- Use only the web interface.
- Do not use SSH.
- Do not install plugins.
- Do not change site settings.
- Do not touch other courses.
- If anything does not match these instructions, stop and ask.

## 0. Before you start

1. Confirm that no course with the short name `TDTF-CA-EN` exists. If it does, stop and ask.
2. Check in *Site administration > Plugins > Plugins overview* whether **Custom certificate** and **Level Up** exist. Note it for the report.
3. If the site has no H5P activities yet, the first one you upload installs its libraries: upload it with the administrator account. If a library error appears, stop and report the exact message.

## 1. Create the course

| Field | Value |
|---|---|
| Full name | Your Money, Your Family, Your Future |
| Short name | TDTF-CA-EN |
| Visibility | **Show** |
| Format | **Tiles** if installed; otherwise Topics. 7 sections |
| Completion tracking | Yes |
| Force language | English |

**Tiles format (if available):** in course settings, *Show progress on tiles*: **as a percentage**; one icon per module that fits its topic; the General section above the tiles. If Tiles doesn't exist, use Topics with "Show one section per page."

**Enrolment:** *Enrolment methods* > enable **Self enrolment** with the **enrolment key** the person gives you (if you don't have it, leave "[TBD]" and report it). Turn off guest access.

## 2. Sections

| Section | Name | Description |
|---|---|---|
| General | Welcome | Link to chapter 1 of the support book and the forum "Questions and comments" |
| 1 | Module 1. Understand your money and organize your finances | Content of `1_books/M1_resumen.html` |
| 2 | Module 2. Understand the financial system and plan your remittances | `M2_resumen.html` |
| 3 | Module 3. Build your credit and manage your debts | `M3_resumen.html` |
| 4 | Module 4. Protect your money, your identity and your family | `M4_resumen.html` |
| 5 | Module 5. Build wealth and prepare your future | `M5_resumen.html` |
| 6 | Support materials | "Cases, practice, glossary and where to get help." |
| 7 | Assessment and certificate | "Your certificate of completion." |

Description of the forum "Questions and comments": "Don't share account numbers, SSN, ITIN, passwords or your immigration status."

## 3. Lesson books

In each module section:

1. Create a book: name `Module N lessons`, chapter formatting "None", completion "View".
2. Book menu > **Import chapter** > `1_books/MN_libro_Moodle.zip`, type "Each HTML file represents one chapter".
3. Check that each lesson has its cover page first and 3 indented subchapters.

| Module | Chapters | Pages |
|---|---|---|
| M1 | 14 | 56 |
| M2 | 13 | 52 |
| M3 | 10 | 40 |
| M4 | 11 | 44 |
| M5 | 12 | 48 |

## 4. Support book

In section 6, create the book `Support materials` with the same settings and import `1_books/Apoyo_libro_Moodle.zip` (6 chapters). In the General section, add a **URL** or label to chapter 1 ("Welcome").

In the same section 6, add a **File** resource named `Tools for your numbers (Excel)` with the file in `10_tools/`. Display: "Force download". Description: "Budget, debt list, emergency fund and compound-interest goal. Type only in the pink cells; the file is yours and isn't shared." Completion: "View".

## 5. Glossary

In section 6, create the glossary `Course key words` and import `3_glossary/Glosario_curso_Moodle.xml`, destination "current glossary".

## 6. Question bank and self-assessments

1. *Question bank > Import*: GIFT format, `4_questions/banco_preguntas_v3_en.gift.txt`. Categories *Your Money v3.4/M1* to *M5* are created, with 180 questions.
2. In each module section, create the quiz `Module N self-assessment`: grade to pass 70, unlimited attempts, highest grade, shuffle answers, review with correct answer and feedback, completion "Require passing grade".
3. Add **all** questions from *Your Money v3.4/MN*, 10 per page:

| M1 | M2 | M3 | M4 | M5 |
|---|---|---|---|---|
| 42 | 39 | 30 | 33 | 36 |

## 7. H5P activities (60)

Files in `2_h5p/MN/`, in order. In each section, **after the book** and in lesson order:

1. *Add an activity > H5P*.
2. Name: `MN UYY · What would you do?`.
3. Upload `MN_UYY_what_would_you_do.h5p`.
4. Options: download no, embed no, copyright yes.
5. Grade: tracking yes, "highest grade". Completion: "Student must receive a grade".

**Final order of each section:** book, H5P in order, self-assessment.

**Check:** open 3 random activities with *Switch role to > Student*. You should see 3 cases, 3 options per case and the grade at the end.

## 8. Program surveys

`8_surveys/` has the surveys and their document `surveys.md`. Use the **Feedback** module in **anonymous** mode and, in each one, *Templates > Import questions* with its XML (if the import fails, build them by hand from `surveys.md`):

| Activity | Section | File | Completion |
|---|---|---|---|
| `Start survey` | General | `survey_start.xml` | Submit |
| `Final survey` | 7 | `survey_final.xml` | Submit; required for the certificate |
| `30-day follow-up` | 7 | `survey_follow_up.xml` | Submit |
| `90-day follow-up` | 7 | `survey_follow_up.xml` | Submit |

Restrict the follow-ups by date: 30 and 90 days after the cohort's end date ("[TBD]"). The final survey is the program's evidence of results: don't skip it.

## 9. Level Up, badges, completion and certificate

Follow `7_guides/gamification_guide.md`: sections 2 (Level Up), 3 (8 badges with `5_badges/`; each name includes the course so it's unique on the platform), 4 (completion with the 5 self-assessments) and 5 (certificate with the standard template and the data in `6_certificate/certificate.md`). If Level Up or Custom certificate does not exist, do not install it: skip that step and report it.

## 10. Final review (as a student)

- M1 U01: cover page first, two path buttons, colored terms with their meaning and "Current fact" or "Before you act, check" boxes.
- One H5P per module opens, shows 3 cases and records a grade.
- One self-assessment shows 3 options per question.
- The support book shows "See the key" in the case studies and collapsible frequently asked questions.

## 11. Report for the person

Course link; pages per book; H5P per module; questions per self-assessment; surveys created; active badges; Level Up settings; certificate status; what you could not do and why; screenshots of the tiles home page, an H5P, a self-assessment and the certificate preview.

The course stays **visible**, with enrolment by key. For the catalog listing, use `catalog_card.md`.
