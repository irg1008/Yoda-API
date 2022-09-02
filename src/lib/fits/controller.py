from lib.fits.service import FitsService
from .models import FITSCompletion


class FitsController:
    def __init__(self) -> None:
        self.service = FitsService()

    def get_completion(self, text: str) -> FITSCompletion:
        completion, n_tokens = self.service.infer(text)
        price = self.service.get_infer_price(n_tokens)
        return FITSCompletion(
            completion=completion, estimated_price=price, price_unit="USD"
        )
