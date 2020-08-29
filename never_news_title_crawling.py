import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

""" import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding = 'utf-8') """

news_list = []
date_list = []

for i in range(27,12,-1):
    print(i)
    base_url = 'https://news.naver.com/main/list.nhn?mode=LS2D&sid2=259&sid1=101&mid=shm&date=202008' # 금융
    #base_url = 'https://news.naver.com/main/list.nhn?mode=LS2D&sid2=258&sid1=101&mid=shm&date=202008' # 증권
    
    date_n =i
    page_n = 1
    date = base_url[-6:] + str(date_n)
    
    for j in range(1,24):

        page = '&page='
        URL = base_url + str(date_n) + page + str(page_n)
        print(URL)
        page_n = page_n + 1

        response = requests.get(URL)
        soup = BeautifulSoup(response.text, 'html.parser')

        news_list_1 = soup.select(
            "#main_content > div.list_body.newsflash_body > ul.type06_headline > li")

        news_list_2 = soup.select(
            "#main_content > div.list_body.newsflash_body > ul.type06 > li")

        
        for news in news_list_1:
            if news.select_one('dl > dt[class=photo]'):
                a_tag = news.select_one('dl > dt:nth-child(2) > a')
                #print(a_tag.text.strip())
                T = a_tag.text.strip()
                date_list.append(date)
                news_list.append(T)

            else:
                a_tag = news.select_one('dl > dt:nth-child(1) > a')
                #print(a_tag.text.strip())
                T = a_tag.text.strip()
                date_list.append(date)
                news_list.append(T)

        for news in news_list_2:
            if news.select_one('dl > dt[class=photo]'):
                a_tag = news.select_one('dl > dt:nth-child(2) > a')
                #print(a_tag.text.strip())
                T = a_tag.text.strip()
                date_list.append(date)
                news_list.append(T)
            else:
                a_tag = news.select_one('dl > dt:nth-child(1) > a')
                #print(a_tag.text.strip())
                T = a_tag.text.strip()
                date_list.append(date)
                news_list.append(T)

#print(date_list)
#print(news_list)

dic_data = {'date': date_list,
'title': news_list}

df = pd.DataFrame(dic_data)
df = df.set_index("date")
df = df.drop_duplicates(['title'])

df.to_csv("test.csv",encoding='utf-8')


