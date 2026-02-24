""""
dependencias reutilizaveis 

este arquivo concentra a logica de autenticação para usar em multiplas rotas 
"""

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.config import settings
from app.services.security import decode_access_token
from app.services.database import find_user_by_email

# esquema padrão para token Bearer no header Authorization

bearer_scheme = HTTPBearer(auto_error=False)

def get_current_user(credentials: HTTPAuthorizationCredentials | None = Depends(bearer_scheme), ):
    """
    Retorna o usuario autenticado a partir de JWT
    se o token ausente/invalido, retorna 401.
    """

    if not credentials:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token não informado.",
        )
    
    payload = decode_access_token(credentials.credentials)
    email = payload.get("sub")
    user = find_user_by_email(email)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuário não encontrado.",
    )
    return user






