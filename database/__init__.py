from abc import ABC, abstractmethod

class DatabaseConnector(ABC):
    def __init__(self):
        self.connection = None
        self.cursor = None
        self.config = {}

    @abstractmethod
    def connect(self, **kwargs):
        pass

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()