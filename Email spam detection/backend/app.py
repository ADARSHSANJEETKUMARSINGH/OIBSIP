from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import pickle
import os

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(BASE_DIR, "..", "model", "model.pkl")
vectorizer_path = os.path.join(BASE_DIR, "..", "model", "vectorizer.pkl")
frontend_path = os.path.join(BASE_DIR, "..", "frontend", "index.html")

# Load
model = pickle.load(open(model_path, "rb"))
vectorizer = pickle.load(open(vectorizer_path, "rb"))

# Serve frontend
@app.get("/")
def serve_frontend():
    return FileResponse(frontend_path)

# Schema
class Message(BaseModel):
    text: str


def keyword_boost(text: str) -> int:
    spam_keywords = [
        "gift card",
        "deal",
        "buy now",
        "exclusive",
        "limited time offer",
        "win free",
        "free tickets"
    ]

    text = text.lower()

    return int(any(word in text for word in spam_keywords))

# Prediction
@app.post("/predict")
def predict(msg: Message):
    
    data = vectorizer.transform([msg.text])
    model_pred = model.predict(data)[0]

    # keyword boost
    keyword_pred = keyword_boost(msg.text)

    # 🔥 Smart fusion (NOT aggressive)
    if model_pred == 1:
        final = 1
    elif keyword_pred == 1:
        final = 1
    else:
        final = 0

    result = "Spam" if final == 1 else "Not Spam"

    return {"prediction": result}