from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

# API to retrieve YT captions based on video ID
class YTCaptioner():
    def get_transcript(id):
        t = YouTubeTranscriptApi.get_transcript(id)
        formatter = TextFormatter()
        return formatter.format_transcript(t)

# API to retrieve Zoom captions
class ZoomCaptioner():
    def get_transcript(id):
        pass

# Testing
SEGMENT = 4000
class DocParser():
    def get_transcript(filename):
        ret = []
        file = ""
        with open(filename, "r") as f:
            lines = f.readlines()
        
        for line in lines:
            if len(file) > SEGMENT:
                ret.append(file)
                file = ""

            cleaned = line.strip()[line.find(":")+3:]
            file += cleaned
        
        ret.append(file)

        return tuple(ret)

class SummaryParser():
    def get_transcript(prompt):
        ret = []
        
        for i in range(0, len(prompt), SEGMENT):
            if i+SEGMENT < len(prompt):
                ret.append(prompt[i:i+SEGMENT])
            else:
                ret.append(prompt[i:])

        return tuple(ret)