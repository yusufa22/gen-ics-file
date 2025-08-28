import downloader, processor, uploader
from .Pipeline import Pipeline

class MufcFixturesPipeline(Pipeline):
   def __init__(self, source=None, sink=None):
      if source is not None:
         self.downloader = downloader.InMemoryDownloader(source)
      else:
        self.downloader = downloader.SkyTeamFixtureDownloader("manchester-united")
      self.processor = processor.CompositeProcessor(
          processor.AlterMetaDataProcessor(), 
          #processor.RemoveAwayGamesProcessor(),
          #processor.AddStubEventProcessor(),
          processor.AddAlarmsProcessor()
          ) 
      if sink is not None:
         self.uploader = uploader.InMemoryUploader(sink)
      else:
        self.uploader = uploader.CompositeUploader(
          uploader.FileSystemUploader("mufc-games.ics"), 
          uploader.NetlifyUploader("mufc-games.ics"), 
          )
   
   def run(self):
      calendar = self.downloader.download()
      calendar = self.processor.process(calendar)
      self.uploader.upload(calendar)
      