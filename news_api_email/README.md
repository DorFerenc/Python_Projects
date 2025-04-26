# 📬 News API Email Aggregator

A simple Python script that fetches the latest news articles about **Tesla** from [NewsAPI.org](https://newsapi.org/) and prints their titles.
It also demonstrates safe API key handling with a `.env` file.

---

## 📁 Project Structure

```
news_api_email/
├── main.py
├── .env
├── .gitignore
└── README.md
```

---

## ⚙️ How to Use

1. **Clone this repository** to your local machine.

2. **Install dependencies** if you haven't already:
   ```bash
   pip install requests python-dotenv
   ```

3. **Create a `.env` file** in the root of the project, and add your News API key:
   ```
   API_KEY=your_actual_api_key_here
   ```

4. **Make sure `.env` is ignored by Git!**
   Add this line to your `.gitignore` file:
   ```
   .env
   ```

5. **Run the script**:
   ```bash
   python main.py
   ```

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

---