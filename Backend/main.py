from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API de Rosaria Web"}

@app.get("/status")
def get_status():
    return {"status": "online", "version": "1.0.0"}
import google.generativeai as genai
import os
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

class Mensaje(BaseModel):
    texto: str

@app.post("/chat")
async def chat(mensaje: Mensaje):
    prompt = f"Eres RosarIA, una IA de Rosario Argentina. Responde corto, canchero y con onda rosarina: {mensaje.texto}"
    response = model.generate_content(prompt)
    return {"respuesta": response.text}
