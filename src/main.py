from decouple import config
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from lib.fits.controller import FitsController
from lib.fits.models import FITSModel
from lib.ner.inference import Inference
from lib.ner.models import NERInferenceModel

app = FastAPI()
ner_engine: Inference
fits_controller: FitsController

# Origins for development and production clients.
origins = ["http://localhost:3000"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
    max_age=3600,
)


@app.on_event("startup")
async def startup_event():
    global ner_engine, fits_controller
    ner_engine = Inference("ner")
    fits_controller = FitsController()


@app.get("/")
def read_root():
    return {"hello": "Yoda NER"}


@app.get(
    "/ents",
    tags=["ner"],
    description="Get text entities",
    response_model=NERInferenceModel,
)
async def ner(text: str) -> NERInferenceModel:
    if not text:
        raise HTTPException(status_code=400, detail="Provide a valid text")

    entities = ner_engine.infer(text)

    return NERInferenceModel(entities=entities)


@app.get(
    "/completion",
    tags=["fits"],
    description="Get text completion",
    response_model=FITSModel,
)
async def fits(text: str) -> FITSModel:
    if not text:
        raise HTTPException(status_code=400, detail="Provide a valid text")

    completion = fits_controller.get_completion(text)

    return FITSModel(completion=completion)
