from abc import ABC, abstractmethod
import requests
from ics import Calendar


class Downloader(ABC):
    
    def download(self):
        icsFile = requests.get(self.url).text
        cal = Calendar(icsFile)
        return cal