# Instructions for Claude: install "Your Business, Your Money, Your Future · U.S." (Moodle 3.10)

You will create the course **Your Business, Your Money, Your Future · U.S.** on academia.desarrollatalento.com. The site runs Moodle 3.10, the Boost theme, Level Up 3.15.2 and the **Custom certificate** plugin (mod_customcert).

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

1. Confirm that no course with the short name `YBMF-US-EN` exists. If it does, stop and ask.
2. Check in *Site administration > Plugins > Plugins overview* whether **Custom certificate** and **Level Up** exist. Note it for the report.
3. If the site has no H5P activities yet, the first one you upload installs its libraries: upload it with the administrator account. If a library error appears, stop and report the exact message.

## 1. Create the course

| Field | Value |
|---|---|
| Full name | Your Business, Your Money, Your Future · U.S. |
| Short name | YBMF-US-EN |
| Visibility | **Hide** |
| Format | Topics, 11 sections |
| Completion tracking | Yes |
| Force language | English |

## 2. Sections

| Section | Name | Description |
|---|---|---|
| General | Welcome | Link to chapter 1 of the support book and the forum "Questions and comments" |
| 1 | Module 1. Your business and your home: separate money | Content of `1_books/M1_resumen.html` |
| 2 | Module 2. Costs and price | `M2_resumen.html` |
| 3 | Module 3. Cash flow | `M3_resumen.html` |
| 4 | Module 4. Get paid and sell without losing | `M4_resumen.html` |
| 5 | Module 5. Formalize and handle taxes without fear | `M5_resumen.html` |
| 6 | Module 6. Credit for your business | `M6_resumen.html` |
| 7 | Module 7. Protect your business | `M7_resumen.html` |
| 8 | Module 8. Grow in an orderly way | `M8_resumen.html` |
| 9 | Module 9. Your future | `M9_resumen.html` |
| 10 | Support materials | "Cases, practice, glossary and where to get help." |
| 11 | Assessment and certificate | "Your certificate of completion." |

Description of the forum "Questions and comments": "Do not share your SSN, ITIN, EIN, passwords, account numbers, your business's real amounts or your immigration status."

## 3. Lesson books

In each module section:

1. Create a book: name `Module N lessons`, chapter formatting "None", completion "View".
2. Book menu > **Import chapter** > `1_books/MN_libro_Moodle.zip`, type "Each HTML file represents one chapter".
3. Check that each lesson has its cover page first and 3 indented subchapters.

| Module | Chapters | Pages |
|---|---|---|
| M1 | 5 | 20 |
| M2 | 4 | 16 |
| M3 | 3 | 12 |
| M4 | 3 | 12 |
| M5 | 5 | 20 |
| M6 | 4 | 16 |
| M7 | 7 | 28 |
| M8 | 4 | 16 |
| M9 | 3 | 12 |

## 4. Support book

In section 10, create the book `Support materials` with the same settings and import `1_books/Apoyo_libro_Moodle.zip` (6 chapters). In the General section, add a **URL** or label to chapter 1 ("Welcome").

## 5. Glossary

In section 10, create the glossary `Course key words` and import `3_glossary/Glosario_curso_Moodle.xml`, destination "current glossary".

## 6. Question bank and self-assessments

1. *Question bank > Import*: GIFT format, `4_questions/question_bank_ybmf_us_en.gift.txt`. Categories *Your Business US EN/M1* to *M9* are created, with 114 questions.
2. In each module section, create the quiz `Module N self-assessment`: grade to pass 70, unlimited attempts, highest grade, shuffle answers, review with correct answer and feedback, completion "Require passing grade".
3. Add **all** questions from *Your Business US EN/MN*, 10 per page:

| M1 | M2 | M3 | M4 | M5 | M6 | M7 | M8 | M9 |
|---|---|---|---|---|---|---|---|---|
| 15 | 12 | 9 | 9 | 15 | 12 | 21 | 12 | 9 |

## 7. H5P activities (38)

Files in `2_h5p/MN/`, in order. In each section, **after the book** and in lesson order:

1. *Add an activity > H5P*.
2. Name: `MN UYY · What would you do?`.
3. Upload `MN_UYY_what_would_you_do.h5p`.
4. Options: download no, embed no, copyright yes.
5. Grade: tracking yes, "highest grade". Completion: "Student must receive a grade".

**Final order of each section:** book, H5P in order, self-assessment.

**Check:** open 3 random activities with *Switch role to > Student*. You should see 3 cases, 3 options per case and the grade at the end.

## 8. Level Up, badges, completion and certificate

Follow `7_guides/gamification_guide.md`: sections 2 (Level Up), 3 (8 badges with `5_badges/`), 4 (completion with the 9 self-assessments) and 5 (certificate with `6_certificate/certificate_background.png`). If Level Up or Custom certificate does not exist, do not install it: skip that step and report it.

## 9. Community (optional, ask first)

Ask the person whether they want you to create the course **Your Business Community · U.S.** (`YBMF-US-EN-COM`, hidden). It has its own folder and instructions: `README_CREATE_COMMUNITY_FOR_CLAUDE.md`.

## 10. Final review (as a student)

- M1 U01: cover page first, two path buttons, colored terms with their meaning and "Current fact" or "Before you act, check" boxes.
- One H5P per module opens, shows 3 cases and records a grade.
- One self-assessment shows 3 options per question.
- The support book shows "See the key" in the case studies and collapsible frequently asked questions.

## 11. Report for the person

Course link; pages per book; H5P per module; questions per self-assessment; active badges; Level Up settings; certificate status; what you could not do and why; screenshots of a cover page, an H5P, a self-assessment and the certificate preview.

The course stays **hidden**. The person decides when to show it.
