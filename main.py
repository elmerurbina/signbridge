from fastapi import FastAPI, UploadFile, File
from app.services.hand_service import classify_hand_from_frame
from app.services.speech_service import recognize_speech

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API de Clasificador de Señales y Voz"}

@app.post("/api/hand-recognition")
async def hand_recognition(file: UploadFile = File(...)):
    image_bytes = await file.read()
    label = classify_hand_from_frame(image_bytes)
    return {"expression": label}

@app.get("/api/speech-recognition")
def speech_recognition():
    result = recognize_speech()
    return result
