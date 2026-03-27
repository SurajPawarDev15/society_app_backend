FROM python:3.13

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip
RUN pip install -r backend/requirements.txt

EXPOSE 8000

ENV PYTHONPATH=/app:$PYTHONPATH

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "backend.wsgi:application"]