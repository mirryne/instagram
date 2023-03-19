from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
import time


# 원래 url을 분석한다.
# https://search.naver.com/search.naver?nso=&page=2&qdt=-1&query=%EB%A6%AC%EC%A5%AC%EB%9E%80%ED%9E%90%EB%9F%AC&qvt=-1&sm=tab_pag&start=1&where=web

baseUrl = 'https://search.naver.com/search.naver?nso=&page=2&qdt=-1'
queryUrl = '&query='  
keywordUrl = input('검색어를 넣어주세요 : ')
lastUrl = "&qvt=-1&sm=tab_pag&start=1&where=web"

# 모든 조건을 합치고, 한글을 인코딩해 준다. 이때 quote_plus를 사용한다.
url = baseUrl + queryUrl + quote_plus(keywordUrl) + lastUrl

# print(url)
driver = webdriver.Chrome()
driver.get(url)
time.sleep(10)