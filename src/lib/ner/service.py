import logging
import re

from lib.hf.client import HFClient
from lib.hf.types import TokenClassResponse
from utils.config import ner_model

from .models import Entities, Entity

logging.getLogger("flair").setLevel(logging.ERROR)


def is_valid(value):
    # Filter values with single non-alphanumeric character
    blacklist = r"^[^a-zA-Z0-9]$"
    return not re.match(blacklist, value)


def parse_response(res: list[TokenClassResponse]) -> Entities:
    entities: dict[str, Entity] = {}

    last_end = float("inf")
    last_group: str = ""

    for r in res:
        group, value, start, end = (
            r["entity_group"],
            r["word"].lower(),
            r["start"],
            r["end"],
        )
        ents = entities.get(group, [])

        if not is_valid(value):
            continue

        # Append word to previous entity if it's a continuation, if not add new entity
        if start - 1 == last_end and group == last_group:
            ents[-1] += f" {value}"
        else:
            ents.append(value)

        # Update values
        entities[group] = ents
        last_end = end
        last_group = group

    # Remove duplicated
    entities = {k: list(set(v)) for k, v in entities.items()}

    return Entities(**entities)


class NerService:
    def __init__(self):
        self.hf_client = HFClient.for_token_class(ner_model)

    def infer(self, text) -> Entities:
        res = self.hf_client.infer(text)
        return parse_response(res)
