
# 🐍 Python Small Projects Collection

This repository contains a curated set of small, practical Python projects designed for learning, automation, experimentation, and real-world application. Each project is self-contained and includes documentation, code, and dependencies where needed.

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/python_small_projects.git
cd python_small_projects
```

### 2. Navigate to a Project

```bash
cd news_api_email
# or
cd NLP_for_eBooks
```

### 3. Install Dependencies

* You can either install project-specific `requirements.txt` file.
* Or install the global one at the root of the repo:
```bash
pip install -r requirements.txt
```

---

## 🧠 Projects Overview

### `news_api_email/`
Fetches top 3 headlines for tech, science, and business from US & Israel using NewsAPI.org, formats them, and sends them via Gmail SMTP. Ideal for daily digests or news briefings.

- Uses: `requests`, `dotenv`, `smtplib`
- Includes rate limiting and fallback for limited results from IL
- Supports secure email sending via Gmail App Password

> 📬 Great for personal info digests or automation exercises.

### `NLP_for_eBooks/`
Analyzes diary entries using sentiment analysis (nltk) and displays visualized mood trends using streamlit and plotly.

- Uses: nltk, plotly, streamlit
- Reads .txt files from /diary
- Outputs sentiment graphs for positivity & negativity
---

## 📬 Contributing

Have an idea for a mini-project? Fork this repo and add a new folder under `python_small_projects/`, or open a pull request with suggestions.

---
