from .Downloader import *

class InMemoryDownloader(Downloader):

    def __init__(self, inMemoryLocation):
        self.calendar = inMemoryLocation

    def download(self):
        return self.calendar