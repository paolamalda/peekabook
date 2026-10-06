# Instructions for Claude: install "Back Home, Your Money, Your Future" (Moodle 4.5)

You will create the course **Back Home, Your Money, Your Future** on academia.desarrollatalento.com. The site runs Moodle 4.5, the Boost theme, Level Up (block_xp) and the **Custom certificate** plugin (mod_customcert).

If other courses exist on the site, **do not touch them.**

Work in the browser with the administrator session the person opened.

Rules:

- Use only the web interface.
- Do not use SSH.
- Do not install plugins.
- Do not change site settings.
- Do not touch other courses.
- If anything does not match these instructions, stop and ask.

## In Moodle 4.5: where everything is

The site runs **Moodle 4.5**. Where these instructions name a menu, look for it like this:

| To | In Moodle 4.5 |
|---|---|
| Edit the course | **Edit mode** toggle, top right |
| Settings, participants, badges, question bank, content bank, completion | Course menu (tabs under the title): *Settings*, *Participants* and *More* > *Question bank*, *Content bank*, *Badges*, *Course completion* |
| Enrolment methods | *Participants* > selector at the top > *Enrolment methods* |
| Import chapters into a book | Inside the book, actions menu (⋮ or *More*) > *Import chapter* |
| Import glossary entries | Inside the glossary, selector or actions menu > *Import entries* |
| Import questions into a survey (Feedback) | Inside the activity, *Questions* tab > menu > *Import questions* |
| View as a student | Your user menu (top right) > *Switch role to…* > *Student* |
| Activity completion | In its settings, *Completion conditions* section |

**To save hours** (the course has many pieces):

1. **Default completion before creating the books:** *More > Course completion* > selector > *Default activity completion*. For **Book**: "View". For **Quiz**: "Receive a passing grade". Every new book then starts with its completion set.
2. **Bulk edit:** in edit mode, *Bulk edit* (top right) lets you move, show or hide several activities at once.
3. **Work in stages and report at each one:** first the General section (Welcome, forum, "My goal", start survey, "Your starting point") and all of Part 1. Stop, take screenshots and report to the person before continuing with the other parts.
4. If an option in these instructions has a different name in 4.5, use the equivalent and note it in the report.

**Tiles in 4.5:** if *Use sub-tiles for activities* or *Show progress* don't appear in the course settings, they may be turned off for the whole site; don't change site settings: report it.

**Level Up in 4.5:** newer versions group the rules under *Level Up > Points*. If there is an **activity completion** rule, use it with 25 points instead of the event. *Ladder* may be called *Leaderboard*.

## 0. Before you start

1. Confirm that no course with the short name `TRDF-MX-EN` exists. If it does, stop and ask.
2. Check in *Site administration > Plugins > Plugins overview* whether **Custom certificate** and **Level Up** exist. Note it for the report.
3. If the site has no H5P activities yet, the first one you upload installs its libraries: upload it with the administrator account. If a library error appears, stop and report the exact message.

## 1. Create the course

| Field | Value |
|---|---|
| Full name | Back Home, Your Money, Your Future |
| Short name | TRDF-MX-EN |
| Visibility | **Show** |
| Format | **Tiles**. 10 sections |
| Completion tracking | Yes |
| Force language | English |

**Tiles format:**
- *Show progress on tiles*: **as a percentage**.
- **Use sub-tiles for activities: Yes** (each lesson shows as a tile inside its part).
- One icon per part that fits its topic; the General section above the tiles.
- Hide the Level Up *Ladder* or *Leaderboard* block if it appears in the right column.

**Enrolment:** *Enrolment methods* > enable **Self enrolment** with the **enrolment key** the person gives you (if you don't have it, leave "[TBD]" and report it). Turn off guest access.

## 2. Sections

| Section | Name | Description |
|---|---|---|
| General | Welcome | «Welcome» book, "Questions and comments" forum, start survey, «Your starting point» and «My goal» |
| 1 | Your papers | Content of `1_books/M1_resumen.html` |
| 2 | Your account in Mexico | `M2_resumen.html` |
| 3 | Credit from scratch | `M3_resumen.html` |
| 4 | What you left in the United States | `M4_resumen.html` |
| 5 | Your Afore, your IMSS and your weeks | `M5_resumen.html` |
| 6 | Your first 90 days | `M6_resumen.html` |
| 7 | Work or a business with what you know how to do | `M7_resumen.html` |
| 8 | Don't get scammed when you return | `M8_resumen.html` |
| 9 | Support materials | "Cases, practice, glossary and where to get help." |
| 10 | Closing and certificate | "What you achieved, your certificate and see you soon." |

Description of the forum "Questions and comments": "Don't share account numbers, PINs, passwords, your CURP, documents or the real amounts of your debts."

### Welcome and farewell (designed books)

They are the first and last thing each person sees: don't skip them.

1. **General section, at the very top:** create the book `Welcome` (chapter formatting "None", navigation "Text") and import `1_books/Bienvenida_libro_Moodle.zip`, type "Each HTML file represents one chapter". There must be 4 chapters: Welcome, How the course works, Contact and community guide, Before you start. Completion: "View".
2. Below it, the **"Questions and comments"** forum (general forum). **Don't create an introductions forum:** asking people to introduce themselves invites them to share personal data.
   Then the **"My goal"** assignment: type *Assignment*, submission "Online text" (60-word limit), **no grade**, no due date, no notifications to other participants; only the person and the course team can see submissions. Instructions: "In one sentence: what you expect from the program and what you want to achieve. Don't write personal data or real amounts. You'll open it again at the end of the course." Allow editing the submission at any time. Completion: "Submit".
3. Below, the **Start survey** (section 8) and the **«Your starting point»**: import `4_questions/diagnostica.gift.txt` (it creates its own «Start» category), all questions, maximum grade 0 (doesn't count toward the grade), **one attempt**, 10-minute time limit, review with the correct answer at the end.
4. **Restrict access** on the first lesson of Part 1: the `Welcome` book must be viewed.
5. **Section 10, at the very top:** create the book `Closing and farewell` with the same settings and import `1_books/Cierre_libro_Moodle.zip` (4 chapters: What you achieved, Your plan continues, Final survey and certificate, See you soon). Restrict access: the last part's self-assessment must be complete. The final survey and certificate go below it.
6. **Guide to print or share:** `7_guides/Contact_and_community_guide.html`. Open it in a browser > Print > Save as PDF, and share it in the in-person session or by WhatsApp.

## 3. Lessons: one book per lesson

The full structure (names, order, files and minutes) is in `estructura_moodle.json`. In each section, for each lesson and in order:

1. Create a **Book** with the lesson name **exactly as written** (the question, without codes like "M1 U01"). Chapter formatting "None"; navigation style "Text".
2. Book menu > **Import chapter** > the lesson zip (`1_books/MN/NN_MN_UYY.zip`), type "Each HTML file represents one chapter". There should be 4 chapters: Start, The essentials, Go deeper, Practice.
3. **Completion:** "View".
4. **Restrict access:** the previous lesson must be complete (the first lesson of each part has no restriction; the first lesson of part 2 onward requires the last lesson of the previous part). Show the locked lesson greyed out, not hidden.

| Part | Lessons | Folder |
|---|---|---|
| Your papers | 3 | `1_books/M1/` |
| Your account in Mexico | 3 | `1_books/M2/` |
| Credit from scratch | 3 | `1_books/M3/` |
| What you left in the United States | 3 | `1_books/M4/` |
| Your Afore, your IMSS and your weeks | 3 | `1_books/M5/` |
| Your first 90 days | 3 | `1_books/M6/` |
| Work or a business with what you know how to do | 3 | `1_books/M7/` |
| Don't get scammed when you return | 3 | `1_books/M8/` |

## 4. Support book

In section 9, create the book `Support materials` with the same settings and import `1_books/Apoyo_libro_Moodle.zip` (6 chapters).

Below it, create the book **`Further reading`** with the same settings and import `1_books/Fondo_libro_Moodle.zip` (9 chapters: "How to use further reading" and one per part). Description: "Optional. For people who want to read the official sources, rules and documents for each topic." **Completion: none** (it's optional and doesn't count toward finishing the course).

In the same section 9, add a **File** resource named `Tools for your numbers (Excel)` with the file in `10_tools/`. Display: "Force download". Description: "Budget, debt list, emergency fund and compound-interest goal. Type only in the pink cells; the file is yours and isn't shared." Completion: "View".

## 5. Glossary

In section 9, create the glossary `Course key words` and import `3_glossary/Glosario_curso_Moodle.xml`, destination "current glossary".

## 6. Question bank and self-assessments

1. *Question bank > Import*: GIFT format, `4_questions/banco_preguntas_trdf_en.gift.txt`. Categories *Back Home v0.1/M1* to *M8* are created, with 72 questions.
2. In each module section, create the quiz `Module N self-assessment`: grade to pass 70, unlimited attempts, highest grade, shuffle answers, review with correct answer and feedback, completion "Require passing grade".
3. Add **all** questions from *Back Home v0.1/MN*, 10 per page:

| M1 | M2 | M3 | M4 | M5 | M6 | M7 | M8 |
|---|---|---|---|---|---|---|---|
| 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |

## 7. Practice inside each lesson (24 H5P)

The practice does **not** go as a separate activity in the section: it is embedded in the "Practice" chapter of its book.

1. Course *Content bank* > **Upload** the 24 files from `2_h5p/MN/` (`MN_UYY_practica.h5p`).
2. Open the "Practice" chapter of each book in edit mode. You'll see a pink box with the text `[[H5P MN_UYY_practica.h5p]]`.
3. Delete **the whole box** and in its place insert the H5P with the editor's **Insert H5P** button, choosing that file from the content bank.
4. Save and check with *Switch role to > Student* that the situations and questions show, one per screen.

**Note:** embedded practice doesn't record a grade. Each lesson's progress is marked when it's viewed, and the module grade comes from the self-assessment.

**Final order of each section:** the lessons in order and the self-assessment at the end (restricted to completing the last lesson of the part).

## 8. Program surveys

`8_surveys/` has the surveys and their document `surveys.md`. Use the **Feedback** module in **anonymous** mode and, in each one, *Templates > Import questions* with its XML (if the import fails, build them by hand from `surveys.md`):

| Activity | Section | File | Completion |
|---|---|---|---|
| `Start survey` | General | `survey_start.xml` | Submit |
| `Final survey` | 10 | `survey_final.xml` | Submit; required for the certificate |
| `30-day follow-up` | 10 | `survey_follow_up.xml` | Submit |
| `90-day follow-up` | 10 | `survey_follow_up.xml` | Submit |

Restrict the follow-ups by date: 30 and 90 days after the cohort's end date ("[TBD]"). The final survey is the program's evidence of results: don't skip it.

## 9. Level Up, badges, completion and certificate

Follow `7_guides/gamification_guide.md`: sections 2 (Level Up), 3 (8 badges with `5_badges/`; each name includes the course so it's unique on the platform), 4 (completion with the 8 self-assessments) and 5 (certificate with the standard template and the data in `6_certificate/certificate.md`). If Level Up or Custom certificate does not exist, do not install it: skip that step and report it.

## Extra section: Programs and support

This section is **separate**: nothing in the course depends on it.

1. Add a section **at the end** of the course called `Programs and support` (description: "Government programs and public services that may help you. Reviewed information; confirm it on the official site."). Pick a "help" icon for its tile.
2. Create the book `Programs and support` with the same settings and import `1_books/Programas_libro_Moodle.zip` (11 chapters).
3. **Completion: none.** Don't add it to course completion or to any other activity's restrictions, and don't give it points.
4. **To remove it:** hide the section (eye icon > Hide) or delete it. The rest of the course stays the same.
5. If you get a new package for this book, replace only this book.

## 10. Final review (as a student)

- The home page shows one tile per part with its percentage; inside each part, one sub-tile per lesson with no technical codes.
- The first lesson: chapters Start, The essentials, Go deeper and Practice; "Watch out for these mistakes" at the end of The essentials; the embedded practice works.
- The second lesson shows as locked until the first is viewed.
- No leaderboard or ladder is visible.
- One self-assessment shows 3 options per question.
- The support book shows "See the key" in the case studies and collapsible frequently asked questions.

## 11. Report for the person

Course link; books per part; embedded H5P; questions per self-assessment; surveys created; active badges; Level Up settings; certificate status; what you could not do and why; screenshots of the tiles home page, an H5P, a self-assessment and the certificate preview.

The course stays **visible**, with enrolment by key. For the catalog listing, use `catalog_card.md`.
