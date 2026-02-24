from fastapi import APIRouter, Depends
from app.deps import get_current_user
from app.models.schemas import HomeResponse

router = APIRouter(prefix="/home", tags=["home"])

@router.get("", response_model=HomeResponse)
def home_endpoint(current_user: dict = Depends(get_current_user)):
    return {"message": "Hello World", "usuario": current_user.get("nome")}
