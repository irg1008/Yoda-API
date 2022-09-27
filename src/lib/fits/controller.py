from lib.fits.service import FitsService
from .models import Completion
from utils.controller import Controller


class FitsController(Controller):
    def _load(self):
        self.service = FitsService()
        print("FITS loaded and ready to go!")

    def get_completion(self, text: str) -> Completion:
        title = self.service.infer(text)
        # Remove last period if present
        if title[-1] == ".":
            title = title[:-1]
        return Completion(title=title, estimated_price=0.0)
