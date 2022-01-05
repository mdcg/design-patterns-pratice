from abc import ABC, abstractmethod


class Database(ABC):
    def __init__(self, config):
        self.config = config
        self.conn = self.connect()

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def sanity_sake(self):
        pass


class Tester(ABC):
    def __init__(self, config):
        self.config = config

    @abstractmethod
    def connection(self):
        pass

    def test(self):
        db = self.connection()
        return db.sanity_sake()
