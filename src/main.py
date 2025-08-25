import downloader, processor, uploader
from dotenv import load_dotenv
import sys

class CalendarGenerator:
   def __init__(self, downloader: downloader.Downloader, processor: processor.Processor, uploader: uploader.Uploader):
      self.downloader = downloader
      self.processor = processor
      self.uploader = uploader
   
   def generate(self):
      self.uploader.upload(self.processor.process(self.downloader.download()))

if __name__ == "__main__":
    load_dotenv("./.env")
    isTestRun = True if sys.argv[1] == "test" else False
    calendarGenerator = CalendarGenerator(
       downloader.SkySportsDownloader(), 
       processor.CompositeProcessor(
          processor.AlterMetaDataProcessor(), 
          processor.RemoveAwayGamesProcessor(),
          processor.AddStubEventProcessor(),
          processor.AddAlarmsProcessor()
          ), 
       uploader.FileSystemUploader() if isTestRun else uploader.CompositeUploader(uploader.FileSystemUploader(),uploader.NetlifyUploader()) 
       )
    calendarGenerator.generate()