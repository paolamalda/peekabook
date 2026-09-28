# Level Up and Badges Guide

Proposed setup using what you already have in Moodle: H5P, Level Up (block_xp) and badges. The goal is to motivate without competition: points reward consistency and practice, not whoever knows the most.

## Principles

- **No public leaderboard with names.** Many participants prefer not to be visible. If you turn on the ladder, use anonymous mode or the mode that shows only nearby neighbors.
- **Reward finishing and practicing, not perfect scores.**
- **No points for screen time.** Reward completion.
- **Levels have names that tell a story of progress**, not ranks.

## Levels (Level Up)

Set up 6 levels, with the cumulative points each one requires:

| Level | Name | Cumulative points |
|---|---|---|
| 1 | Getting started | 0 |
| 2 | Getting organized | 300 |
| 3 | Using my account | 800 |
| 4 | Caring for my credit | 1,400 |
| 5 | Protecting my family | 2,100 |
| 6 | Building my future | 2,900 |

## Point rules

| Action | Points | How to set it up |
|---|---|---|
| Complete a lesson (page or book) | 20 | Activity completion rule* |
| Complete the H5P activity | 20 | Activity completion* |
| Pass the lesson quiz (70% or more) | 20 | Completion with passing grade* |
| Submit "Your plan" (Assignment) | 30 | "Submission created" event |
| Post in the questions forum | 5 (maximum 3 a day) | "Post created" event with a repetition limit |
| Complete a module | 100 | Section completion or course rule* |

\* Completion- and grade-based rules depend on the installed version. The free version of Level Up awards points by **events**, with basic rules. Rules by activity completion, grade and "section bonus" belong to **Level Up+**, which is paid. **To confirm:** check which options appear under *Level Up > Rules*.

**If you have the free version:** use the event rule "Course module completion updated" (course_module_completion_updated), filtered by the course. The list of available events depends on your version.

**Avoid double counting:** turn off points for "viewed" (course_module_viewed) or set them to 0, so opening and closing does not earn points.

**Estimated points for the full course:**

| Item | Calculation | Points |
|---|---|---|
| Lesson, H5P and quiz | 59 lessons × 60 | 3,540 |
| "Your plan" | 59 × 30 | 1,770 |
| Modules | 5 × 100 | 500 |
| **Total** | | **5,810** |

Levels are reached before finishing so that progress shows early. Adjust the thresholds if most people get stuck at one level.

## Badges (Moodle, Open Badges compatible)

Create the badges under *Course administration > Badges*. The criterion is completion of the activities listed.

| Badge | Criterion | Message |
|---|---|---|
| My money in order (M1) | Complete the 14 lessons and the M1 quiz | You organized your calendar, budget and tax folder. |
| Smart sender (M2) | Complete M2 | You know how to choose an account and compare remittances. |
| Credit on track (M3) | Complete M3 | You understand and care for your credit. |
| Protected family (M4) | Complete M4 | You have a protection and response plan. |
| Future in motion (M5) | Complete M5 | Your long-term plan is written down. |
| Scam detective | Pass the H5P in M4 U01 and M3 U04 with 90% or more | You recognize the signs of fraud. |
| Expert comparer | Complete the H5P in M2 U04, M2 U08 and M3 U05 | You compare using total cost. |
| Complete plan | All 5 module badges | Program certificate of participation. |

**Notes:**

- The "Complete plan" badge goes with the **certificate of participation**. It is not a professional certificate or accreditation.
- In each badge description, write the estimated hours and the skills practiced. That way it serves as evidence for the impact record.
- Turn on "Badges in Backpack" (Open Badges) only if participants ask for it. Sharing is voluntary.

## Activity completion (base setup)

| Activity | Completion condition |
|---|---|
| Lesson page or book | View |
| Ungraded H5P | View |
| Graded H5P | Receive a grade; passing grade 70% |
| Lesson quiz | Passing grade 70%, unlimited attempts, show feedback at the end |
| Your plan (Assignment) | Submit |

**For the quiz:** import `banco_preguntas_en.gift.txt` or `banco_preguntas_es.gift.txt` from *Question bank > Import > GIFT format*. Categories are created by module (M1 to M5), with 3 questions per lesson and 175 in total. Then create one quiz per lesson with that lesson's 3 questions.

## Data for the impact evaluation

Export the following every month, without names, using the internal Moodle ID:

- Points and level per person (Level Up > Report).
- Badges issued (Badges > Recipients).
- Completion per lesson (Reports > Activity completion).

This feeds indicators E01 to E06 of the master plan.
