#!/bin/bash
# Azure App Service startup script for FastAPI

# Use PORT environment variable if set, otherwise default to 8000
PORT=${PORT:-8000}

echo "Starting FastAPI app on port $PORT..."

# Start uvicorn with the app
python3 -m uvicorn app.main:app --host=0.0.0.0 --port=$PORT