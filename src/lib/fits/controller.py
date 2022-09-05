from lib.fits.service import FitsService
from .models import FitsCompletion


class FitsController:
    def __init__(self) -> None:
        self.service = FitsService()

    def get_completion(self, text: str) -> FitsCompletion:
        title, n_tokens = self.service.infer(text)
        price = self.service.get_infer_price(n_tokens)
        return FitsCompletion(title=title, estimated_price=price, price_unit="USD")
