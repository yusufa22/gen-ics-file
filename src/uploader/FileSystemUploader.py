from .Uploader import *

class FileSystemUploader():
    def upload(self, calendar):
        open('./generated.ics', 'w').writelines(calendar.serialize_iter())
        print("SUCCESS: ICS file has been generated in this directory with the filename 'generated.ics'")
