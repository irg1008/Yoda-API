from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from lib.fits import FitsController, FitsModel
from lib.ner import NerController, NerModel

app = FastAPI()
ner_controller: NerController
fits_controller: FitsController

# Origins for development and production clients.
origins = ["http://localhost:3000"]

# Add root as api and api versions routes as well

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
    global ner_controller, fits_controller
    ner_controller = NerController()
    fits_controller = FitsController()


@app.get("/")
def read_root():
    return {"hello": "Yoda NER"}


@app.get(
    "/ents",
    tags=["ner"],
    description="Get text entities",
    response_model=NerModel,
)
async def ner(text: str) -> NerModel:
    if not text:
        raise HTTPException(status_code=400, detail="Provide a valid text")

    entities = ner_controller.infer(text)

    return NerModel(entities=entities)


@app.get(
    "/completion",
    tags=["fits"],
    description="Get text completion",
    response_model=FitsModel,
)
async def fits(text: str) -> FitsModel:
    if not text:
        raise HTTPException(status_code=400, detail="Provide a valid text")

    completion = fits_controller.get_completion(text)

    return FitsModel(completion=completion)
