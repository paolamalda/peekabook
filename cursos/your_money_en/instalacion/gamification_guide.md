# Activities, points, badges and certificate guide · Your Money, Your Family, Your Future

This guide is for Moodle 4.5 with Level Up (block_xp) and the Custom certificate plugin (mod_customcert).

The goal is to motivate without competing. Points reward progress, not perfect scores. Nobody's name is ever shown in a table.

## 1. What each part has

| Activity | How many | Completion |
|---|---|---|
| One book per lesson (with the practice embedded) | 63 | View |
| Quiz "Module N self-assessment" | 1 per part (5) | Passing grade of 70% |

**Self-assessments:** use the bank of 189 three-option questions with feedback, in categories *Your Money v1.0/M1* to *M5*. Passing grade 70%, unlimited attempts, shuffled answers and review with the correct answer and feedback at the end.

## 2. Level Up: levels and points

**Rules** (*Level Up > Rules*):

1. Remove the default rules or set them to 0.
2. **For completing any activity:** 25 points, event "Course module completion updated" (`\core\event\course_module_completion_updated`).
3. **For posting in the forum:** 5 points, event "Post created" (`\mod_forum\event\post_created`).
4. Keep cheat guard on.

Completing the whole course gives about 1,700 points:

| Activities | How many | Points |
|---|---|---|
| Lessons | 63 | 1,575 |
| Self-assessments | 5 | 125 |
| **Total** | 68 | **1,700** |

**Levels** (6 levels, no automatic algorithm):

| Level | Name | Points | Reached around |
|---|---|---|---|
| 1 | Getting started | 0 | On entry |
| 2 | Getting organized | 150 | Halfway through Module 1 |
| 3 | Using my account | 450 | During Module 2 |
| 4 | Caring for my credit | 800 | During Module 3 |
| 5 | Protecting my family | 1,150 | During Module 4 |
| 6 | Building my future | 1,500 | During Module 5 |

**Ladder (leaderboard): off.** In *Level Up > Ladder* choose not to show it, and remove or hide the leaderboard block. Each person sees only their own points, level and badges.

## 3. Badges

*More > Badges > Add a new badge*. Images in `5_badges/`. Issuer: Desarrolla Talento. Expiry: never. Names include the course so they're unique on the platform: use them exactly.

| Image | Badge | Criterion (activity completion, with passing grade) | Description |
|---|---|---|---|
| 01_M1_my_money_in_order.png | My money in order · Your Money | Module 1 Self-assessment completed (passed) | You organized your cash flow, your budget and your taxes. 14 lessons, about 3 hours. |
| 02_M2_smart_sending.png | Smart sending · Your Money | Module 2 Self-assessment | You know how to choose an account, compare remittances and protect your family from fraud. 13 lessons. |
| 03_M3_credit_on_track.png | Credit on track · Your Money | Module 3 Self-assessment | You understand your report, compare loans and have a debt plan. 10 lessons. |
| 04_M4_protected_family.png | Protected family · Your Money | Module 4 Self-assessment | You have a plan for protection, insurance and family preparedness. 11 lessons. |
| 05_M5_future_in_motion.png | Future in motion · Your Money | Module 5 Self-assessment | Your goals, your retirement and your one-page plan are in writing. 11 lessons. |
| 06_scam_detective.png | Scam detective · Your Money | H5P for M2 U11, M4 U01 and M4 U02 completed | You recognize the signs of fraud and verify before you act. |
| 07_expert_comparer.png | Expert comparer · Your Money | H5P for M2 U08, M3 U05 and M5 U05 completed | You compare by total cost, not just the advertised price. |
| 08_complete_plan.png | Complete plan · Your Money | Course completion | You completed the program's five modules. |

When done, **enable** each badge.

## 4. Course completion

*More > Course completion*: activity completion condition with **all** 5 self-assessments. Optional: the 5 books.

## 5. Certificate of completion (Custom certificate)

1. In the section "Assessment and certificate", add **Custom certificate** using the **platform's standard template** (no background image): name "Certificate of completion".
2. **Restrict access:** one "Activity completion" condition for each of the 5 self-assessments, "must be marked complete and pass", and the **Final survey** submitted.
3. In the template change only these data (also in `6_certificate/certificate.md`):

   | Field | Text |
   |---|---|
   | Course title | Your Money, Your Family, Your Future |
   | Line | for completing the financial well-being program Your Money, Your Family, Your Future |
   | Topic 1 | My money |
   | Topic 2 | Financial system |
   | Topic 3 | Credit and debt |
   | Topic 4 | Protection |
   | Topic 5 | Future and wealth |

4. Check the **PDF preview** and turn on "Verify certificate".

If Custom certificate is not installed, the **Complete plan · Your Money** badge works as a digital certificate.

## 6. What not to do

- Do not give points for viewing pages.
- Do not post names in rankings.
- Do not ask for real data to pass.
- Do not tie badges or the certificate to buying services or products.
