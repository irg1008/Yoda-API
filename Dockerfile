FROM python:3.9.8-slim

ENV PYTHONUNBUFFERED 1 
EXPOSE 8000
WORKDIR /app

COPY ./requirements.txt .
COPY ./src ./src

RUN pip install -r requirements.txt

# Download packages folder to install model.
RUN gdown --folder "1MMJrkXZEVR6PBfbx-nPLZQX_DXgIUHS-" -O ./packages 

RUN rm -rf ./packages

WORKDIR /app/src
CMD ["uvicorn", "main:app", "--port", "8000", "--host", "0.0.0.0"]