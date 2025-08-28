from .Processor import Processor

class NullProcessor(Processor):
    def process(self, calendar):
        return calendar