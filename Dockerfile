# Start from a Python base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the downloader script and run it to "bake" the model into the image
COPY ./src/download_model.py .
RUN python download_model.py

# Copy the rest of your application code
COPY ./src /app/src

# Expose the port the API will run on
EXPOSE 8000

# Command to start the Uvicorn server
CMD ["uvicorn", "src.api:app", "--host", "0.0.0.0", "--port", "8000"]