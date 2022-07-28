FROM python:3.9.8-slim

ENV PYTHONUNBUFFERED 1 
EXPOSE 8000
WORKDIR /app

COPY ./requirements.txt .
COPY ./src ./src

# Download packages folder to install model.
RUN pip install gdown
RUN gdown --no-cookies --folder "1MMJrkXZEVR6PBfbx-nPLZQX_DXgIUHS-" -O ./packages 

RUN pip install -r requirements.txt

RUN rm -rf ./packages

WORKDIR /app/src
CMD ["gunicorn", "-w", "4", "-b", ":8000", "main:app"]