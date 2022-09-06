from fastapi import APIRouter
from routes import fits, ner
from utils.auth import api_key_dep


router = APIRouter(prefix="/api", dependencies=[api_key_dep])
router.include_router(ner, prefix="/ner")
router.include_router(fits, prefix="/fits")
