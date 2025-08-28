from .Uploader import Uploader

class NullUploader(Uploader):
    def upload(self, calendar):
        return calendar