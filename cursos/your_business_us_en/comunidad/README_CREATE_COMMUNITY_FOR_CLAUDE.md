# Instructions for Claude: create "Your Business Community · U.S." (Moodle 3.10)

You will create the course **Your Business Community · U.S.** on academia.desarrollatalento.com. It is a space separate from the course *Your Business, Your Money, Your Future · U.S.* (DT-NEGOCIO-US-EN). Don't touch other courses.

Rules:

- Use only the web interface.
- Do not use SSH.
- Do not install plugins.
- Do not change site settings.
- If anything doesn't match these instructions, stop and ask.

## 0. Before you start

1. Confirm that no course with the short name `DT-NEGOCIO-US-EN-COM` exists. If it does, stop and ask.
2. Ask the person for:
   - the date and link of the first monthly live session;
   - the WhatsApp channel link;
   If they don't have these, leave the text "[to be defined]" and report it.

## 1. Create the course

| Field | Value |
|---|---|
| Full name | Your Business Community · U.S. |
| Short name | DT-NEGOCIO-US-EN-COM |
| Visibility | **Show** |
| Enrolment | Self enrolment with the community's own enrolment key (Paola or the Archivist gives it to you; never write it in any file or report) |
| Format | Topics, 4 sections |
| Completion tracking | No |
| Show gradebook | No |
| Force language | English |
| Summary | "The community space for Your Business, Your Money, Your Future (U.S.): questions, announcements, tax dates, scam alerts, introduce your business, wins and a monthly live session." |

## 2. Sections and activities

### General · Welcome

1. The **Announcements** forum already exists (news forum). Set it up:
   - Name: `Announcements`.
   - Description: "Tax dates, reminders, scam alerts, monthly challenges and the monthly session. Only the team posts. Desarrolla Talento never asks for your SSN, ITIN, passwords, account numbers or immigration status."
   - Subscription: forced.
2. **Book** `Community guide`: chapter formatting "None". Book menu > Import chapter > `1_book/Comunidad_libro_Moodle.zip`, "Each HTML file represents one chapter" (6 chapters).
3. **URL** `WhatsApp announcements channel`: the link the person gives you; open in a new window. Description: "Only the team posts; nobody sees your number. Questions are answered in the forums."

### Section 1 · Take part

Create these forums. In **all** of them:

- Maximum number of attachments: **0**.
- Maximum attachment size: uploads not allowed.
- Grade: none. Ratings: off.
- Group mode: no groups.
- Subscription: optional.
- Copy this warning at the start of each description: "Don't post SSN, ITIN, EIN, passwords, account numbers, real amounts, screenshots of your bank or IRS account, or your immigration status."

| Name | Forum type | Description (after the warning) |
|---|---|---|
| What I want to achieve | Standard forum for general use | "In one sentence, what you want to achieve this year. No full name, personal data or real amounts." |
| Questions: money, price, cash flow and payments | Standard forum displayed in a blog-like format | "Modules 1 to 4. Use the template in chapter 3 of the guide." |
| Questions: taxes and formality | Standard forum displayed in a blog-like format | "Module 5. General orientation; review your case with a tax preparer or CPA. Immigration topics aren't covered. Use the template in chapter 3." |
| Questions: credit, protection, growth and future | Standard forum displayed in a blog-like format | "Modules 6 to 9. Use the template in chapter 3 of the guide." |
| Introduce your business | Standard forum for general use | "One post a month per person, with the template in chapter 3. No loans, investments or tax schemes." |
| Scam alerts | Standard forum for general use | "Warn about 'IRS' calls, government-imitation letters, overpayment checks or fake suppliers, without personal data. If it already affected you, follow M4 U03 and M7 U03." |
| Wins | Standard forum for general use | "Share your progress and the monthly challenges you completed." |

If your Moodle version doesn't show the "blog-like" type under that name, use "Standard forum for general use" and report it.

### Section 2 · Monthly live session

1. **Page** `Monthly live session`: copy the content of chapter 5 (first part) and add the date and link the person gave you.
2. **Choice** `What topic do you want for the next session?`:
   - Options: "Price and costs", "Cash flow and invoices", "Payments and selling scams", "LLC, EIN and permits", "Taxes and estimated payments", "Sales tax", "Credit", "Health and insurance", "Selling online", "Retirement".
   - Allow updating the answer: yes. Show results: after answering. Privacy: publish anonymous results.
3. **Feedback** `Community survey`, anonymous, with these questions:
   - Multiple choice: "How useful is the community to you?" (Very useful / Useful / Not very useful / Not useful).
   - Multiple choice: "Which space do you use most?" (Announcements / Question forums / Introduce your business / Alerts / Wins / Monthly session / WhatsApp channel).
   - Long text: "What topic would you like us to add to the course?"
   - Long text: "What would you improve about the community?"

### Section 3 · Commercial referrals

1. **Label** with this text: "Commercial referrals. Here we post services with a commercial agreement. Desarrolla Talento may receive a commission. Using them is voluntary and doesn't affect your access, points or certificate. Always compare with at least one other option (chapter 6 of the guide)."
2. **Forum** `Commercial referrals`, type "News forum" or, if another can't be added, "Standard forum for general use" with this restriction: in the forum's *Permissions*, remove the Student capabilities `mod/forum:startdiscussion` and `mod/forum:replypost`. If you can't change permissions, stop and ask.

## 3. Link from the main course

In the course **DT-NEGOCIO-US-EN**, General section, add a **URL** `Your Business Community · U.S.` to the new course, with the description: "Questions, tax dates, scam alerts, introduce your business and the monthly session."

## 4. Enrollment

- Enable **Self enrolment** in the community, role Student, with the community's own enrolment key (Paola or the Archivist gives it to you; never write it in any file or report). Report that it is active, without the key.
- Add the moderation team with the role **Non-editing teacher** (or Teacher, if the person asks).

## 5. Review (as a student)

- Attachments can't be added in the forums.
- The student can post in What I want to achieve, Questions, Introduce your business, Alerts and Wins.
- The student can't post in Announcements or Commercial referrals.
- The book shows 6 chapters.
- The choice and the survey work.

## 6. Report

Course link; list of forums with their settings; status of the choice and the survey; enrollment method; what was left "[to be defined]"; screenshots of the course's main page and of a forum showing the warning.

The course stays **visible**, with enrolment by key.
