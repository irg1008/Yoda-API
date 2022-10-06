FROM python:3.9-slim

ENV PYTHONUNBUFFERED=True
ARG APP_DIR="/app"

WORKDIR $APP_DIR

COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src ./src

CMD exec gunicorn -b 0.0.0.0:$PORT -w 2 --threads 8 -k uvicorn.workers.UvicornWorker -t 0 --chdir src main:app --preload