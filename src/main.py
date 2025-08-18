import downloader, processor, uploader

class CalendarGenerator:
   def __init__(self, downloader: downloader.Downloader, processor: processor.Processor, uploader: uploader.Uploader):
      self.downloader = downloader
      self.processor = processor
      self.uploader = uploader
   
   def generate(self):
      self.uploader.upload(self.processor.process(self.downloader.download()))

if __name__ == "__main__":
    calendarGenerator = CalendarGenerator(downloader.SkySportsDownloader(), processor.RemoveHomeProcessor(), uploader.FileSystemUploader())
    calendarGenerator.generate()