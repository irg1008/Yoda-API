from fastapi import APIRouter
from routes import fits, ner

router = APIRouter(prefix="/api")
router.include_router(ner, prefix="/ner")
router.include_router(fits, prefix="/fits")
