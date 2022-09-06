from fastapi import APIRouter, HTTPException
from lib.ner import NerController, Entities

router = APIRouter()

ner_controller: NerController


@router.on_event("startup")
async def startup_event():
    global ner_controller
    ner_controller = NerController()


@router.get(
    "/ents",
    tags=["NER"],
    description="Get text entities",
    response_model=Entities,
)
async def ner(title: str):
    if not title:
        raise HTTPException(status_code=400, detail="Provide a valid title")

    return ner_controller.infer(title)