# in src/api.py

from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
import torch

# --- 1. Initialize FastAPI App ---
app = FastAPI(
    title="Sentiment Analysis API",
    description="An API to analyze the sentiment of a piece of text using a pre-trained Hugging Face model."
)

# --- 2. Load the Sentiment Analysis Pipeline ---
# This happens only once when the application starts.
sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

# --- 3. Define the Input Data Model ---
class TextInput(BaseModel):
    text: str

# --- 4. Create the Prediction Endpoint ---
@app.post("/analyze")
def analyze_sentiment(input_data: TextInput):
    """
    Analyzes the sentiment of the input text and returns the label and score.
    """
    text_to_analyze = input_data.text
    result = sentiment_pipeline(text_to_analyze)[0]
    
    return {
        "text": text_to_analyze,
        "label": result['label'],
        "score": result['score']
    }