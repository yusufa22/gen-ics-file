from .Uploader import *
import requests, hashlib, os

class NetlifyUploader():

    def __init__(self, fileName):
      self.requestsHeader = {
        "Authorization": f"Bearer {os.environ.get('NETLIFY_TOKEN')}",
        "Content-Type": "application/json"
        }
      self.fileName = fileName
    
    @staticmethod
    def RequestIsSuccessful(response):
      try:
       response.raise_for_status()
       return True
      except requests.exceptions.HTTPError as e:
       print("Error:", e)
       return False
    
    def NetlifySiteExists(self, siteDomain):
      url = f"https://api.netlify.com/api/v1/sites/{siteDomain}"
      response = requests.get(url=url, headers=self.requestsHeader)
      return self.RequestIsSuccessful(response)

    def createNetlifySite(self, siteName):
      url = "https://api.netlify.com/api/v1/sites"
      body = {
        "name": siteName
      }
      response = requests.post(url=url, headers=self.requestsHeader, json=body)
      return self.RequestIsSuccessful(response)
    
    
    def createNetlifyDeployment(self, siteDomain, fileName, fileContents):
        url = f"https://api.netlify.com/api/v1/sites/{siteDomain}/deploys"
        fileContentsHash = hashlib.sha1(fileContents.encode("utf-8")).hexdigest()
        body = {"files": {fileName: fileContentsHash}}
        response = requests.post(url, headers=self.requestsHeader, json=body)
        if not self.RequestIsSuccessful(response):
            return False

        responseData = response.json()
        if fileContentsHash not in responseData.get("required", {}):
          return True
        url = f"https://api.netlify.com/api/v1/deploys/{responseData['id']}/files/{fileName}"
        Header = {
          "Authorization": f"Bearer {os.environ.get('NETLIFY_TOKEN')}",
          "Content-Type": "text/calendar"
        }
        response = requests.put(url, headers=Header, data=fileContents.encode("utf-8"))
        return self.RequestIsSuccessful(response)
        
      
    def upload(self, calendarObject):
      icsFileContents = calendarObject.serialize()
      siteName = "gencal"
      siteDomain = f"{siteName}.netlify.app"
      if self.NetlifySiteExists(siteDomain) == False:
        self.createNetlifySite(siteName)
      self.createNetlifyDeployment(siteDomain, self.fileName, icsFileContents)
      print("SUCCESS: Netlify Upload successful")
      