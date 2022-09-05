from lib.fits.service import FitsService
from .models import Completion


class FitsController:
    def __init__(self) -> None:
        self.service = FitsService()

    def get_completion(self, text: str) -> Completion:
        title, n_tokens = self.service.infer(text)
        price = self.service.get_infer_price(n_tokens)
        return Completion(title=title, estimated_price=price, price_unit="USD")
