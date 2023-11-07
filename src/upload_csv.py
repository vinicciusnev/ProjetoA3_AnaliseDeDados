import pandas as pd
from sqlalchemy import create_engine

from models.DatabaseConfig import DatabaseConfig


def upload_csv():
    nome_arquivo = 'out.csv'

    data = pd.read_csv('files/' + nome_arquivo)

    config = DatabaseConfig()

    engine = create_engine('mysql+pymysql://' + config.get_connection_string())

    data.to_sql('faturamento_por_item', engine, if_exists='append', index=False)

    return "Dados carregados com sucesso", 200
