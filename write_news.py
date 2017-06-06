import re
import subprocess
import locale
import sys
import time
import json
from bs4 import BeautifulSoup

locale.setlocale(locale.LC_TIME, "zh_cn")
news_txt = open('news.txt', 'w')
sys.stdout = news_txt

TODAY = time.strftime("%Y年%-b月%-d日星期%a")
TOPK = 5
TEMPLATE = '『中德人工智能协会』- 今天AI了没？🤣 \n' \
           '今天是%s，让我们来扒一扒国内外人工智能届外的那些新闻吧👀\n\n' \
           '%s \n\n' \
           '本文由『中德人工智能协会』自动整理生成🤖。今天AI了没？🤣『中德人工智能协会』旗下的新闻摘要服务。' \
           '关注aichina.de (主页建设中) 成为AI Geek!👽'

subprocess.Popen("bash google-news.sh",  shell=True).communicate()
#print('news json is ready!')

with open('news.json') as fp:
    news = json.load(fp)
    for v in news:
        v['summary'] = BeautifulSoup(v['summary'], "html.parser").text\
            .replace('\n','')\
            .replace('and more »', '')\
            .replace('大纪元', '')
        v['summary'] = re.sub(r'all\s\d+\snews articles', '', v['summary'])

print(TEMPLATE%(TODAY, '\n\n'.join('▶ %s\n%s'%(v['summary'], v['link']) for v in news[:TOPK])))
news_txt.close()
