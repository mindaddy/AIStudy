from abc import ABC, abstractmethod

class Document(ABC):
    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def get_property(self):
        pass
