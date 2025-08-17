from .Processor import *

class RemoveHomeProcessor(Processor):
    def modify_event(self, event):
      event.name = 'BCFC Home Game'
      event.description = "Football game at St. Andrew's Stadium today. Expect heavy congestion around Small Heath"
      return event

    def process(self, calendar):
        calendar.events = {self.modify_event(event) for event in calendar.events if "St. Andrew's Stadium" in event.location}
        return calendar
