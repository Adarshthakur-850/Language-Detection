from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import os
from src.preprocessing import preprocess_text

app = FastAPI(title="Language Detection API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

MODEL_PATH = "models/language_detector.pkl"
model = None

class TextRequest(BaseModel):
    text: str

@app.on_event("startup")
def load_model():
    global model
    if os.path.exists(MODEL_PATH):
        model = joblib.load(MODEL_PATH)
        print("Model loaded.")
    else:
        print("Model not found. Please train first.")

@app.post("/predict")
def predict_language(request: TextRequest):
    if not model:
        return {"error": "Model not loaded"}
    
    clean_text = preprocess_text(request.text)
    prediction = model.predict([clean_text])[0]
    probabilities = model.predict_proba([clean_text])[0]
    confidence = max(probabilities)
    
    return {
        "text": request.text,
        "language": prediction,
        "confidence": float(confidence)
    }
