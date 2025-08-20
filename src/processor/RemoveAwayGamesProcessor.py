from .Processor import *

class RemoveAwayGamesProcessor(Processor):
    
    def updateEvent(self, event):
      event.name = 'BCFC Home Game'
      event.description = "Football game at St. Andrew's Stadium today. Expect heavy congestion around Small Heath"
      return event
    
    def removeAwayGames(self, calendar):
        homeGames = {
            self.updateEvent(event) 
            for event in calendar.events 
            if "St. Andrew's Stadium" in event.location
            }
        return homeGames

    def process(self, calendar):
        homeGames = self.removeAwayGames(calendar)
        calendar.events = homeGames
        return calendar
