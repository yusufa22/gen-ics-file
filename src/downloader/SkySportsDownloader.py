from .Downloader import *
import requests
from ics import Calendar

class SkySportsDownloader(Downloader):
    def __init__(self):
      self.url = "https://www.skysports.com/calendars/football/fixtures/teams/birmingham-city"

    def download(self):
        icsFileContents = requests.get(self.url).text
        calendar = Calendar(icsFileContents)
        return calendar

