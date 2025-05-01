
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
```

### 3. Install Dependencies

* Each project has its own `requirements.txt` file. Install with:
* You can also install the top `requirements.txt` includes all the projects.

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

---

## 📬 Contributing

Have an idea for a mini-project? Fork this repo and add a new folder under `python_small_projects/`, or open a pull request with suggestions.

---
