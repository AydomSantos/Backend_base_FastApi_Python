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

# função Responsavel pela Criação do usuario
def register_user(data: RegisterUser) -> dict:
    try {
        # Verifica se senha e confirmação de senha são iguais
        if data.senha != data.confirmar_senha:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Senha e Confirma senha não conferem.",
        )
        # Normaliza CPF e verifica se já está cadastrado
        cpf_normalized = normalize_cpf(data.cpf)
        if find_user_by_cpf(cpf_normalized):
            raise HTTPException(
            status_code=status.HTTP_409_BAD_REQUEST,
            detail="CPF já cadastrado.",
        )
         # Verifica se email já está cadastrado
        if find_user_by_email(data.email):
        raise HTTPException(
            status_code=status.HTTP_409_BAD_REQUEST,
            detail="Email já cadastrado.",
        )
    
    } catch (error) {
        # Captura qualquer erro inesperado e retorna como Bad Request
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error),
        )
    }
    
# Fução responsavel por fazer o login do usuario
def login_user(data: LoginRequest) -> TokenResponse:
    try {
        # Verifica se email existe
        if not (user := find_user_by_email(data.email)):
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
        if not user["ativo"]:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Usuário não está ativo.",
            )

    } catch(error){
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error),
        )
    }

# Função responsavel pela parte de esqueçeu a senha 
def forgot_password(data: ForgotPasswordRequest) -> ForgotPasswordResponse:
    try{

    }catch(error){
        raise HTTPException(
           status_code=status.HTTP_400_BAD_REQUEST,
           detail=str(error), 
        )
    }

# Função responsavel por atualizar a senha
def update_password(token: str, password: str) -> MensageResponse:
    try{

    } catch(error){
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error),
        )
    }
    




 