from .Processor import Processor
from ics import DisplayAlarm
import datetime

class AddAlarmsProcessor(Processor):

    def addRelativeAlarm(self, event, hoursBefore):
        event.alarms.append(DisplayAlarm(trigger=datetime.timedelta(hours=-hoursBefore), display_text=event.description))

    def addAbsoluteAlarm(self, event, time):
        event.alarms.append(DisplayAlarm(trigger=time, display_text=event.description))

    def process(self, calendar):
        for event in calendar.events:
            eventDate = event.begin.date()
            absoluteAlarmTime = datetime.datetime(eventDate.year, eventDate.month, eventDate.day, 9, 0, 0)
            self.addRelativeAlarm(event, hoursBefore=3)
            self.addAbsoluteAlarm(event, time=absoluteAlarmTime)
        return calendar