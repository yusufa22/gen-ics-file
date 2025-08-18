from .Uploader import *

class NetlifyUploader():
    def upload(self, calendar):
      open('./generated.ics', 'w').writelines(calendar.serialize_iter())
      print("SUCCESS: ICS file has been generated in this directory with the filename 'generated.ics'")

#create new netlify site 
#create new netlify deploy 