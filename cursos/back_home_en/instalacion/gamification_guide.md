# Activities, points, badges and certificate guide · Back Home, Your Money, Your Future

This guide is for Moodle 4.5 with Level Up (block_xp) and the Custom certificate plugin (mod_customcert).

The goal is to motivate without competing. Points reward progress, not perfect scores. Nobody's name is ever shown in a table.

## 1. What each module has

| Activity | How many | Completion |
|---|---|---|
| Book "Module N lessons" | 1 per module (8) | View |
| H5P activity "MN UYY · What would you do?" | 1 per lesson (24) | Receive a grade |
| Quiz "Module N self-assessment" | 1 per module (8) | Passing grade of 70% |

**Each H5P activity:** no download button, copyright button on, embed off; attempt tracking with "Highest grade"; completion "Student must receive a grade".

**Self-assessments:** use the bank of 72 three-option questions with feedback, in categories *Back Home v0.1/M1* to *M8*. Passing grade 70%, unlimited attempts, shuffled answers and review with the correct answer and feedback at the end.

## 2. Level Up: levels and points

**Rules** (*Level Up > Rules*):

1. Remove the default rules or set them to 0.
2. **For completing any activity:** 25 points, event "Course module completion updated" (`\core\event\course_module_completion_updated`).
3. **For posting in the forum:** 5 points, event "Post created" (`\mod_forum\event\post_created`).
4. Keep cheat guard on.

Completing the whole course gives about 1,000 points:

| Activities | How many | Points |
|---|---|---|
| H5P activities | 24 | 600 |
| Books | 8 | 200 |
| Self-assessments | 8 | 200 |
| **Total** | 40 | **1,000** |

**Levels** (6 levels, no automatic algorithm):

| Level | Name | Points | Reached around |
|---|---|---|---|
| 1 | Getting started | 0 | On entry |
| 2 | Getting organized | 100 | During Module 2 |
| 3 | Moving forward | 200 | During Module 3 |
| 4 | Protecting what's mine | 350 | During Module 5 |
| 5 | Planning ahead | 450 | During Module 7 |
| 6 | I made it | 550 | During Module 8 |

**Ladder:** anonymity on; show only nearby neighbors or turn it off.

## 3. Badges

*More > Badges > Add a new badge*. Images in `5_badges/`. Issuer: Desarrolla Talento. Expiry: never. Names include the course so they're unique on the platform: use them exactly.

| Image | Badge | Criterion (activity completion, with passing grade) | Description |
|---|---|---|---|
| 01_papers_in_order.png | Papers in order · Back Home | Module 1 self-assessment completed (passed) | Your list of papers in order: repatriation record, CURP, birth certificate, INE and your children's papers. |
| 02_account_in_my_name.png | Account in my name · Back Home | Module 2 self-assessment completed (passed) | An account in your name to receive support and money, and your returnee cards used well. |
| 03_history_from_scratch.png | History from scratch · Back Home | Module 3 self-assessment completed (passed) | Your first credit history in Mexico, starting small and with no traps. |
| 04_nothing_left_behind.png | Nothing left behind · Back Home | Module 4 self-assessment completed (passed) | Your list of what was left there: last paycheck, accounts, taxes and retirement. |
| 05_weeks_counted.png | Weeks counted · Back Home | Module 5 self-assessment completed (passed) | Your contribution weeks checked and your Afore located. |
| 06_ninety_days.png | Ninety days · Back Home | Module 6 self-assessment completed (passed) | Your return budget for the first three months. |
| 07_what_i_know.png | What I know how to do · Back Home | Module 7 self-assessment completed (passed) | Your plan to use what you know how to do: a job, a trade or a small business. |
| 08_complete_plan.png | Complete plan · Back Home | Course completion | You completed the program's 8 modules. |

When done, **enable** each badge.

## 4. Course completion

*More > Course completion*: activity completion condition with **all** 8 self-assessments. Optional: the 8 books.

## 5. Certificate of completion (Custom certificate)

1. In the section "Assessment and certificate", add **Custom certificate** using the **platform's standard template** (no background image): name "Certificate of completion".
2. **Restrict access:** one "Activity completion" condition for each of the 8 self-assessments, "must be marked complete and pass", and the **Final survey** submitted.
3. In the template change only these data (also in `6_certificate/certificate.md`):

   | Field | Text |
   |---|---|
   | Course title | Back Home, Your Money, Your Future |
   | Line | for completing the financial well-being program Back Home, Your Money, Your Future |
   | Topic 1 | Papers and account |
   | Topic 2 | Credit from scratch |
   | Topic 3 | What was left there |
   | Topic 4 | Afore and weeks |
   | Topic 5 | Return plan |

4. Check the **PDF preview** and turn on "Verify certificate".

If Custom certificate is not installed, the **Complete plan · Back Home** badge works as a digital certificate.

## 6. What not to do

- Do not give points for viewing pages.
- Do not post names in rankings.
- Do not ask for real data to pass.
- Do not tie badges or the certificate to buying services or products.
