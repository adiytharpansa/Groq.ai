from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

class Prompt(BaseModel):
    prompt: str

# Embedded Groq API key
GROQ_API_KEY = "gsk_ATu2dQY6QwqsKcZopQOQWGdyb3FYxKCznkjwCGzfpevcoxpH"

headers = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}

@app.get("/")
def root():
    return {"status": "Bot AI FastAPI aktif"}

@app.post("/ask")
def ask(prompt: Prompt):
    data = {
        "model": "llama3-8b-8192",
        "messages": [
            {"role": "system", "content": "Kamu adalah asisten cerdas."},
            {"role": "user", "content": prompt.prompt}
        ]
    }
    response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=data)
    return response.json()
