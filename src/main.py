from fastapi import FastAPI, HTTPException
from utils.docs import get_ents, Entities
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Origins for development and production clients.
origins = ["http://localhost:3000"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
    max_age=3600,
)


class EntitiesModel(BaseModel):
    entities: Entities


@app.get(
    "/ents",
    tags=["ner"],
    description="Get text entities",
    response_model=EntitiesModel,
)
async def ner(text: str) -> EntitiesModel:
    if not text:
        raise HTTPException(status_code=400, detail="Provide a valid text")

    ents = get_ents(text)

    return EntitiesModel(entities=ents)
