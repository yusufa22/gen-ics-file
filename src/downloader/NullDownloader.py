from .Downloader import Downloader

class NullDownloader(Downloader):
    def download(self):
        pass