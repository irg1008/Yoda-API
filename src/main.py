from fastapi import FastAPI, HTTPException
from services.inference import Inference, Entities
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Origins for development and production clients.
origins = ["http://localhost:3000"]


engine = Inference("lite")


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
    max_age=3600,
)


class InferenceModel(BaseModel):
    entities: Entities

    class Config:
        schema_extra = {
            "example": {
                "entities": {
                    "color": ["red", "blue"],
                    "size": ["s", "l", "43.5"],
                    "brand": ["Zara", "Adidas"],
                }
            }
        }


@app.get("/")
def read_root():
    return {"hello": "Yoda NER"}


@app.get(
    "/ents",
    tags=["ner"],
    description="Get text entities",
    response_model=InferenceModel,
)
async def ner(text: str) -> InferenceModel:
    if not text:
        raise HTTPException(status_code=400, detail="Provide a valid text")

    entities = engine.infer(text)

    return InferenceModel(entities=entities)
