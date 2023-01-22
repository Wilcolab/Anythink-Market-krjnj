from fastapi import APIRouter

router = APIRouter()

@router.get("/", status_code=200)
async def home():
    return "Anythink backend is up."

@router.get("/health", status_code=200)
async def health():
    return "OK"
