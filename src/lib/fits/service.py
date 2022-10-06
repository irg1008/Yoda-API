from lib.hf.client import HFClient
from utils.config import fits_model


class FitsService:
    def __init__(self):
        self.hf_client = HFClient.for_text_sum(fits_model)

    def infer(self, text: str) -> str:
        res = self.hf_client.infer(
            text,
            {"max_length": 25},
        )
        short_title = res[0]["summary_text"]
        return short_title
