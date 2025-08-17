from abc import ABC, abstractmethod
import requests
from ics import Calendar


class Downloader(ABC):

    def download(self):
        icsFile = requests.get(self.url).text
        calendar = Calendar(icsFile)
        return calendar