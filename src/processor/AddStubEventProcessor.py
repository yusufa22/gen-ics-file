from .Processor import Processor
from ics import Event
import datetime

class AddStubEventProcessor(Processor):

    def createEvent(self, name, datetime):
        event = Event()
        event.name = name
        event.begin = datetime
        return event

    def process(self, calendar):
        currentDateTime = datetime.datetime.now()
        eventsToAdd = 48 - 1
        eventNumber = 0
        for event in range(eventsToAdd):
            eventTime = currentDateTime + datetime.timedelta(hours=eventNumber)
            event = self.createEvent(name="Test Event", datetime=eventTime)
            calendar.events.add(event)
            eventNumber = eventNumber + 1
        return calendar