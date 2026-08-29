# GenAI Vercel Deployment

A collection of GenAI applications built with **Python, FastAPI, Google Gemini, HTML, CSS, and JavaScript**, with a focus on deploying AI-powered applications using **Vercel**.

This repository contains two projects:

* **`genai_deployment`** — a GenAI chatbot with a separate frontend and FastAPI backend.
* **`saas`** — a lightweight SaaS-style GenAI application designed for Vercel deployment.

---

## 📁 Repository Structure

```text
genai_vercel_deployment/
│
├── genai_deployment/
│   ├── backend/
│   │   ├── .env.example
│   │   ├── config.py
│   │   ├── gemini_service.py
│   │   └── index.py
│   │
│   ├── frontend/
│   │   ├── app.js
│   │   ├── index.html
│   │   └── style.css
│   ├── xcreenshots/
│   │
│   ├── requirements.txt
│   └── vercel.json
│
├── saas/
│   ├── app.py
│   ├── requirements.txt
│   └── vercel.json
│
├── .gitignore
└── README.md
```

---

# 🚀 Projects

## 1. `genai_deployment`

A full-stack GenAI chatbot application using a **FastAPI backend** and a separate **HTML/CSS/JavaScript frontend**.

### Features

* 🤖 Google Gemini-powered chatbot
* ⚡ FastAPI backend
* 💬 Chat interface
* 🎨 Responsive frontend
* 🌙 Dark/light theme support
* 🔄 New chat functionality
* ☁️ Vercel deployment configuration
* 🔐 Environment-variable based API key configuration

### Technology Stack

| Technology    | Purpose                 |
| ------------- | ----------------------- |
| Python        | Backend development     |
| FastAPI       | REST API                |
| Pydantic      | Request/data validation |
| Google Gemini | Generative AI           |
| HTML          | Frontend structure      |
| CSS           | Frontend styling        |
| JavaScript    | Frontend interaction    |
| Vercel        | Deployment              |

### Backend

The backend is responsible for receiving chat messages and communicating with the Gemini API.

Main files:

```text
genai_deployment/backend/
├── config.py
├── gemini_service.py
└── index.py
```

### Frontend

The frontend provides the user interface for interacting with the chatbot.

```text
genai_deployment/frontend/
├── index.html
├── style.css
└── app.js
```

### Local Setup

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r genai_deployment/requirements.txt
```

Create a `.env` file inside the backend directory:

```env
GEMINI_API_KEY=your_gemini_api_key
MODEL_NAME=gemini-3-flash-preview
```

Run the FastAPI application:

```bash
cd genai_deployment/backend
uvicorn index:app --reload --port 8000
```

The local API will be available at:

```text
http://127.0.0.1:8000
```

Chat endpoint:

```text
POST /api/chat
```

---

# 2. `saas`

The `saas` directory contains a lightweight GenAI SaaS-style application designed with **Vercel deployment** in mind.

### Features

* 🤖 GenAI integration
* 🐍 Python application
* ☁️ Vercel deployment configuration
* 📦 Dedicated Python dependencies
* 🧩 Simple structure suitable for extending into a larger SaaS product

### Technology Stack

| Technology    | Purpose             |
| ------------- | ------------------- |
| Python        | Application/backend |
| Google Gemini | Generative AI       |
| Vercel        | Deployment          |

### Structure

```text
saas/
├── app.py
├── requirements.txt
└── vercel.json
```

The `app.py` file contains the main application logic, while `requirements.txt` defines the Python dependencies and `vercel.json` contains the deployment configuration.

---

# 🔑 Environment Variables

API keys should **never be committed to GitHub**.

For local development, use a `.env` file:

```env
GEMINI_API_KEY=your_gemini_api_key
MODEL_NAME=gemini-3-flash-preview
```

The repository includes `.env.example` as a template.

> **Never replace the placeholder in `.env.example` with your real API key.**

For Vercel, add environment variables through the project's **Environment Variables** settings.

---

# ☁️ Deploying to Vercel

Both projects include Vercel configuration files.

Before deployment:

1. Push the repository to GitHub.
2. Import the repository into Vercel.
3. Select the appropriate project directory.
4. Configure the required environment variables.
5. Deploy the application.
6. Test the deployed API and frontend.

For `genai_deployment`, make sure the frontend uses the deployed API route rather than a localhost URL.

For example:

```javascript
fetch("/api/chat", {
    // ...
});
```

instead of:

```javascript
fetch("http://127.0.0.1:8000/api/chat", {
    // ...
});
```

---

# 🔒 Security

This repository uses an API key to communicate with Google Gemini.

Follow these security practices:

* Never commit `.env` files.
* Never put API keys directly inside frontend JavaScript.
* Use Vercel Environment Variables for production secrets.
* Keep `.env.example` limited to placeholder values.
* Rotate/revoke an API key immediately if it is accidentally exposed.
* Configure production CORS appropriately.

---

# 🛠️ Future Improvements

Possible improvements for both applications include:

* 👤 User authentication
* 💾 Conversation history
* 🗄️ Database integration
* ⚡ Streaming AI responses
* 📝 Markdown response rendering
* 🚦 API rate limiting
* 📊 Usage tracking
* 💳 SaaS subscription/payment integration
* 🧪 Automated tests
* 📝 Better logging and error handling
* 🔐 Improved production security

---

# 📚 Learning Goals

This repository can be used to demonstrate practical experience with:

* Generative AI application development
* Google Gemini API integration
* FastAPI
* REST APIs
* Frontend/backend integration
* Environment-variable management
* Vercel deployment
* Structuring AI applications for production

---

## ⭐ Acknowledgements

Built as a learning and development project for exploring **Generative AI, FastAPI, and Vercel deployment**.
