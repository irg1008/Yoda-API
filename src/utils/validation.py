from fastapi import HTTPException


async def check_title(title: str):
    if not title:
        raise HTTPException(status_code=400, detail="Provide a valid title")
    return title
