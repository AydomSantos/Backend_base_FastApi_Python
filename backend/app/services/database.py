"""
Acessa ao Banco de dados TinyDB

- um banco no-sql baseado em arquivos JSON

"""

import tinydb

from app.config import settings 

# Instancia global do banco, apontando para um arquivo JSON
db = TinyDB(settings.database_path)

# Representando uma "tabela" que armazena usuario
user_table = db.Table("users")

def find_user_by_email(email: str):
    # Retorna usuario por email ou None, se não existir
    users_query = Query()
    return users_table.get(users_query.email == email.lower().strip())

def find_user_by_cpf(cpf: str):
    # Retorna usuario por cpf ou None, se não existir
    users_query = Query()
    return users_table.get(users_query.cpf == normalize_cpf(cpf))

def find_user_reset_token(token: str):
    # Busca Usuario pelo token de reculperação de senha
    users_query = Query()
    return users_table.get(users_query.reset_token == token)

def insert_user(user_data: dict):
    # Insere um novo usuario no banco
    users_table.insert(user_data)

def update_user(email : str, updates : dict):
    # Atualiza um usuario no banco
    users_query = Query()
    users_table.update(updates, users_query.email == email.lower().strip())

def normalize_cpf(cpf: str) -> str:
    # Remove caracteres não numericos do CPF
    # Exemplo : 123.456.789-00 -> 12345678900
    return "".join(char for char in cpf if char.isdigit())


