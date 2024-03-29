from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from utils.fastapi import simplify_op_id

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
    {
        "name": "Status",
        "description": "Information about the current services",
    },
]


app = FastAPI(
    openapi_tags=tags_metadata,
    openapi_url="/docs/json",
    docs_url="/docs",
    redoc_url=None,
    title="Yoda API",
    description="AI powered API for ecommerce feed optimization. We create short title from product titles and extract product attributes from product descriptions.",
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

# Simplify operations IDs
simplify_op_id(app)
