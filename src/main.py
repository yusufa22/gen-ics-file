import downloader
import uploader

class CalendarGenerator:
   def __init__(self, downloader: downloader.Downloader, uploader: uploader.Uploader):
      self.downloader = downloader
      self.uploader = uploader
   
   def generate(self):
      self.downloader.download()
      self.uploader.upload()

if __name__ == "__main__":
    calendarGenerator = CalendarGenerator(downloader.SkySportsDownloader(), uploader.NetlifyUploader())
    calendarGenerator.generate()