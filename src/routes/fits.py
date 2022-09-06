from fastapi import APIRouter, HTTPException
from lib.fits import FitsController, Completion

router = APIRouter()

fits_controller: FitsController


@router.on_event("startup")
async def startup_event():
    global fits_controller
    fits_controller = FitsController()


@router.get(
    "/completion",
    tags=["FITS"],
    description="Get text completion",
    response_model=Completion,
)
async def fits(text: str):
    if not text:
        raise HTTPException(status_code=400, detail="Provide a valid text")

    return fits_controller.get_completion(text)
