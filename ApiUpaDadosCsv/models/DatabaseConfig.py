import os

class DatabaseConfig:
    def __init__(self, userLogin='root', host='localhost', port=3306, dbName='faturamento_hospital_a3'):
        self.userLogin = userLogin
        self.password = self.get_password_from_env()  # Obter a senha do ambiente
        self.host = host
        self.port = port
        self.dbName = dbName

    def get_password_from_env(self):
        return os.environ.get('PASSWORD_BANCO_PESSOAL_MYSQL')

    def get_connection_string(self):
        return f"{self.userLogin}:{self.password}@{self.host}:{self.port}/{self.dbName}"
