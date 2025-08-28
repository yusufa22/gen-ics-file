from .Uploader import *

class FileSystemUploader():
    def __init__(self, fileName):
        self.fileName = fileName

    def upload(self, calendar):
        open(self.fileName, 'w').writelines(calendar.serialize_iter())
        print(f"SUCCESS: ICS file has been generated in this directory with the filename {self.fileName}")
