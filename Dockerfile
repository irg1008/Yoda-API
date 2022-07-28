FROM python:3.9.8-slim

ENV PYTHONUNBUFFERED 1 
# EXPOSE 8000
EXPOSE ${PORT}
WORKDIR /app

COPY ./requirements.txt .
COPY ./src ./src

# Download packages folder to install model.
RUN pip install gdown
RUN gdown --folder "1Qg265DJn2YYPMnJ3h3rWY_1mY-cNfOOj" -O ./packages 

RUN pip install -r requirements.txt

RUN rm -rf ./packages

WORKDIR /app/src
CMD ["uvicorn", "main:app", "--port", ${PORT}, "--host", "0.0.0.0"]