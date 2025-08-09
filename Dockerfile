FROM python:3.11-slim

WORKDIR /app


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DATABASE_URL=${DATABASE_URL}

# Expose port
EXPOSE 8000

# Run using Python so we can read PORT env var
CMD ["python", "-m", "src.main"]
