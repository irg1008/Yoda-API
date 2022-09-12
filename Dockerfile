FROM python:3.9.8-slim

ENV PYTHONUNBUFFERED=True
ARG MODELS_FOLDER_ID="1vm17O0m1M1bvnp_yhHmzgOuVoOTAN1kD"
ARG APP_DIR="/app"
ARG N_WORKERS=2

WORKDIR $APP_DIR

COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Download packages folder to install model.
RUN pip install gdown
RUN gdown --folder $MODELS_FOLDER_ID -O ./models

COPY ./src ./src

CMD exec gunicorn --bind 0.0.0.0:$PORT --workers $N_WORKERS -k uvicorn.workers.UvicornWorker --timeout 0 --chdir src main:app