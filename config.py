from datetime import timedelta

class Config:
    SECRET_KEY = 'sua_chave_secreta_supersegura'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///users.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'sua_chave_jwt_secreta_supersegura'
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=4)
    SWAGGER = {
        'title': 'API de Dados Vitivinícolas',
        'uiversion': 3
    }