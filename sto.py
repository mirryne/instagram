import requests
from bs4 import BeautifulSoup

데이터 = requests.get('https://finance.naver.com/item/main.naver?code=005930')

print(데이터.content)