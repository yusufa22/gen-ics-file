from .Processor import Processor

class CompositeProcessor(Processor):
    def __init__(self, *processors):
        self.processors = processors

    def process(self, data):
        output = data
        for processor in self.processors:
            output = processor.process(output)
        return output