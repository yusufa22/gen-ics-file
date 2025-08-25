from .Processor import Processor
from ics import Event
import datetime

class AddStubEventProcessor(Processor):

    def createEvent(self, name, time):
        event = Event()
        event.name = name
        event.begin = time
        return event

    def process(self, calendar):
        currentDateTime = datetime.datetime.now()
        eventsToAdd = 1440
        eventNumber = 1
        for event in range(eventsToAdd):
            eventTime = currentDateTime + datetime.timedelta(minutes=eventNumber)
            event = self.createEvent(name=f"Test Event {eventNumber}", time=eventTime)
            calendar.events.add(event)
            eventNumber = eventNumber + 1
        return calendar