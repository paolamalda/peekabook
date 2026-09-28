# Guide to activities, points, badges and certificate (version 3, English course)

This guide is for Moodle 3.10 with Level Up (block_xp) 3.15.2 and the Custom certificate plugin (mod_customcert), which is already installed on the site.

The goal is to motivate without competing. Points reward moving forward, not a perfect grade. Nobody's name is ever shown on a leaderboard.

## 1. What's in each module

| Activity | How many | Completion |
|---|---|---|
| Book "Module N Lessons" | 1 per module | View |
| H5P activity "MN UYY · What would you do?" | 1 per lesson (59 in total) | Receive a grade |
| Quiz "Module N Self-assessment" | 1 per module | Passing grade of 70% |

**The H5P activities:**

- Each one has three cases from the lesson, with three options each.
- They shuffle the options, mark the correct answer and allow retries.
- They're *Single Choice Set* activities. They include their libraries, in versions compatible with Moodle 3.10.
- Upload them as an **H5P activity** (mod_h5pactivity, part of Moodle since 3.9).

**Settings for each H5P activity:**

- H5P options: no download button, copyright button on, embed off.
- Attempts: tracking on, grading method "Highest grade".
- Completion: "Student must receive a grade".

**The self-assessments:**

- They use the v3 question bank: 177 questions with three options and feedback.
- Each module has its own category: *Your Money v3/M1* to *M5*.
- Settings: 70% passing grade, unlimited attempts and review with the correct answer and feedback at the end.

## 2. Level Up: levels and points

The free version of Level Up gives points for **events**. Set up a single main rule, so it works with both the free version and Level Up+.

**Rules** (*Level Up > Rules*):

1. **Remove or set the default rules to 0.** That way, opening a page or viewing a resource doesn't give points.
2. **For completing any activity:** 25 points. Use the event "Course module completion updated" (`\core\event\course_module_completion_updated`).
3. **For taking part in the forum:** 5 points. Use the event "Post created" (`\mod_forum\event\post_created`).
4. Keep Level Up's **cheat guard** on. It stops the same repeated event from adding points.

With these rules, completing the whole course gives about 1,725 points:

| Activities | How many | Points |
|---|---|---|
| H5P activities | 59 | 1,475 |
| Books | 5 | 125 |
| Self-assessments | 5 | 125 |
| **Total** | 69 | **1,725** |

**Levels** (*Level Up > Levels*, 6 levels, no automatic algorithm):

| Level | Name | Points | Reached roughly |
|---|---|---|---|
| 1 | Getting started | 0 | On entry |
| 2 | Getting organized | 150 | Halfway through Module 1 |
| 3 | Using my account | 450 | During Module 2 |
| 4 | Caring for my credit | 800 | During Module 3 |
| 5 | Protecting my family | 1,150 | During Module 4 |
| 6 | Building my future | 1,500 | During Module 5 |

**Ladder** (*Level Up > Ladder*):

- Anonymity on.
- Show only nearby neighbors, or turn the ladder off.

## 3. Badges

Create them in *Course administration > Badges > Add a new badge*. The images are in `5_badges/`.

For each badge:

- **Issuer:** Desarrolla Talento.
- **Expiry:** never.
- **Criteria:** "Activity completion", except "Complete plan", which uses "Course completion".

| Image | Badge | Criteria | Description |
|---|---|---|---|
| 01_M1_my_money_in_order.png | My money in order | Module 1 Self-assessment completed (passed) | You organized your cash flow, your budget and your taxes. 14 lessons, about 3 hours. |
| 02_M2_smart_sending.png | Smart sending | Module 2 Self-assessment | You know how to choose an account, compare remittances and protect your family from fraud. 13 lessons. |
| 03_M3_credit_on_track.png | Credit on track | Module 3 Self-assessment | You understand your report, compare loans and have a debt plan. 10 lessons. |
| 04_M4_protected_family.png | Protected family | Module 4 Self-assessment | You have a plan for protection, insurance and family preparedness. 11 lessons. |
| 05_M5_future_in_motion.png | Future in motion | Module 5 Self-assessment | Your goals, your retirement and your one-page plan are in writing. 11 lessons. |
| 06_scam_detective.png | Scam detective | H5P for M2 U11, M4 U01 and M4 U02 completed | You recognize the signs of fraud and verify before you act. |
| 07_expert_comparer.png | Expert comparer | H5P for M2 U08, M3 U05 and M5 U05 completed | You compare by total cost, not just the advertised price. |
| 08_complete_plan.png | Complete plan | Course completion | You completed the program's five modules. |

When you're done, **enable** each badge (*Enable access*). Moodle doesn't let you change the criteria of a badge that has already been awarded.

## 4. Course completion

*Course administration > Course completion*:

- **Condition:** activity completion, with **all** of these: the 5 self-assessments.
- **Optional:** also add the 5 books.

## 5. Certificate of completion (Custom certificate)

1. In the "Assessment and certificate" section, add a **Custom certificate** activity.
   - **Name:** Certificate of Completion.
   - **Size:** A4 landscape (297 × 210 mm).
2. **Restrict access:** add one "Activity completion" condition for each of the 5 self-assessments, with the option "must be marked complete and pass grade".
3. **Edit certificate.** Add these elements:

   | Element | Approximate position (mm) | Format |
   |---|---|---|
   | Background image | Covers the page | `6_certificate/certificate_background.png` |
   | Student name | X 0, Y 74, width 297, centered | Bold, 32 pt, color #0B1220 |
   | Date (course completion date) | X 17, Y 170, width 70, centered | 12 pt, color #E4007C |
   | Code | X 210, Y 170, width 70, centered | 12 pt, color #E4007C |

4. Use **Preview PDF** and adjust the Y positions if anything overlaps. Compare with `certificate_sample.png`.
5. **Optional:** turn on "Verify certificate" so anyone can check the code.

## 6. What not to do

- Don't give points for viewing pages.
- Don't publish names on leaderboards.
- Don't ask for real data to pass.
- Don't create badges with criteria that depend on amounts of money or on signing up for products.
