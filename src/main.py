from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api import router


tags_metadata = [
    {
        "name": "NER",
        "description": "Named Entity Recognition",
    },
    {
        "name": "FITS",
        "description": "First Intergalactic Title Shortener",
    },
]


app = FastAPI(
    openapi_tags=tags_metadata,
    openapi_url="/docs/json",
    docs_url="/docs",
    redoc_url=None,
    title="Yoda API",
    description="AI powered API for title summarization and entity extraction",
    version="0.1.0",
    swagger_ui_parameters={
        "docExpansion": "none",
        "defaultModelsExpandDepth": -1,
    },
)


@app.get("/", include_in_schema=False)
def root():
    return {"Yoda API": "Hi! Go to /docs for more information."}


# Main API router
app.include_router(router, prefix="/api")

# Origins for development and production clients.
origins = ["http://localhost:3000", "https://app.lighthousefeed.com"]
app.add_middleware(CORSMiddleware, allow_origins=origins)
