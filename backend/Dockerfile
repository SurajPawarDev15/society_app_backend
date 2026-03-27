FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip
RUN pip install -r backend/requirements.txt

EXPOSE 8000

ENV PYTHONPATH=/app

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "backend.backend.wsgi:application"]