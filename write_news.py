import subprocess
import json

subprocess.Popen("bash google-news.sh",  shell=True).communicate()
print('news json is ready!')

with open('news.json') as fp:
    news = json.load(fp)