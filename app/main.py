from fastapi import FastAPI, WebSocket, Request, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from .services.hand_service import classify_hand_from_frame
from .services.speech_service import recognize_speech

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

# Static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.websocket("/ws/hand")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        try:
            frame_bytes = await websocket.receive_bytes()
            print("📷 Frame recibido - bytes:", len(frame_bytes))

            label = classify_hand_from_frame(frame_bytes)
            if label:
                print(f"🟢 Gesto detectado: {label}")
                await websocket.send_json({"gesture": label})
            else:
                print("🔴 Ningún gesto detectado.")
                await websocket.send_json({"gesture": "No se detectó gesto."})

        except Exception as e:
            print(f"❌ Error en WebSocket: {e}")
            await websocket.send_json({"error": str(e)})
            break


@app.get("/api/speech")
def get_speech():
    result = recognize_speech()
    return result


@app.post("/test_hand")
async def test_hand(file: UploadFile = File(...)):
    frame_bytes = await file.read()
    label = classify_hand_from_frame(frame_bytes)
    return {"gesture": label}
