from .service import NerService
from .models import Entities
from os import path
from utils.controller import Controller


class NerController(Controller):
    def _load(self):
        model_path = path.abspath(
            path.join(path.dirname(__file__), "../../../models/ner/lite/best_model.pt")
        )
        self.service = NerService(model_path)
        print("NER loaded and ready to go!")

    def infer(self, text: str) -> Entities:
        return self.service.infer(text)
