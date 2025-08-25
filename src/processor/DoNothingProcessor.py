from .Processor import Processor

class DoNothingProcessor(Processor):
    def process(self, input):
        return input