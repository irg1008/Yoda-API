from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from db import api_keys

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def api_key_auth(key: str = Depends(oauth2_scheme)):
    api_key = await api_keys.find_one({"api_key": key})
    if not api_key:
        raise HTTPException(status_code=401, detail="Invalid API key")
    return key


api_key_dep = Depends(api_key_auth)
