# in app.py

import gradio as gr
import requests
import json

# The URL where our FastAPI is running
API_URL = "http://127.0.0.1:8000/analyze"

# --- NEW: Custom CSS for a Sharp, High-Contrast Dark Theme ---
high_contrast_css = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

/* Main theme: dark background, light text */
body, #sentiment-app {
    background-color: #121212; /* Very dark grey */
    font-family: 'Inter', sans-serif;
    color: #e0e0e0; /* Light grey text */
}
#sentiment-app {
    background-color: #1e1e1e; /* Slightly lighter card background */
    border: 1px solid #333;
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
    border-radius: 12px;
}

/* Header styling */
#header h1 {
    color: #ffffff; /* White title */
    font-size: 2.25em;
    font-weight: 700;
}
#header p {
    color: #a0a0a0; /* Lighter grey for description */
    font-size: 1.1em;
}

/* Input textbox styling */
#input-textbox textarea {
    background-color: #2b2b2b;
    color: #ffffff;
    border: 1px solid #444;
    border-radius: 8px;
    font-size: 1.1em;
    padding: 12px;
}
#input-textbox textarea:focus {
    border-color: #6a0dad; /* Purple accent on focus */
}

/* Button styling: vibrant and clear */
#analyze-button {
    background-color: #8a2be2; /* Vibrant Blue-Violet */
    color: white;
    font-weight: 600;
    border: none;
    border-radius: 8px;
    padding: 12px 24px;
    transition: all 0.3s ease;
}
#analyze-button:hover {
    background-color: #9932cc; /* Darker Magenta */
    transform: scale(1.02);
    box-shadow: 0 0 15px rgba(138, 43, 226, 0.6);
}

/* Output Label styling */
#output-label .label-holder {
    background-color: #2b2b2b;
    border: 1px solid #444;
    border-radius: 8px;
}
#output-label .label-title {
    font-weight: 600;
    color: #a0a0a0;
}
#output-label .secondary-label {
    font-size: 1.2em;
    font-weight: 700;
    color: #ffffff; /* White for high contrast */
}
"""

def analyze_sentiment(text_input):
    """
    Sends text to the FastAPI and returns the predicted segment for the Label.
    """
    if not text_input:
        return {"Error": 1.0}
        
    payload = {"text": text_input}
    
    try:
        response = requests.post(API_URL, json=payload)
        response.raise_for_status()
        result = response.json()
        
        label = result.get("label", "N/A")
        score = result.get("score", 0)
        
        return {label: score, "Other": 1 - score}

    except requests.exceptions.RequestException as e:
        print(f"Error connecting to the API: {e}")
        return {"API Connection Error": 1.0}

# --- Build the Gradio App with the new UI ---
with gr.Blocks(css=high_contrast_css, elem_id="sentiment-app") as app:
    with gr.Column(elem_id="header"):
        gr.Markdown("<h1>Social Media Sentiment Analyzer</h1>")
        gr.Markdown("<p>Enter a sentence to analyze its sentiment. The tool will classify it as POSITIVE or NEGATIVE.</p>")

    # Input section
    input_textbox = gr.Textbox(
        lines=4,
        label="Enter Text for Analysis",
        placeholder="e.g., 'The new design is absolutely stunning!'",
        elem_id="input-textbox"
    )
    
    # Button to trigger the prediction
    analyze_button = gr.Button("Analyze Sentiment", elem_id="analyze-button")
    
    # Output section using the Label component for a clean look
    output_label = gr.Label(label="Sentiment Result", elem_id="output-label")
    
    # Connect the button to the function
    analyze_button.click(
        fn=analyze_sentiment,
        inputs=input_textbox,
        outputs=output_label
    )

app.launch()