import mysql.connector as mc 
from mysql.connector import MySQLConnection
from dotenv import load_dotenv 
from os import getenv
from typing import Optional, Any, Tuple, List

class Database:
    def __init__(self) -> None:
        """Método construtor da classe Database."""	
        load_dotenv()
        self.host: str = getenv('DB_HOST')
        self.username: str = getenv('DB_USER')
        self.password: str = getenv('DB_PSWD')
        self.database: str = getenv('DB_NAME')
        self.connection: Optional[MySQLConnection] = None 
        self.cursor: Optional[List[dict]] = None 

    
    def __enter__(self) -> 'Database':
        """Método especial para permitir o uso do gerenciador de contexto."""
        self.conectar()
        return self
    
    
    def __exit__(self, exc_type: Optional[Any], exc_value: Optional[Any], exc_tb: Optional[Any]) -> None:
        """Método especial para garantir que a conexão seja encerrada."""
        self.desconectar()
        if exc_type is not None:
            print(f'Erro: {exc_value}')

    
    def conectar(self) -> None:
        """Estabelece uma conexão com o banco de dados."""
        try:
            self.connection = mc.connect(
                host = self.host,
                database = self.database,
                user = self.username,
                password = self.password
            )
            if self.connection.is_connected():
                self.cursor = self.connection.cursor(dictionary=True)
                print('Conexão ao banco de dados realizada com sucesso!')
        except Exception as e:
            print(f'Erro de conexão: {e}')
            self.connection = None
            self.cursor = None
            raise e

    
    def desconectar(self) -> None:
        """Encerra a conexão com o banco de dados e o cursor, se existirem."""
        
        if self.cursor:
            self.cursor.close()
        
        if self.connection:
            self.connection.close()

    
    def executar(self, sql: str, params: Optional[Tuple[Any, ...]] = None) -> Optional[List[dict]]:
        """Executa uma instrução no banco de dados."""
        
        if self.connection is None or self.cursor is None:
            print('Conexão ao banco de dados não estabelecida!')
            return None
        
        try:
            self.cursor.execute(sql, params)

            if sql.strip().upper().startswith('SELECT'):
                return self.cursor.fetchall()
            else:
                self.connection.commit()
                return self.cursor
            
        except Exception as e:
            print(f'Erro de execução: {e}')
            raise e
