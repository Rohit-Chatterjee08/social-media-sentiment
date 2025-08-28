# 💬 Social Media Sentiment Analyzer

An elegant web application that uses a state-of-the-art Transformer model to perform real-time sentiment analysis on any given text.

## Live Demo

You can try the live application here: **[Your Hugging Face Space URL]**

---

## Overview

This project provides a simple yet powerful tool for determining if a piece of text is **POSITIVE** or **NEGATIVE**. It's built using a modern, decoupled architecture where the user interface is separate from the machine learning model, making it scalable and maintainable.

The core of the application is a pre-trained **DistilBERT** model from the **Hugging Face Hub**, which has been fine-tuned for sentiment analysis.

**Key Features:**
-   **State-of-the-Art NLP:** Leverages a powerful, pre-trained Transformer model for high accuracy.
-   **Decoupled Architecture:** A standalone FastAPI backend serves the model, while a separate Gradio app provides the UI.
-   **Containerized Backend:** The API is packaged with Docker, making it portable and ready for cloud deployment.
-   **Modern UI:** Features a custom-built, high-contrast dark theme for a sharp and elegant user experience.

---

## Architecture

The application consists of two main components that communicate over an API:

1.  **Backend API:** A Python **FastAPI** service running in a **Docker** container. It loads the Hugging Face model and exposes an `/analyze` endpoint for predictions.
2.  **Frontend UI:** A **Gradio** application that provides a user-friendly interface. It sends the text entered by the user to the backend API and displays the returned sentiment.



---

## Technology Stack

-   **Backend & Modeling:** Python, FastAPI, Hugging Face Transformers, PyTorch, Docker
-   **Frontend:** Gradio, Requests
-   **Deployment:** Designed for cloud services like Google Cloud Run and Hugging Face Spaces.

---

## How to Run Locally

To run this project, you need two separate terminals. Ensure Docker Desktop is running first.

### 1. Run the Backend API

```bash
# Navigate to the project's root directory
cd sentiment-analyzer

# 1. Build the Docker image (this will download the model and may take time)
docker build -t sentiment-api .

# 2. Run the Docker container
docker run -p 8000:8000 sentiment-api
