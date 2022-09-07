from lib.fits.service import FitsService
from .models import Completion


class FitsController:
    def __init__(self) -> None:
        self.service = FitsService()

    def get_completion(self, text: str) -> Completion:
        title, price = self.service.infer(text)
        return Completion(title=title, estimated_price=price)
