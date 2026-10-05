# Activities, points, badges and certificate guide · Your Business, Your Money, Your Future · U.S.

This guide is for Moodle 3.10 with Level Up (block_xp) 3.15.2 and the Custom certificate plugin (mod_customcert).

The goal is to motivate without competing. Points reward progress, not perfect scores. Nobody's name is ever shown in a table.

## 1. What each module has

| Activity | How many | Completion |
|---|---|---|
| Book "Module N lessons" | 1 per module (9) | View |
| H5P activity "MN UYY · What would you do?" | 1 per lesson (45) | Receive a grade |
| Quiz "Module N self-assessment" | 1 per module (9) | Passing grade of 70% |

**Each H5P activity:** no download button, copyright button on, embed off; attempt tracking with "Highest grade"; completion "Student must receive a grade".

**Self-assessments:** use the bank of 135 three-option questions with feedback, in categories *Your Business US EN v1.3/M1* to *M9*. Passing grade 70%, unlimited attempts, shuffled answers and review with the correct answer and feedback at the end.

## 2. Level Up: levels and points

**Rules** (*Level Up > Rules*):

1. Remove the default rules or set them to 0.
2. **For completing any activity:** 25 points, event "Course module completion updated" (`\core\event\course_module_completion_updated`).
3. **For posting in the forum:** 5 points, event "Post created" (`\mod_forum\event\post_created`).
4. Keep cheat guard on.

Completing the whole course gives about 1,575 points:

| Activities | How many | Points |
|---|---|---|
| H5P activities | 45 | 1,125 |
| Books | 9 | 225 |
| Self-assessments | 9 | 225 |
| **Total** | 63 | **1,575** |

**Levels** (6 levels, no automatic algorithm):

| Level | Name | Points | Reached around |
|---|---|---|---|
| 1 | Idea | 0 | On arrival |
| 2 | Launch | 200 | During Module 2 |
| 3 | Up and running | 400 | During Module 4 |
| 4 | Formal | 650 | During Module 5 |
| 5 | Growing | 900 | During Module 7 |
| 6 | Established | 1,100 | During Module 9 |

**Ladder:** anonymity on; show only nearby neighbors or turn it off.

## 3. Badges

*Course administration > Badges > Add a new badge*. Images in `5_badges/`. Issuer: Desarrolla Talento. Expiry: never. Names include the course so they're unique on the platform: use them exactly.

| Image | Badge | Criterion (activity completion, with passing grade) | Description |
|---|---|---|---|
| 01_separate_money.png | Separate money · Your Business US EN | Module 1 self-assessment | You separated business and household money and pay yourself a salary. |
| 02_fair_price.png | Fair price · Your Business US EN | Module 2 self-assessment | You know your costs, your margin and your break-even point. |
| 03_cash_flow_under_control.png | Cash flow under control · Your Business US EN | Module 3 and 4 self-assessments | You manage your cash flow, customer credit and payment methods without losing. |
| 04_formal_business.png | Formal business · Your Business US EN | Module 5 self-assessment | Your structure, numbers, permits and taxes are in order. |
| 05_smart_credit.png | Smart credit · Your Business US EN | Module 6 self-assessment | You know whether you need credit and what it really costs. |
| 06_protected_business.png | Protected business · Your Business US EN | Module 7 self-assessment | You protected your health, business and trademark, and you guard against scams. |
| 07_orderly_growth.png | Orderly growth · Your Business US EN | Module 8 and 9 self-assessments | You grow in an orderly way and have your one-page plan. |
| 08_full_plan.png | Full plan · Your Business US EN | Course completion | You completed all nine modules of the program. |

When done, **enable** each badge.

## 4. Course completion

*Course administration > Course completion*: activity completion condition with **all** 9 self-assessments. Optional: the 9 books.

## 5. Certificate of completion (Custom certificate)

1. In the section "Assessment and certificate", add **Custom certificate** using the **platform's standard template** (no background image): name "Certificate of completion".
2. **Restrict access:** one "Activity completion" condition for each of the 9 self-assessments, "must be marked complete and pass", and the **Final survey** submitted.
3. In the template change only these data (also in `6_certificate/certificate.md`):

   | Field | Text |
   |---|---|
   | Course title | Your Business, Your Money, Your Future · U.S. |
   | Line | for completing the financial well-being program Your Business, Your Money, Your Future · U.S. |
   | Topic 1 | Separate money |
   | Topic 2 | Price and cash flow |
   | Topic 3 | Taxes and formality |
   | Topic 4 | Credit and protection |
   | Topic 5 | Growth and future |

4. Check the **PDF preview** and turn on "Verify certificate".

If Custom certificate is not installed, the **Full plan · Your Business US EN** badge works as a digital certificate.

## 6. What not to do

- Do not give points for viewing pages.
- Do not post names in rankings.
- Do not ask for real data to pass.
- Do not tie badges or the certificate to buying services or products.
