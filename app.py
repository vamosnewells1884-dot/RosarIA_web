from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import google.generativeai as genai
import os
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

class Mensaje(BaseModel):
    texto: str

@app.get("/")
def root():
    return {"mensaje": "Bienvenido a RosarIA"}

@app.get("/status")
def status():
    return {"estado": "online"}

@app.post("/chat")
async def chat(msg: Mensaje):
    prompt = f"Sos RosarIA, una IA amable y útil; respondé esto: {msg.texto}"
    respuesta = model.generate_content(prompt)
    return {"respuesta": respuesta.text}
