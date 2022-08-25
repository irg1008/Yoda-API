FROM python:3.9.8-slim

ENV PYTHONUNBUFFERED 1 
EXPOSE 8000
WORKDIR /app

COPY ./requirements.txt .
COPY ./src ./src

# Download packages folder to install model.
RUN pip install gdown
RUN gdown --folder "1j--I_KpFWw8HVmtFAHz3meEh5tPlhCup" -O ./models 

RUN pip install -r requirements.txt

CMD ["gunicorn", "--chdir", "src", "main:app", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "-t", "120", "--bind", "0.0.0.0"]