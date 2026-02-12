"""
Modelos de entrada e saida da API

- Esses modelos validam os dados automaticamente e deixam o codigo mais legivel
- Nosso login tera nome, cfp, email, senha e confirma senha

"""

from pydantic import BaseModel, EmailStr, Field

class RegisterUser(BaseModel):
    # Dados Recebidos para cadastrar um novo usuarío
    nome: str = Field(min_length=5, max_length=120)
    cpf: str = Field(min_length=11, max_length=14)
    email: EmailStr
    senha: str = Field(min_length=6, max_length=20)
    confirma_senha: str = Field(min_length=6, max_length=20)

class LoginRequest(BaseModel):
    # Dados Recebidos para autenticar o usuario
    email: EmailStr
    senha: str = Field(min_length=6, max_length=20)

class ForgotPasswordRequest(BaseModel):
    # Dados Recebidos para recuperar a senha
    email: EmailStr

class TokenResponse(BaseModel):
    # Resposta padrão de login contendo um token JWT
    access_token: str
    token_type: str = "bearer"

# model para emitir feadback visual 

class MensageResponse(BaseModel):
    #Resposta Simples de Mensagem
    mensagem: str

class ForgotPasswordResponse(BaseModel):
    """
    Resposta da rota "Esqueci a senha"
    o token_debug so aparece em ambiente de desenvolvimento local
    """
    mensagem: str
    token_debug: str | None = None

class HomeResponse(BaseModel):
    # Resposta para a rota inicial ou de boas-vindas
    mensagem: str
    usuario: str | None = None







