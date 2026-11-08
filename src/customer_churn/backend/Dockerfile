FROM python:3.13.14-slim

WORKDIR /app

COPY . .

# Upgrade pip to the latest version and install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "10000"]