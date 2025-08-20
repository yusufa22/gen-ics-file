import downloader, processor, uploader
from dotenv import load_dotenv

class CalendarGenerator:
   def __init__(self, downloader: downloader.Downloader, processor: processor.Processor, uploader: uploader.Uploader):
      self.downloader = downloader
      self.processor = processor
      self.uploader = uploader
   
   def generate(self):
      self.uploader.upload(self.processor.process(self.downloader.download()))

if __name__ == "__main__":
    load_dotenv("./.env")
    calendarGenerator = CalendarGenerator(
       downloader.SkySportsDownloader(), 
       processor.CompositeProcessor(
          processor.AlterMetaDataProcessor(), 
          processor.RemoveHomeProcessor()
          ), 
       uploader.NetlifyUploader()
       )
    calendarGenerator.generate()