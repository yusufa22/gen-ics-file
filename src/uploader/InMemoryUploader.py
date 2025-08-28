from .Uploader import Uploader

class InMemoryUploader(Uploader):
    
    def __init__(self, sink):
        self.sink = sink

    def upload(self, calendar):
        self.sink.events.update(calendar.events)