from ics import Calendar
import requests
import validators
import boto3

def get_url():
  default_url = "https://www.skysports.com/calendars/football/fixtures/teams/birmingham-city"
  input_url = input('ATTENTION: Enter ICS file URL or press enter to use the default URL https://www.skysports.com/calendars/football/fixtures/teams/birmingham-city: ')
  while input_url != '' and validators.url(input_url) is not True:
    input_url = input('ERROR: You have not given a valid URL. Please try again or press enter to use the default URL https://www.skysports.com/calendars/football/fixtures/teams/birmingham-city: ') 
  return input_url if input_url != '' else default_url


url = get_url()
ics_file = requests.get(url).text
c = Calendar(ics_file)
s3 = boto3.client('s3')

def modify_event(event):
  event.name = 'BCFC Home Game'
  event.description = "Football game at St. Andrew's Stadium today. Expect heavy congestion around Small Heath"
  return event

c.events = {modify_event(event) for event in c.events if "St. Andrew's Stadium" in event.location}

bucket='gen-ics-file-bucket'
fileName= 'generated.ics'
uploadByteStream = bytes(c.serialize_iter())
s3.put_object(Bucket=bucket, Key=fileName, Body=uploadByteStream)


print("SUCCESS: ICS file has been generated in this directory with the filename 'generated.ics'")

