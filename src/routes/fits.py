from fastapi import APIRouter, Depends, HTTPException
from lib.fits import Completion, FitsController
from utils.validation import check_title

fits_controller = FitsController()
router = APIRouter(dependencies=[Depends(fits_controller)])


@router.get(
    "/completion",
    description="Get text completion",
    response_model=Completion,
)
async def get_completion(title: str = Depends(check_title)):
    try:
        completion = fits_controller.get_completion(title)
        return completion
    except Exception as e:
        raise HTTPException(status_code=429, detail="Too many requests to fits model")
