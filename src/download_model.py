# in src/download_model.py

from transformers import pipeline

print("Downloading sentiment analysis model...")

# This line will download and cache the model from the Hugging Face Hub.
pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

print("Model download complete.")