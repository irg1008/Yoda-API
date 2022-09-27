from .hf.client.hf import HFClient


class FitsService:
    def __init__(self):
        self.hf_client = HFClient()

    def infer(self, text: str) -> str:
        short_title = self.hf_client.infer(
            text,
            {
                "max_length": 25,
            },
        )
        return short_title
