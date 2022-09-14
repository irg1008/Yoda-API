from fastapi import APIRouter, Depends
from lib.ner import Entities, NerController
from utils.validation import check_title

ner_controller = NerController()
router = APIRouter(dependencies=[Depends(ner_controller)])


@router.get(
    "/ents",
    description="Get title entities",
    response_model=Entities,
    response_model_exclude_none=True,
)
async def get_entities(title: str = Depends(check_title)):
    return ner_controller.infer(title)
