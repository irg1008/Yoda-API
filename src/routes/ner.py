from fastapi import APIRouter, HTTPException
from lib.ner import NerController, Entities

router = APIRouter()
ner_controller: NerController


@router.on_event("startup")
async def startup():
    global ner_controller
    ner_controller = NerController()


@router.get(
    "/ents",
    description="Get title entities",
    response_model=Entities,
    response_model_exclude_none=True,
)
async def get_entities(title: str):
    if not title:
        raise HTTPException(status_code=400, detail="Provide a valid title")

    return ner_controller.infer(title)
