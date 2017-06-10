import re
import subprocess
import locale
import sys
import time
import json
from bs4 import BeautifulSoup

# if unsupported locale setting reported, you can use locale -a to see whether zh_CN or zh_CN.utf-8 should be used
locale.setlocale(locale.LC_TIME, "zh_CN.utf-8")
news_txt = open('news.txt', 'w')
sys.stdout = news_txt

TODAY = time.strftime("%Y年%-b月%-d日星期%a")
TOPK = 10
TEMPLATE = '『中德人工智能协会』- 今天AI了没？🤣 \n' \
           '今天是%s，让我们来扒一扒国内外人工智能届外的那些新闻吧👀\n\n' \
           '%s \n\n' \
           '本文由『中德人工智能协会』自动整理生成🤖。今天AI了没？🤣『中德人工智能协会』旗下的新闻摘要服务。' \
           '关注aichina.de (主页建设中) 成为AI Geek!👽'

def write_google_news():
	
	subprocess.Popen("bash google-news.sh",  shell=True).communicate()
	with open('news.json') as fp:
    		news = json.load(fp)
    		for v in news:
        		v['summary'] = BeautifulSoup(v['summary'], "html.parser").text\
            			.replace('\n','')\
            			.replace('and more »', '')\
            			.replace('大纪元', '')
        		v['summary'] = re.sub(r'all\s\d+\snews articles', '', v['summary'])

	print(TEMPLATE%(TODAY, '\n\n'.join('▶ %s\n%s'%(v['summary'], v['link']) for v in news[:TOPK])))


def write_chinese_subscription():
	subprocess.Popen("bash chinese-subscription.sh", shell=True).communicate()
	with open('chinese-subscription.json') as fp:
    		news = json.load(fp)
    		for v in news:
        		v['content']['summary'] = BeautifulSoup(v['content']['summary'], "html.parser").text\
            			.replace('\n','')\
            			.replace('and more »', '')\
            			.replace('大纪元', '')
        		v['content']['summary'] = re.sub(r'all\s\d+\snews articles', '', v['content']['summary'])

	print(TEMPLATE%(TODAY, '\n\n'.join('▶ 来源：%s\n标题：%s\n内容：%s\n链接：%s'%(v['feed_name'],v['content']['title'], v['content']['summary'][:200]+'...', v['content']['link']) for v in news[:TOPK])))


if __name__=="__main__":

	#write_google_news()
	write_chinese_subscription()
	news_txt.close()
