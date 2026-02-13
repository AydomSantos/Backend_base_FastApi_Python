"""
Rotas Publicas de autenticação

Todas as Regras de negocio estarão aqui.
"""

import secrets
from fastApi import APIRouter, HTTPException, status

from app.config import settings
from app.models.schemas import {
    RegisterUser,
    LoginRequest,
    ForgotPasswordRequest,
    TokenResponse,
    MensageResponse,
    ForgotPasswordResponse,
    HomeResponse,
}

from app.services.database import {
    find_user_by_cpf,
    find_user_by_email,
    find_user_reset_password_token,
    insert_user,
    normalize_cpf,
    update_user,
}

from app.services.security import craete_access_token, hash_password, verify_password

router = APIRouter(prefix="/auth", tags=["auth"])

def register_user(data: RegisterUser) -> dict:
    try {
        if data.senha != data.confirmar_senha:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Senha e Confirma senha não conferem.",
        )
        cpf_normalized = normalize_cpf(data.cpf)
        if find_user_by_cpf(cpf_normalized):
            raise HTTPException(
            status_code=status.HTTP_409_BAD_REQUEST,
            detail="CPF já cadastrado.",
        )
    
        if find_user_by_email(data.email):
        raise HTTPException(
            status_code=status.HTTP_409_BAD_REQUEST,
            detail="Email já cadastrado.",
        )
    
    } catch (error) {
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error),
        )
    }
    


    




 