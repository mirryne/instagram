import requests
from bs4 import BeautifulSoup
import time
 

파일 = open ('rejuran-naver.txt','w')

# print(파일.write("1페이지" + '\n'))

k = '리쥬란힐러'
data = requests.get('https://search.naver.com/search.naver?display=15&f=&filetype=0&page=2&query=[k]&research_url=&sm=tab_pge&start=1&where=web')
 
soup = BeautifulSoup(data.text.replace('\\',''),'html.parser')
 
글리스트 = soup.select('a.link_tit')

# 파일 = open ('rejuran-naver.txt','w')

print(파일.write("1페이지" + '\n'))
for i in range(15) :
    print(파일.write(글리스트[i]['href'] + '\n'))

    https://search.naver.com/search.naver?display=15&f=&filetype=0&page=2&query=%EB%A6%AC%EC%A5%AC%EB%9E%80%ED%9E%90%EB%9F%AC&research_url=&sm=tab_pge&start=1&where=web

print()