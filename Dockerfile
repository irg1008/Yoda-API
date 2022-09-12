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

CMD ["gunicorn", "--chdir", "src", "main:app", "-w", "2", "-k", "uvicorn.workers.UvicornWorker", "-t", "120", "--bind", "0.0.0.0"]