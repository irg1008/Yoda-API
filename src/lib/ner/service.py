from flair.data import Sentence
from flair.models import SequenceTagger
from os import path
from .models import Entities


class NerService:
    def __init__(self, model_path: str):
        self.model = self._load_model(model_path)

    def _load_model(self, model_path: str) -> SequenceTagger:
        if not path.exists(model_path):
            raise Exception(f"Model not found at {model_path}")
        return SequenceTagger.load(model_path)

    def _predict(self, text: str) -> Sentence:
        sentence = Sentence(text)
        self.model.predict(sentence)
        return sentence

    def _get_entities(self, sentence: Sentence) -> Entities:
        ents: Entities = {}

        for entity in sentence.get_spans("ner"):
            tag = entity.tag
            if not tag:
                continue

            # Creat entry if needed
            if tag not in ents:
                ents[tag] = []

            text = entity.text.lower()
            # Don't allow duplicates
            if text in ents[tag]:
                continue

            ents[tag].append(text)

        return ents

    def infer(self, text) -> Entities:
        sentence = self._predict(text)
        return self._get_entities(sentence)
