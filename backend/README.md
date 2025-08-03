# HTS Co-pilot Backend

FastAPI backend for the HTS Co-pilot application.

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

4. Run the development server:
```bash
uvicorn main:app --reload
```

## API Endpoints

- `GET /` - Health check
- `GET /health` - Detailed health status
- `GET /api/status` - API status and available endpoints
- `GET /docs` - Interactive API documentation (Swagger UI)
- `GET /redoc` - Alternative API documentation

## Development

- **Code formatting**: `black .`
- **Import sorting**: `isort .`
- **Linting**: `flake8 .`
- **Testing**: `pytest`

## Deployment

This backend is designed to be deployed to AWS Lambda using the serverless framework. 