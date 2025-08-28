import pipeline, uploader
from dotenv import load_dotenv
from ics import Calendar
import sys

def main():
    load_dotenv("./.env")
    isTestRun = True if sys.argv[1] == "test" else False
    combinedCalendar = Calendar()
    mufcFixturesPipeline = pipeline.MufcFixturesPipeline(sink=combinedCalendar)
    stAndrewsFixturesPipeline = pipeline.StAndrewsFixturesPipeline(sink=combinedCalendar)
    mufcFixturesPipeline.run()
    stAndrewsFixturesPipeline.run()
    fileSystemUploader = uploader.FileSystemUploader("generated.ics")
    fileSystemUploader.upload(combinedCalendar)

if __name__ == "__main__":
    main()