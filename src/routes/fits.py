from fastapi import APIRouter, Depends
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
    return fits_controller.get_completion(title)
