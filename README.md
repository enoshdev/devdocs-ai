# DevDocs AI

An AI-powered developer tool that instantly explains Python code, generates docstrings, and suggests improvements.

## Live Demo
[Coming soon after deployment]

## What It Does
- Paste any Python function
- Get plain English explanation
- Get a generated docstring
- Get 3 specific improvement suggestions

## Tech Stack
- Backend: Python, FastAPI, Groq API (LLaMA 3)
- Frontend: HTML, CSS, JavaScript
- Deployment: Render (backend), Netlify (frontend)

## Run Locally

### Backend
cd backend
pip install -r requirements.txt
python -m uvicorn main:app --reload

### Frontend
Open frontend/index.html with Live Server in VS Code

## Author
Built by Enosh — github.com/enoshdev