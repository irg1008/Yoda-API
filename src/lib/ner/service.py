from .models import Entities, Entity
import logging

from lib.hf.client import HFClient
from lib.hf.types import TokenClassResponse
from utils.config import ner_model

logging.getLogger("flair").setLevel(logging.ERROR)


def parse_response(res: list[TokenClassResponse]) -> Entities:
    entities: dict[str, Entity] = {}

    last_end = float("inf")

    for r in res:
        group, value, start, end = r["entity_group"], r["word"], r["start"], r["end"]
        ents = entities.get(group, [])

        # Append word to previous entity if it's a continuation, if not add new entity
        if start - 1 == last_end:
            ents[-1] += f" {value}"
        else:
            ents.append(value)

        # Update values
        entities[group] = ents
        last_end = end

    return Entities(**entities)


class NerService:
    def __init__(self):
        self.hf_client = HFClient.for_token_class(ner_model)

    def infer(self, text) -> Entities:
        res = self.hf_client.infer(text)
        return parse_response(res)
