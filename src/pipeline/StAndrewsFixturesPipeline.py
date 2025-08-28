import downloader, processor, uploader
from .Pipeline import Pipeline

class StAndrewsFixturesPipeline(Pipeline):
   def __init__(self, source=None, sink=None):
      if source is not None:
        self.downloader = downloader.InMemoryDownloader(source)
      else:
        self.downloader = downloader.SkyTeamFixtureDownloader("birmingham-city")
      self.processor = processor.CompositeProcessor(
          processor.AlterMetaDataProcessor(), 
          processor.RemoveAwayGamesProcessor(),
          #processor.AddStubEventProcessor(),
          processor.AddAlarmsProcessor()
          ) 
      if sink is not None:
        self.uploader = uploader.InMemoryUploader(sink)
      else:
        self.uploader = uploader.CompositeUploader(
          uploader.FileSystemUploader("bcfc-home-games.ics"), 
          uploader.NetlifyUploader("bcfc-home-games.ics"), 
          )
   
   def run(self):
      calendar = self.downloader.download()
      calendar = self.processor.process(calendar)
      self.uploader.upload(calendar)
      