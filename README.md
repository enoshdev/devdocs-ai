# 🤖 DevDocs AI

> Paste any Python function. Get instant explanation, docstring and improvement suggestions — powered by Groq LLaMA 3.1.

## 🔗 Live Demo
**[https://devdocs-ai.netlify.app](https://devdocs-ai.netlify.app)**

## ✨ Features
- 💡 Plain English explanation of what your code does
- 📄 Auto-generated Google-style docstring
- ⚡ 3 specific numbered improvement suggestions
- 📋 One-click copy for generated docstring
- ⌨️ Ctrl + Enter keyboard shortcut

## 🛠 Tech Stack
| Layer | Technology |
|-------|-----------|
| Backend | Python, FastAPI |
| AI | Groq API — LLaMA 3.1 |
| Frontend | HTML, CSS, JavaScript |
| Deployment | Hugging Face Spaces + Netlify |

## 🚀 Run Locally

### Backend
```bash
cd backend
pip install -r requirements.txt
python -m uvicorn main:app --reload
```

### Frontend
Open `frontend/index.html` with Live Server in VS Code.

## 📁 Project Structure
devdocs-ai/
backend/
main.py          # FastAPI app + Groq AI integration
requirements.txt
Dockerfile       # For Hugging Face deployment
frontend/
index.html       # Full UI with particle animations
README.md

## 👨‍💻 Author
Built by **Enosh** — IT undergrad at Vasavi College of Engineering, Hyderabad

[![GitHub](https://img.shields.io/badge/GitHub-enoshdev-181717?style=flat&logo=github)](https://github.com/enoshdev)