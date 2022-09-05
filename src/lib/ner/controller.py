from .service import NerService
from .models import Entities
from os import path


class NerController:
    def __init__(self):
        model_path = path.abspath(
            path.join(
                path.dirname(__file__),
                "../../../models",
                "ner",
                "lite",
                "best_model.pt",
            )
        )
        self.service = NerService(model_path)

    def infer(self, text: str) -> Entities:
        return self.service.infer(text)
