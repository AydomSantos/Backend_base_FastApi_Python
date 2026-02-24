from fastapi import FastAPI
from app.deps import get_current_user
from app.models.schemas import HomeResponse

router = APIRouter(prefix="/home", tags=["home"])

@router.get("", response_model=HomeResponse)
def home_endpoint(current_user=Depends(get_current_user)):
    _ = current_user
    return{"message": "Hello World"} 
