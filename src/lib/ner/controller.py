from .service import NerService
from .models import Entities
from os import path
from utils.controller import Controller


class NerController(Controller):
    def _load(self):
        self.service = NerService()
        print("NER loaded and ready to go!")

    def infer(self, text: str) -> Entities:
        return self.service.infer(text)
