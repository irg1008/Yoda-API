FROM python:3.9.8-slim

ENV PYTHONUNBUFFERED=1 
EXPOSE 8000
WORKDIR /app

COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Download packages folder to install model.
RUN pip install gdown
RUN gdown --folder "1vm17O0m1M1bvnp_yhHmzgOuVoOTAN1kD" -O ./models

COPY ./src ./src

CMD exec gunicorn --bind :$PORT --workers 2  --timeout 0 --chdir src main:app