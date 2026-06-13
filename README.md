# Pulse MasterKit 🚀

Pulse MasterKit is an autonomous Python-based email automation bot that runs on GitHub Actions and delivers scheduled daily email reports without requiring a local machine to be running.

## 📌 Features

* Automated email delivery
* Runs entirely on GitHub Actions
* Secure credential management using GitHub Secrets
* Scheduled execution using Cron jobs
* No need to keep VS Code or laptop running
* Easy to customize for news, weather, quotes, reminders, and reports

## 🛠️ Tech Stack

* Python 3.11
* GitHub Actions
* Gmail SMTP
* GitHub Secrets

## 📂 Project Structure

```text
pulse-masterkit/
│
├── main.py
│
└── .github/
    └── workflows/
        └── daily.yml
```

## ⚙️ How It Works

1. GitHub Actions triggers the workflow based on a schedule.
2. The workflow starts a virtual machine.
3. Python executes `main.py`.
4. Email credentials are securely loaded from GitHub Secrets.
5. The email is sent automatically to the recipient.

## 🔐 Required GitHub Secrets

Create the following repository secrets:

| Secret Name | Description             |
| ----------- | ----------------------- |
| EMAIL_USER  | Sender Gmail address    |
| EMAIL_PASS  | Gmail App Password      |
| EMAIL_TO    | Recipient email address |

## 📧 Email Automation

The bot sends emails automatically using Gmail SMTP.

Example workflow:

```text
GitHub Actions
        ↓
Run Python Script
        ↓
Generate Email
        ↓
Send Email
        ↓
Recipient Inbox
```
<img width="925" height="620" alt="image" src="https://github.com/user-attachments/assets/f73b3246-c941-4b5a-9470-b50ae65e7cd8" />


## 🚀 Running Locally

Clone the repository:

```bash
git clone https://github.com/DevatheerthaKS/pulse-masterkit.git
cd pulse-masterkit
```

Run:

```bash
python main.py
```

## 🎯 Future Enhancements

* Daily news briefing
* Weather updates
* Motivational quotes
* AI-generated summaries
* Personalized reports
* Multi-user support

## 👩‍💻 Author

**Devatheertha K S**

B.Tech Computer Science Student
Muthoot Institute of Technology and Science

---

*"Automating daily communication through the power of Python and GitHub Actions."*

