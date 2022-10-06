from .types import (
    TParameters,
    TResponse,
    TextSumInferParameters,
    TextSumResponse,
    TokenClassInferParameters,
    TokenClassResponse,
    Payload,
)
from typing import Generic, Optional
import requests
from utils.config import HF_API_KEY, HF_BASE_URL


def query(payload: Payload, model_name: str):
    request_url = f"{HF_BASE_URL}/{model_name}"
    headers = {"Authorization": f"Bearer {HF_API_KEY}"}
    response = requests.post(request_url, headers=headers, json=payload)
    return response.json()


class HFClient(Generic[TParameters, TResponse]):
    def __init__(self, model_name: str) -> None:
        self.model_name = model_name

    @classmethod
    def for_text_sum(
        cls, model_name: str
    ) -> "HFClient[TextSumInferParameters, TextSumResponse]":
        return cls(model_name)  # type: ignore

    @classmethod
    def for_token_class(
        cls, model_name: str
    ) -> "HFClient[TokenClassInferParameters, TokenClassResponse]":
        return cls(model_name)  # type: ignore

    def _query(self, payload: Payload) -> list[TResponse]:
        return query(payload, self.model_name)

    def infer(self, text: str, params: Optional[TParameters] = None):
        payload = Payload(
            inputs=text,
            parameters=params,
            options={"use_gpu": False, "wait_for_model": True},
        )
        return self._query(payload)
