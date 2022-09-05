from fastapi import APIRouter, HTTPException
from lib.fits import FitsController, FitsModel

router = APIRouter()

fits_controller: FitsController


@router.on_event("startup")
async def startup_event():
    global fits_controller
    fits_controller = FitsController()


@router.get(
    "/completion",
    tags=["fits"],
    description="Get text completion",
    response_model=FitsModel,
)
async def fits(text: str) -> FitsModel:
    if not text:
        raise HTTPException(status_code=400, detail="Provide a valid text")

    completion = fits_controller.get_completion(text)

    return FitsModel(completion=completion)
