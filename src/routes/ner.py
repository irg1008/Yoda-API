from fastapi import APIRouter, HTTPException
from lib.ner import NerController, NerModel

router = APIRouter()

ner_controller: NerController


@router.on_event("startup")
async def startup_event():
    global ner_controller
    ner_controller = NerController()


@router.get(
    "/ents",
    tags=["ner"],
    description="Get text entities",
    response_model=NerModel,
)
async def ner(text: str) -> NerModel:
    if not text:
        raise HTTPException(status_code=400, detail="Provide a valid text")

    entities = ner_controller.infer(text)

    return NerModel(entities=entities)
