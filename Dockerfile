FROM python:3.9.8-slim

ENV PYTHONUNBUFFERED=True
ARG MODELS_FOLDER_ID="1vm17O0m1M1bvnp_yhHmzgOuVoOTAN1kD"
ARG APP_DIR="/app"

WORKDIR $APP_DIR

COPY ./requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir

COPY ./models ./models

RUN pip install gdown
RUN gdown --folder $MODELS_FOLDER_ID -O ./models

COPY ./src ./src

CMD exec gunicorn -b 0.0.0.0:$PORT -w 2 -k uvicorn.workers.UvicornWorker -t 0 --chdir src main:app --preload