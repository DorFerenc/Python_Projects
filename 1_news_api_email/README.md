# 📰 News Aggregator & Email Notifier

This Python project automatically fetches the top 3 headlines for **Technology**, **Science**, and **Business** categories from the **US and Israel**, using the [NewsAPI.org](https://newsapi.org/) service. The headlines are compiled into a neatly formatted message and sent to your email via **Gmail SMTP**.

It includes:
- Keyword fallback for Israel in case NewsAPI doesn’t return results by country.
- Basic rate limiting handling (`time.sleep`) to avoid 429 errors.
- Support for markdown-style article formatting including headline, description, URL, and thumbnail link.
- Secure use of `.env` for all secrets.

---

## 📁 Project Structure

```
news_api_email/
├── main.py            # Main script to fetch and send news
├── send_email.py      # Utility for sending emails via SMTP
├── .env               # Environment variables (not included in Git)
├── .gitignore         # Excludes .env from version control
└── README.md          # This file
```

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-user/news_api_email.git
cd news_api_email
```

### 2. Install dependencies

```bash
pip install requests python-dotenv
```

### 3. Set up `.env` file

Create a `.env` file in the root directory:

```
API_KEY=your_newsapi_api_key
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SENDER_EMAIL=your_email@gmail.com
EMAIL_PASSWORD=your_16_digit_gmail_app_password
```

> **Important:** You must use a [Gmail App Password](https://myaccount.google.com/apppasswords) — not your regular Gmail password.

### 4. Run the script

```bash
python main.py
```

You should see log messages like:
```
📡 Starting news aggregation...
Fetching: US - technology
...
📬 Email sent.
```

---

## 🛠 How it Works

- Connects to [NewsAPI.org](https://newsapi.org/) and fetches:
  - `country=us` with `category=technology|science|business`
  - `country=il` or fallback to `q=Israel` with same categories
- Formats articles (title, description, date, URL, image)
- Sends the formatted content via email using Gmail SMTP

---

## 🛡️ Security Notes

- Your `.env` file is not tracked by Git (see `.gitignore`).
- Never commit secrets (API key or email password) to public repositories.

---

## 📧 Sample Output (Email Body Snippet)

```
===== US - Technology =====
Elon Musk unveils new AI robot
2025-04-30T10:12:00Z
The Tesla CEO introduced a humanoid robot called Optimus...
https://example.com/article-url
[Image](https://example.com/image.jpg)
```

---

## ✨ Future Improvements

- HTML email formatting with inline images
- Logging to file
- Web dashboard or scheduled job runner

---

## 📌 Notes

- **API Key**: You can get a free API key by signing up at [https://newsapi.org/](https://newsapi.org/).
- **Rate Limiting**: A small delay (`time.sleep(1)`) is added to avoid sending too many requests quickly.
- **Headers**: A `User-Agent` is used to simulate a real browser request and avoid blocking.

---

## 🛡️ Best Practices Followed
- API keys are loaded securely using `dotenv`.
- Sensitive files are excluded from version control (`.gitignore`).
- Clean and understandable project structure.
- Ping email command: ```ping smtp-relay.brevo.com```
- [site for emails](https://app-smtp.brevo.com/real-time)
---