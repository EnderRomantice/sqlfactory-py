"""数据库操作封装，提供基础的CRUD操作接口"""

from ..builders import SQLBuilder

class DatabaseOperations:
    def __init__(self, connector):
        self.connector = connector

    def execute(self, sql, params=None):
        self.connector.cursor.execute(sql, params or ())
        return self.connector.cursor

    def query(self, sql, params=None):
        cursor = self.execute(sql, params)
        return cursor.fetchall()

    def insert(self, table, data):
        sql, params = SQLBuilder.build_insert(table, data)
        self.execute(sql, params)
        self.connector.connection.commit()
        return self.connector.cursor.lastrowid

    def update(self, table, data, where):
        sql, params = SQLBuilder.build_update(table, data, where)
        self.execute(sql, params)
        self.connector.connection.commit()
        return self.connector.cursor.rowcount

    def delete(self, table, where):
        sql, params = SQLBuilder.build_delete(table, where)
        self.execute(sql, params)
        self.connector.connection.commit()
        return self.connector.cursor.rowcount