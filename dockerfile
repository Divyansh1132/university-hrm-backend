FROM python:3.13-slim

# Install only what's needed for PostgreSQL + Python
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc libpq-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy requirements first → Docker cache optimization
COPY requirements.txt ./

# Install with pip (fast, reliable, no uv PATH issues)
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY . .

EXPOSE 8000

# Auto-run migrations + start server
CMD ["sh", "-c", "alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port 8000"]