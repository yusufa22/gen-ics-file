from abc import ABC, abstractmethod

class Uploader(ABC):
    @abstractmethod
    def upload(self):
        pass