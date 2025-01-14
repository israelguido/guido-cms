from abc import ABC, abstractmethod
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Base para os modelos ORM
Base = declarative_base()

class AbstractDatabase(ABC):
    def __init__(self, db_type: str, username: str, password: str, host: str, port: int, database: str):
        self.db_type = db_type
        self.username = username
        self.password = password
        self.host = host
        self.port = port
        self.database = database
        self.engine = self._create_engine()
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    @abstractmethod
    def get_connection_url(self) -> str:
        """Constrói a URL de conexão com base no tipo do banco de dados."""
        pass

    def _create_engine(self):
        connection_url = self.get_connection_url()
        return create_engine(connection_url)

    def get_session(self):
        """Retorna uma sessão para realizar operações no banco de dados."""
        return self.SessionLocal()

    def create_tables(self):
        """Cria as tabelas no banco de dados."""
        Base.metadata.create_all(bind=self.engine)

    def drop_tables(self):
        """Remove as tabelas do banco de dados."""
        Base.metadata.drop_all(bind=self.engine)


# Implementações para bancos de dados específicos
class MySQLDatabase(AbstractDatabase):
    def get_connection_url(self) -> str:
        return f"mysql+pymysql://{self.username}:{self.password}@{self.host}:{self.port}/{self.database}"

class PostgreSQLDatabase(AbstractDatabase):
    def get_connection_url(self) -> str:
        return f"postgresql://{self.username}:{self.password}@{self.host}:{self.port}/{self.database}"

class OracleDatabase(AbstractDatabase):
    def get_connection_url(self) -> str:
        return f"oracle+cx_oracle://{self.username}:{self.password}@{self.host}:{self.port}/{self.database}"

class SQLiteDatabase(AbstractDatabase):
    def get_connection_url(self) -> str:
        # O SQLite utiliza apenas o caminho do arquivo do banco
        return f"sqlite:///{self.database}"