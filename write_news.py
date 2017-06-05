import re
import subprocess
import locale
import time
import json
from bs4 import BeautifulSoup

locale.setlocale(locale.LC_TIME, "zh_cn")

TODAY = time.strftime("%Y年%-b月%-d日星期%a")
TOPK = 7
TEMPLATE = '『中德人工智能协会』- 今天AI了没？\n' \
           '今天是%s，让我们来看看今天国内人工智能届外发生了哪些新闻。 \n\n' \
           '%s \n\n' \
           '本文由『中德人工智能协会』自动整理。关注aichina.de 成为AI Geek!'

#subprocess.Popen("bash google-news.sh",  shell=True).communicate()
print('news json is ready!')

with open('news.json') as fp:
    news = json.load(fp)
    for v in news:
        v['summary'] = BeautifulSoup(v['summary'], "html.parser").text\
            .replace('\n','')\
            .replace('and more »', '')
        v['summary'] = re.sub(r'all\s\d+\snews articles', '', v['summary'])

print(TEMPLATE%(TODAY, '\n\n'.join('%s\n%s'%(v['summary'], v['link']) for v in news[:TOPK])))