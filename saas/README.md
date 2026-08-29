# SaaS Application

A lightweight SaaS application designed to demonstrate the deployment of a Python-based application on **Vercel**.

This project is part of the [`genai_vercel_deployment`](../) repository and contains the standalone SaaS application along with the configuration required for Vercel deployment.

---

## 📁 Project Structure

```text
saas/
│
├── app.py
├── requirements.txt
├── vercel.json
├── .gitignore
└── README.md
```

### File Description

| File               | Description                                     |
| ------------------ | ----------------------------------------------- |
| `app.py`           | Main Python application                         |
| `requirements.txt` | Python dependencies required by the application |
| `vercel.json`      | Vercel deployment configuration                 |
| `.gitignore`       | Files and folders excluded from Git             |
| `README.md`        | Documentation for the SaaS application          |

---

## 🚀 Features

* Python-based SaaS application
* Simple and lightweight project structure
* Vercel-ready deployment configuration
* Dependency management using `requirements.txt`
* Easy local development and deployment

---

## 🛠️ Technologies Used

* **Python**
* **Vercel**
* **Flask / Python Web Framework**
* **Git & GitHub**

---

## 💻 Local Setup

### 1. Clone the Repository

```bash
git clone https://github.com/manasranjanmeher99/genai_vercel_deployment.git
cd genai_vercel_deployment/saas
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment:

**Windows:**

```bash
venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python app.py
```

The application should then be available at the local address configured by the application.

---

## ☁️ Deploy to Vercel

This project includes a `vercel.json` file containing the configuration required for deployment.

### Deploy using Vercel CLI

Install the Vercel CLI:

```bash
npm install -g vercel
```

Then run:

```bash
vercel
```

Follow the prompts to configure and deploy the application.

For production deployment:

```bash
vercel --prod
```

---

## 🔐 Environment Variables

If the application requires API keys or other secrets, store them as environment variables rather than committing them to Git.

For local development, you can use a `.env` file:

```env
GEMINI_API_KEY=your_api_key
```

Make sure `.env` is included in `.gitignore`.

For Vercel deployment, add the required variables through the project's Vercel environment-variable settings.

---

## 📦 Dependencies

All Python dependencies are listed in:

```text
requirements.txt
```

Install them with:

```bash
pip install -r requirements.txt
```

When adding a new dependency, update the requirements file accordingly.

---

## 🔄 Deployment Workflow

The recommended workflow is:

```text
Local Development
       │
       ▼
   Test App
       │
       ▼
   Git Commit
       │
       ▼
   GitHub Repository
       │
       ▼
     Vercel
       │
       ▼
 Production Deployment
```

---

## 📌 Repository Structure

The complete parent repository contains two deployment projects:

```text
genai_vercel_deployment/
│
├── genai_deployment/
│   ├── backend/
│   ├── frontend/
│   ├── .gitignore
│   ├── README.md
│   ├── requirements.txt
│   └── vercel.json
│
└── saas/
    ├── .gitignore
    ├── app.py
    ├── requirements.txt
    ├── vercel.json
    └── README.md
```

The **`genai_deployment`** folder contains the GenAI application deployment, while **`saas`** contains the standalone SaaS application.

---

## 📝 Notes

* Do not commit API keys, passwords, tokens, or other secrets.
* Keep dependencies updated in `requirements.txt`.
* Test the application locally before deploying.
* Keep `vercel.json` synchronized with the application's deployment requirements.

---

## 👨‍💻 Author

**Manas Ranjan Meher**

---
