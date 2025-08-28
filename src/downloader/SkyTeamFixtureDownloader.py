from .Downloader import *
import requests
from ics import Calendar

class SkyTeamFixtureDownloader(Downloader):

    def __init__(self, team):
        self.url = f"https://www.skysports.com/calendars/football/fixtures/teams/{team}"

    def download(self):
        icsFileContents = requests.get(self.url).text
        calendar = Calendar(icsFileContents)
        return calendar

