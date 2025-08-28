from .Downloader import Downloader
from ics import Calendar

class CompositeDownloader(Downloader):
    def __init__(self, *downloaders):
        self.downloaders = downloaders

    def download(self):
        CompositeCalendar = Calendar()
        for downloader in self.downloaders:
            downloadedCalendar = downloader.download()
            CompositeCalendar.events.update(downloadedCalendar.events)
        return CompositeCalendar