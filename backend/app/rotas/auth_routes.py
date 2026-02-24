"""
Rotas Publicas de autenticação

Todas as Regras de negocio estarão aqui.
"""

import secrets
from fastapi import APIRouter, HTTPException, status

from app.config import settings
from app.models.schemas import (
    RegisterUser,
    LoginRequest,
    ForgotPasswordRequest,
    TokenResponse,
    MessageResponse,
    ForgotPasswordResponse,
)

from app.services.database import (
    find_user_by_cpf,
    find_user_by_email,
    find_user_reset_token,
    insert_user,
    normalize_cpf,
    update_user,
)

from app.services.security import create_access_token, hash_password, verify_password

router = APIRouter(prefix="/auth", tags=["auth"])

# função Responsavel pela Criação do usuario
@router.post("/register", response_model=MessageResponse, status_code=status.HTTP_201_CREATED)
def register_user(data: RegisterUser):
    # Verifica se senha e confirmação de senha são iguais
    if data.senha != data.confirma_senha:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Senha e Confirma senha não conferem.",
        )
    # Normaliza CPF e verifica se já está cadastrado
    cpf_normalized = normalize_cpf(data.cpf)
    if find_user_by_cpf(cpf_normalized):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="CPF já cadastrado.",
        )
        # Verifica se email já está cadastrado
    if find_user_by_email(data.email):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email já cadastrado.",
        )

    user_data = data.model_dump()
    user_data.pop("confirma_senha")  # Remove o campo de confirmação
    user_data["cpf"] = cpf_normalized
    user_data["email"] = data.email.lower().strip()
    user_data["senha"] = hash_password(data.senha)
    user_data["ativo"] = True  # Define o usuário como ativo por padrão

    insert_user(user_data)

    return {"message": "Usuário criado com sucesso!"}

# Fução responsavel por fazer o login do usuario
@router.post("/login", response_model=TokenResponse)
def login_user(data: LoginRequest):
    # Verifica se email existe
    user = find_user_by_email(data.email)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuário não encontrado.",
        )

    # Verifica se senha está correta
    if not verify_password(data.senha, user["senha"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Senha incorreta.",
        )

    # Verifica se usuário está ativo
    if not user.get("ativo", False):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuário não está ativo.",
        )

    # Cria o token de acesso
    access_token = create_access_token(data={"sub": user["email"]})
    return {"access_token": access_token, "token_type": "bearer"}

# Função responsavel pela parte de esqueçeu a senha 
@router.post("/forgot-password", response_model=ForgotPasswordResponse)
def forgot_password(data: ForgotPasswordRequest):
    # Implementação futura
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED)

# Função responsavel por atualizar a senha
@router.post("/reset-password", response_model=MessageResponse)
def reset_password(token: str, password: str):
    # Implementação futura
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED)