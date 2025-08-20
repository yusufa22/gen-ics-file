from abc import ABC, abstractmethod
import requests, inspect
from ics import Calendar


class Downloader(ABC):
    
    @abstractmethod
    def download():
        pass