"""数据库工厂类，用于创建和管理不同类型数据库的连接和操作"""

from ..database.connectors import MySQLConnector, PostgreSQLConnector, SQLiteConnector
from ..operations import DatabaseOperations

class SQLFactory:
    def __init__(self, db_type):
        self.db_type = db_type
        self._connector = None
        self._operations = None

    def connect(self, **kwargs):
        if self.db_type == 'mysql':
            self._connector = MySQLConnector()
        elif self.db_type == 'postgresql':
            self._connector = PostgreSQLConnector()
        elif self.db_type == 'sqlite':
            self._connector = SQLiteConnector()
        else:
            raise ValueError(f"不支持的数据库类型: {self.db_type}")

        self._connector.connect(**kwargs)
        self._operations = DatabaseOperations(self._connector)

    def __getattr__(self, name):
        if self._operations is None:
            raise RuntimeError("请先调用connect方法建立数据库连接")
        return getattr(self._operations, name)

    def close(self):
        if self._connector:
            self._connector.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()