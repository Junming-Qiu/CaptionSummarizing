from get_caption import YTCaptioner, DocParser
from summarize import GPTSummarizer
import time

cc = YTCaptioner.get_transcript("Uc6lM1Aig9c")
#cc = DocParser.get_transcript("./testing/Meeting2.txt")
store = []

print("Segments:", len(cc))
for i, segment in enumerate(cc):
    s = GPTSummarizer.get_completion(segment, "summary")[0]
    print(f"Segment {i+1} Done!")
    time.sleep(0.2)
    store.append(s)

print(store)




