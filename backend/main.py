from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from groq import Groq
from dotenv import load_dotenv
import os
import json
import re

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

class CodeInput(BaseModel):
    code: str

@app.get("/")
def home():
    return {"status": "DevDocs AI is running"}

@app.post("/analyze")
def analyze_code(input: CodeInput):
    prompt = f"""
You are an expert Python developer.
Analyze this Python code carefully.
You MUST respond with ONLY a valid JSON object. No extra text before or after.
No markdown. No backticks. Just raw JSON.

Use this exact structure:
{{
    "explanation": "write explanation here",
    "docstring": "write docstring here",
    "improvements": "write 3 improvements here"
}}

Python code to analyze:
{input.code}
"""
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.1,
        )

        content = response.choices[0].message.content.strip()

        content = re.sub(r'^```json\s*', '', content)
        content = re.sub(r'^```\s*', '', content)
        content = re.sub(r'\s*```$', '', content)
        content = content.strip()

        start = content.find('{')
        end = content.rfind('}') + 1
        if start != -1 and end != 0:
            content = content[start:end]

        result = json.loads(content)
        return result

    except Exception as e:
        return {
            "explanation": "Error analyzing code. Please try again.",
            "docstring": str(e),
            "improvements": "Make sure your code is valid Python."
        }