from fastapi import APIRouter
from routes import fits, fits_controller
from utils.auth import api_key_dep
from utils.models import Model


router = APIRouter(dependencies=[api_key_dep])
# router.include_router(ner, prefix="/ner", tags=["NER"])
router.include_router(fits, prefix="/fits", tags=["FITS"])


class Status(Model):
    ner_loaded: bool = False
    fits_loaded: bool = False


@router.get(
    "/status",
    tags=["Status"],
    description="Get status of server",
    response_model=Status,
    response_model_exclude_none=True,
)
def get_status() -> Status:
    return Status(
        ner_loaded=ner_controller.loaded,
        fits_loaded=fits_controller.loaded,
    )
