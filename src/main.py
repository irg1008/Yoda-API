from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api import router


app = FastAPI()
app.include_router(router)

# Origins for development and production clients.
origins = ["http://localhost:3000", "https://app.lighthousefeed.com"]

app.add_middleware(CORSMiddleware, allow_origins=origins)


@app.get("/", include_in_schema=False)
def root():
    return {"hello": "Yoda API"}
