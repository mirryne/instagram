import requests
from bs4 import BeautifulSoup
import time
 
data = requests.get('https://search.naver.com/search.naver?display=15&f=&filetype=0&page=2&query=%EB%A6%AC%EC%A5%AC%EB%9E%80%ED%9E%90%EB%9F%AC&research_url=&sm=tab_pge&start=1&where=web')
 
soup = BeautifulSoup(data.text.replace('\\',''),'html.parser')
 
글리스트 = soup.select('a.link_tit')

파일 = open ('rejuran-naver.txt','w')

print("1페이지" + '\n')
print(파일.write(글리스트[0]['href'] + '\n'))
print(파일.write(글리스트[1]['href'] + '\n'))
print(파일.write(글리스트[2]['href'] + '\n'))
print(파일.write(글리스트[3]['href'] + '\n'))
print(파일.write(글리스트[4]['href'] + '\n'))
print(파일.write(글리스트[6]['href'] + '\n'))
print(파일.write(글리스트[7]['href'] + '\n'))
print(파일.write(글리스트[8]['href'] + '\n'))
print(파일.write(글리스트[9]['href'] + '\n'))
print(파일.write(글리스트[10]['href'] + '\n'))
print(파일.write(글리스트[11]['href'] + '\n'))
print(파일.write(글리스트[12]['href'] + '\n'))
print(파일.write(글리스트[13]['href'] + '\n'))
print(파일.write(글리스트[14]['href'] + '\n'))

파일.close()
 
data = requests.get('https://search.naver.com/search.naver?display=15&f=&filetype=0&page=3&query=%EB%A6%AC%EC%A5%AC%EB%9E%80%ED%9E%90%EB%9F%AC&research_url=&sm=tab_pge&start=16&where=web')
soup = BeautifulSoup(data.text.replace('\\',''),'html.parser')
 
글리스트 = soup.select('a.link_tit')

파일 = open ('rejuran-naver.txt','a')
 
print("2페이지" + '\n')
print(파일.write(글리스트[0]['href'] + '\n'))
print(파일.write(글리스트[1]['href'] + '\n'))
print(파일.write(글리스트[2]['href'] + '\n'))
print(파일.write(글리스트[3]['href'] + '\n'))
print(파일.write(글리스트[4]['href'] + '\n'))
print(파일.write(글리스트[6]['href'] + '\n'))
print(파일.write(글리스트[7]['href'] + '\n'))
print(파일.write(글리스트[8]['href'] + '\n'))
print(파일.write(글리스트[9]['href'] + '\n'))
print(파일.write(글리스트[10]['href'] + '\n'))
print(파일.write(글리스트[11]['href'] + '\n'))
print(파일.write(글리스트[12]['href'] + '\n'))
print(파일.write(글리스트[13]['href'] + '\n'))
print(파일.write(글리스트[14]['href'] + '\n'))

파일.close()
 
time.sleep(2)
data = requests.get('https://search.naver.com/search.naver?display=15&f=&filetype=0&page=4&query=%EB%A6%AC%EC%A5%AC%EB%9E%80%ED%9E%90%EB%9F%AC&research_url=&sm=tab_pge&start=31&where=web')
soup = BeautifulSoup(data.text.replace('\\',''),'html.parser')
 
글리스트 = soup.select('a.link_tit')

파일 = open ('rejuran-naver.txt','a')
 
print("3페이지" + '\n')
print(파일.write(글리스트[0]['href'] + '\n'))
print(파일.write(글리스트[1]['href'] + '\n'))
print(파일.write(글리스트[2]['href'] + '\n'))
print(파일.write(글리스트[3]['href'] + '\n'))
print(파일.write(글리스트[4]['href'] + '\n'))
print(파일.write(글리스트[6]['href'] + '\n'))
print(파일.write(글리스트[7]['href'] + '\n'))
print(파일.write(글리스트[8]['href'] + '\n'))
print(파일.write(글리스트[9]['href'] + '\n'))
print(파일.write(글리스트[10]['href'] + '\n'))
print(파일.write(글리스트[11]['href'] + '\n'))
print(파일.write(글리스트[12]['href'] + '\n'))
print(파일.write(글리스트[13]['href'] + '\n'))
print(파일.write(글리스트[14]['href'] + '\n'))

파일.close()
 
data = requests.get('https://search.naver.com/search.naver?display=15&f=&filetype=0&page=5&query=%EB%A6%AC%EC%A5%AC%EB%9E%80%ED%9E%90%EB%9F%AC&research_url=&sm=tab_pge&start=46&where=web')
soup = BeautifulSoup(data.text.replace('\\',''),'html.parser')
 
글리스트 = soup.select('a.link_tit')

파일 = open ('rejuran-naver.txt','a')
 
print("4페이지" + '\n')
print(파일.write(글리스트[0]['href'] + '\n'))
print(파일.write(글리스트[1]['href'] + '\n'))
print(파일.write(글리스트[2]['href'] + '\n'))
print(파일.write(글리스트[3]['href'] + '\n'))
print(파일.write(글리스트[4]['href'] + '\n'))
print(파일.write(글리스트[6]['href'] + '\n'))
print(파일.write(글리스트[7]['href'] + '\n'))
print(파일.write(글리스트[8]['href'] + '\n'))
print(파일.write(글리스트[9]['href'] + '\n'))
print(파일.write(글리스트[10]['href'] + '\n'))
print(파일.write(글리스트[11]['href'] + '\n'))
print(파일.write(글리스트[12]['href'] + '\n'))
print(파일.write(글리스트[13]['href'] + '\n'))
print(파일.write(글리스트[14]['href'] + '\n'))

파일.close()
 
data = requests.get('https://search.naver.com/search.naver?display=15&f=&filetype=0&page=6&query=%EB%A6%AC%EC%A5%AC%EB%9E%80%ED%9E%90%EB%9F%AC&research_url=&sm=tab_pge&start=61&where=web')
soup = BeautifulSoup(data.text.replace('\\',''),'html.parser')
 
글리스트 = soup.select('a.link_tit')

파일 = open ('rejuran-naver.txt','a')
 
print("5페이지" + '\n')
print(파일.write(글리스트[0]['href'] + '\n'))
print(파일.write(글리스트[1]['href'] + '\n'))
print(파일.write(글리스트[2]['href'] + '\n'))
print(파일.write(글리스트[3]['href'] + '\n'))
print(파일.write(글리스트[4]['href'] + '\n'))
print(파일.write(글리스트[6]['href'] + '\n'))
print(파일.write(글리스트[7]['href'] + '\n'))
print(파일.write(글리스트[8]['href'] + '\n'))
print(파일.write(글리스트[9]['href'] + '\n'))
print(파일.write(글리스트[10]['href'] + '\n'))
print(파일.write(글리스트[11]['href'] + '\n'))
print(파일.write(글리스트[12]['href'] + '\n'))
print(파일.write(글리스트[13]['href'] + '\n'))
print(파일.write(글리스트[14]['href'] + '\n'))

파일.close()

time.sleep(2)
data = requests.get('https://search.naver.com/search.naver?display=15&f=&filetype=0&page=7&query=%EB%A6%AC%EC%A5%AC%EB%9E%80%ED%9E%90%EB%9F%AC&research_url=&sm=tab_pge&start=76&where=web')
soup = BeautifulSoup(data.text.replace('\\',''),'html.parser')
 
글리스트 = soup.select('a.link_tit')

파일 = open ('rejuran-naver.txt','a')
 
print("6페이지" + '\n')
print(파일.write(글리스트[0]['href'] + '\n'))
print(파일.write(글리스트[1]['href'] + '\n'))
print(파일.write(글리스트[2]['href'] + '\n'))
print(파일.write(글리스트[3]['href'] + '\n'))
print(파일.write(글리스트[4]['href'] + '\n'))
print(파일.write(글리스트[6]['href'] + '\n'))
print(파일.write(글리스트[7]['href'] + '\n'))
print(파일.write(글리스트[8]['href'] + '\n'))
print(파일.write(글리스트[9]['href'] + '\n'))
print(파일.write(글리스트[10]['href'] + '\n'))
print(파일.write(글리스트[11]['href'] + '\n'))
print(파일.write(글리스트[12]['href'] + '\n'))
print(파일.write(글리스트[13]['href'] + '\n'))
print(파일.write(글리스트[14]['href'] + '\n'))

파일.close()
 
data = requests.get('https://search.naver.com/search.naver?display=15&f=&filetype=0&page=8&query=%EB%A6%AC%EC%A5%AC%EB%9E%80%ED%9E%90%EB%9F%AC&research_url=&sm=tab_pge&start=91&where=web')
soup = BeautifulSoup(data.text.replace('\\',''),'html.parser')
 
글리스트 = soup.select('a.link_tit')

파일 = open ('rejuran-naver.txt','a')
 
print("7페이지" + '\n')
print(파일.write(글리스트[0]['href'] + '\n'))
print(파일.write(글리스트[1]['href'] + '\n'))
print(파일.write(글리스트[2]['href'] + '\n'))
print(파일.write(글리스트[3]['href'] + '\n'))
print(파일.write(글리스트[4]['href'] + '\n'))
print(파일.write(글리스트[6]['href'] + '\n'))
print(파일.write(글리스트[7]['href'] + '\n'))
print(파일.write(글리스트[8]['href'] + '\n'))
print(파일.write(글리스트[9]['href'] + '\n'))
print(파일.write(글리스트[10]['href'] + '\n'))
print(파일.write(글리스트[11]['href'] + '\n'))
print(파일.write(글리스트[12]['href'] + '\n'))
print(파일.write(글리스트[13]['href'] + '\n'))
print(파일.write(글리스트[14]['href'] + '\n'))

파일.close()
 
data = requests.get('https://search.naver.com/search.naver?display=15&f=&filetype=0&page=9&query=%EB%A6%AC%EC%A5%AC%EB%9E%80%ED%9E%90%EB%9F%AC&research_url=&sm=tab_pge&start=106&where=web')
soup = BeautifulSoup(data.text.replace('\\',''),'html.parser')
 
글리스트 = soup.select('a.link_tit')

파일 = open ('rejuran-naver.txt','a')
 
print("8페이지" + '\n')
print(파일.write(글리스트[0]['href'] + '\n'))
print(파일.write(글리스트[1]['href'] + '\n'))
print(파일.write(글리스트[2]['href'] + '\n'))
print(파일.write(글리스트[3]['href'] + '\n'))
print(파일.write(글리스트[4]['href'] + '\n'))
print(파일.write(글리스트[6]['href'] + '\n'))
print(파일.write(글리스트[7]['href'] + '\n'))
print(파일.write(글리스트[8]['href'] + '\n'))
print(파일.write(글리스트[9]['href'] + '\n'))
print(파일.write(글리스트[10]['href'] + '\n'))
print(파일.write(글리스트[11]['href'] + '\n'))
print(파일.write(글리스트[12]['href'] + '\n'))
print(파일.write(글리스트[13]['href'] + '\n'))
print(파일.write(글리스트[14]['href'] + '\n'))

파일.close()
 
time.sleep(2)
data = requests.get('https://search.naver.com/search.naver?display=15&f=&filetype=0&page=10&query=%EB%A6%AC%EC%A5%AC%EB%9E%80%ED%9E%90%EB%9F%AC&research_url=&sm=tab_pge&start=121&where=web')
soup = BeautifulSoup(data.text.replace('\\',''),'html.parser')
 
글리스트 = soup.select('a.link_tit')

파일 = open ('rejuran-naver.txt','a')
 
print("9페이지" + '\n')
print(파일.write(글리스트[0]['href'] + '\n'))
print(파일.write(글리스트[1]['href'] + '\n'))
print(파일.write(글리스트[2]['href'] + '\n'))
print(파일.write(글리스트[3]['href'] + '\n'))
print(파일.write(글리스트[4]['href'] + '\n'))
print(파일.write(글리스트[6]['href'] + '\n'))
print(파일.write(글리스트[7]['href'] + '\n'))
print(파일.write(글리스트[8]['href'] + '\n'))
print(파일.write(글리스트[9]['href'] + '\n'))
print(파일.write(글리스트[10]['href'] + '\n'))
print(파일.write(글리스트[11]['href'] + '\n'))
print(파일.write(글리스트[12]['href'] + '\n'))
print(파일.write(글리스트[13]['href'] + '\n'))
print(파일.write(글리스트[14]['href'] + '\n'))

파일.close()