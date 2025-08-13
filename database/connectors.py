import mysql.connector
import psycopg2
import sqlite3
from . import DatabaseConnector

class MySQLConnector(DatabaseConnector):
    def connect(self, **kwargs):
        self.config.update(kwargs)
        self.connection = mysql.connector.connect(**self.config)
        self.cursor = self.connection.cursor()

class PostgreSQLConnector(DatabaseConnector):
    def connect(self, **kwargs):
        self.config.update(kwargs)
        self.connection = psycopg2.connect(**self.config)
        self.cursor = self.connection.cursor()

class SQLiteConnector(DatabaseConnector):
    def connect(self, **kwargs):
        self.config.update(kwargs)
        self.connection = sqlite3.connect(self.config.get('database', ':memory:'))
        self.cursor = self.connection.cursor()