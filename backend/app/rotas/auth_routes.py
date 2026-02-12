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

router = APIRouter()



 