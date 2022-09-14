from lib.fits.service import FitsService
from .models import Completion
from utils.controller import Controller


class FitsController(Controller):
    def _load(self):
        self.service = FitsService()
        print("FITS loaded and ready to go!")

    def get_completion(self, text: str) -> Completion:
        title, price = self.service.infer(text)
        return Completion(title=title, estimated_price=price)
