# FastAPI Test

A minimal FastAPI application with a couple of endpoints.

## Endpoints
- `GET /` → Welcome message
- `GET /health` → Health check
- `POST /items` → Create an item (JSON body: `{ "name": "string", "price": 12.34, "in_stock": true }`)

## Setup

```bash
# From the project root
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Run the server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Visit:
- Swagger UI: http://localhost:8000/docs
- Redoc: http://localhost:8000/redoc
