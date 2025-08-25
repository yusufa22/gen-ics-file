from .Uploader import Uploader

class CompositeUploader(Uploader):
    
    def __init__(self, *uploaders):
        self.uploaders = uploaders

    def upload(self, data):
        for uploader in self.uploaders:
            uploader.upload(data)