from .types import FITSInferParameters, FITSInferPayload, FITSResponse
import requests
from decouple import config

HF_BASE_URL = "https://api-inference.huggingface.co/models"
HF_API_KEY = config("HF_API_KEY")
YODA_FITS_MODEL = str(config("YODA_FITS_MODEL"))


def query(payload: FITSInferPayload, url: str):
    request_url = f"{HF_BASE_URL}/{url}"
    headers = {"Authorization": f"Bearer {HF_API_KEY}"}
    response = requests.post(request_url, headers=headers, json=payload)
    return response.json()


class HFClient:
    def __init__(self) -> None:
        self.fits_url = YODA_FITS_MODEL

    def infer(self, text: str, params: FITSInferParameters) -> str:
        payload: FITSInferPayload = {
            "inputs": text,
            "options": {
                "wait_for_model": True,
                "use_gpu": True,
            },
            "parameters": params,
        }
        res: list[FITSResponse] = query(payload, self.fits_url)
        print(res)
        summary = res[0]["summary_text"]
        return summary
