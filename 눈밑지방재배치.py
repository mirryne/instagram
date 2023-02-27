import requests
from bs4 import BeautifulSoup
import time
 

파일 = open ('눈밑지방재배치(naver).txt','w')

data = requests.get('https://search.naver.com/search.naver?display=15&f=&filetype=0&page=2&query=%EB%88%88%EB%B0%91%EC%A7%80%EB%B0%A9%EC%9E%AC%EB%B0%B0%EC%B9%98&research_url=&sm=tab_pge&start=1&where=web')
 
soup = BeautifulSoup(data.text.replace('\\',''),'html.parser')
 
글리스트 = soup.select('a.link_tit')

# 파일 = open ('눈밑지방재배치(naver).txt','w')

print(파일.write("2page" + '\n'))
for i in range(15) :
    print(파일.write(글리스트[i]['href'] + '\n'))

# 파일.close()
 
data = requests.get('https://search.naver.com/search.naver?display=15&f=&filetype=0&page=3&query=%EB%88%88%EB%B0%91%EC%A7%80%EB%B0%A9%EC%9E%AC%EB%B0%B0%EC%B9%98&research_url=&sm=tab_pge&start=16&where=web')
soup = BeautifulSoup(data.text.replace('\\',''),'html.parser')
 
글리스트 = soup.select('a.link_tit')

# 파일 = open ('눈밑지방재배치(naver).txt','a')

print(파일.write("3page" + '\n'))
for i in range(15) :
    #    # print(글리스트[i]['href'] + '\n') 
    print(파일.write(글리스트[i]['href'] + '\n')) 
    print(파일.write(글리스트[i]['href'] + '\n'))
 
# print("2page" + '\n')
# print(글리스트[0]['href'] + '\n')
# print(글리스트[1]['href'] + '\n')
# print(글리스트[2]['href'] + '\n')
# print(글리스트[3]['href'] + '\n')
# print(글리스트[4]['href'] + '\n')
# print(글리스트[6]['href'] + '\n')
# print(글리스트[7]['href'] + '\n')
# print(글리스트[8]['href'] + '\n')
# print(글리스트[9]['href'] + '\n')
# print(글리스트[10]['href'] + '\n')
# print(글리스트[11]['href'] + '\n')
# print(글리스트[12]['href'] + '\n')
# print(글리스트[13]['href'] + '\n')
# print(글리스트[14]['href'] + '\n')

# 파일.close()
 
time.sleep(2)
data = requests.get('https://search.naver.com/search.naver?display=15&f=&filetype=0&page=4&query=%EB%88%88%EB%B0%91%EC%A7%80%EB%B0%A9%EC%9E%AC%EB%B0%B0%EC%B9%98&research_url=&sm=tab_pge&start=31&where=web')
soup = BeautifulSoup(data.text.replace('\\',''),'html.parser')
 
글리스트 = soup.select('a.link_tit')

# # 파일 = open ('눈밑지방재배치(naver).txt','a')

print(파일.write("4page" + '\n')) 
for i in range(15) :
       # print(글리스트[i]['href'] + '\n') 
    print(파일.write(글리스트[i]['href'] + '\n'))
# # print("3page" + '\n')
# # print(글리스트[0]['href'] + '\n')
# # print(글리스트[1]['href'] + '\n')
# # print(글리스트[2]['href'] + '\n')
# # print(글리스트[3]['href'] + '\n')
# # print(글리스트[4]['href'] + '\n')
# # print(글리스트[6]['href'] + '\n')
# # print(글리스트[7]['href'] + '\n')
# # print(글리스트[8]['href'] + '\n')
# # print(글리스트[9]['href'] + '\n')
# # print(글리스트[10]['href'] + '\n')
# # print(글리스트[11]['href'] + '\n')
# # print(글리스트[12]['href'] + '\n')
# # print(글리스트[13]['href'] + '\n')
# # print(글리스트[14]['href'] + '\n')

# # 파일.close()
 
data = requests.get('https://search.naver.com/search.naver?display=15&f=&filetype=0&page=5&query=%EB%88%88%EB%B0%91%EC%A7%80%EB%B0%A9%EC%9E%AC%EB%B0%B0%EC%B9%98&research_url=&sm=tab_pge&start=46&where=web')
soup = BeautifulSoup(data.text.replace('\\',''),'html.parser')
 
글리스트 = soup.select('a.link_tit')

# # 파일 = open ('눈밑지방재배치(naver).txt','a')

print(파일.write("5page" + '\n'))
for i in range(15) :
       # print(글리스트[i]['href'] + '\n') 
    print(파일.write(글리스트[i]['href'] + '\n'))

# # print("4page" + '\n')
# # print(글리스트[0]['href'] + '\n')
# # print(글리스트[1]['href'] + '\n')
# # print(글리스트[2]['href'] + '\n')
# # print(글리스트[3]['href'] + '\n')
# # print(글리스트[4]['href'] + '\n')
# # print(글리스트[6]['href'] + '\n')
# # print(글리스트[7]['href'] + '\n')
# # print(글리스트[8]['href'] + '\n')
# # print(글리스트[9]['href'] + '\n')
# # print(글리스트[10]['href'] + '\n')
# # print(글리스트[11]['href'] + '\n')
# # print(글리스트[12]['href'] + '\n')
# # print(글리스트[13]['href'] + '\n')
# # print(글리스트[14]['href'] + '\n')

# # 파일.close()
 
data = requests.get('https://search.naver.com/search.naver?display=15&f=&filetype=0&page=6&query=%EB%88%88%EB%B0%91%EC%A7%80%EB%B0%A9%EC%9E%AC%EB%B0%B0%EC%B9%98&research_url=&sm=tab_pge&start=61&where=web')
soup = BeautifulSoup(data.text.replace('\\',''),'html.parser')
 
글리스트 = soup.select('a.link_tit')

# # 파일 = open ('눈밑지방재배치(naver).txt','a')

print(파일.write("6page" + '\n'))
for i in range(15) :
       # print(글리스트[i]['href'] + '\n') 
    print(파일.write(글리스트[i]['href'] + '\n'))
 
# # print("5page" + '\n')
# # print(글리스트[0]['href'] + '\n')
# # print(글리스트[1]['href'] + '\n')
# # print(글리스트[2]['href'] + '\n')
# # print(글리스트[3]['href'] + '\n')
# # print(글리스트[4]['href'] + '\n')
# # print(글리스트[6]['href'] + '\n')
# # print(글리스트[7]['href'] + '\n')
# # print(글리스트[8]['href'] + '\n')
# # print(글리스트[9]['href'] + '\n')
# # print(글리스트[10]['href'] + '\n')
# # print(글리스트[11]['href'] + '\n')
# # print(글리스트[12]['href'] + '\n')
# # print(글리스트[13]['href'] + '\n')
# # print(글리스트[14]['href'] + '\n')

# # 파일.close()

time.sleep(2)
data = requests.get('https://search.naver.com/search.naver?display=15&f=&filetype=0&page=7&query=%EB%88%88%EB%B0%91%EC%A7%80%EB%B0%A9%EC%9E%AC%EB%B0%B0%EC%B9%98&research_url=&sm=tab_pge&start=76&where=web')
soup = BeautifulSoup(data.text.replace('\\',''),'html.parser')
 
글리스트 = soup.select('a.link_tit')

# # 파일 = open ('눈밑지방재배치(naver).txt','a')

print(파일.write("7page" + '\n'))
for i in range(15) :
       # print(글리스트[i]['href'] + '\n') 
    print(파일.write(글리스트[i]['href'] + '\n'))
 
# # print("6page" + '\n')
# # print(글리스트[0]['href'] + '\n')
# # print(글리스트[1]['href'] + '\n')
# # print(글리스트[2]['href'] + '\n')
# # print(글리스트[3]['href'] + '\n')
# # print(글리스트[4]['href'] + '\n')
# # print(글리스트[6]['href'] + '\n')
# # print(글리스트[7]['href'] + '\n')
# # print(글리스트[8]['href'] + '\n')
# # print(글리스트[9]['href'] + '\n')
# # print(글리스트[10]['href'] + '\n')
# # print(글리스트[11]['href'] + '\n')
# # print(글리스트[12]['href'] + '\n')
# # print(글리스트[13]['href'] + '\n')
# # print(글리스트[14]['href'] + '\n')

# # 파일.close()
 
data = requests.get('https://search.naver.com/search.naver?display=15&f=&filetype=0&page=8&query=%EB%88%88%EB%B0%91%EC%A7%80%EB%B0%A9%EC%9E%AC%EB%B0%B0%EC%B9%98&research_url=&sm=tab_pge&start=91&where=web')
soup = BeautifulSoup(data.text.replace('\\',''),'html.parser')
 
글리스트 = soup.select('a.link_tit')

# # 파일 = open ('눈밑지방재배치(naver).txt','a')

print(파일.write("8page" + '\n'))
for i in range(15) :
       # print(글리스트[i]['href'] + '\n') 
    print(파일.write(글리스트[i]['href'] + '\n'))
 
# # print("7page" + '\n')
# # print(글리스트[0]['href'] + '\n')
# # print(글리스트[1]['href'] + '\n')
# # print(글리스트[2]['href'] + '\n')
# # print(글리스트[3]['href'] + '\n')
# # print(글리스트[4]['href'] + '\n')
# # print(글리스트[6]['href'] + '\n')
# # print(글리스트[7]['href'] + '\n')
# # print(글리스트[8]['href'] + '\n')
# # print(글리스트[9]['href'] + '\n')
# # print(글리스트[10]['href'] + '\n')
# # print(글리스트[11]['href'] + '\n')
# # print(글리스트[12]['href'] + '\n')
# # print(글리스트[13]['href'] + '\n')
# # print(글리스트[14]['href'] + '\n')

# # 파일.close()
 
data = requests.get('https://search.naver.com/search.naver?display=15&f=&filetype=0&page=9&query=%EB%88%88%EB%B0%91%EC%A7%80%EB%B0%A9%EC%9E%AC%EB%B0%B0%EC%B9%98&research_url=&sm=tab_pge&start=106&where=web')
soup = BeautifulSoup(data.text.replace('\\',''),'html.parser')
 
글리스트 = soup.select('a.link_tit')

# # 파일 = open ('눈밑지방재배치(naver).txt','a')

print(파일.write("9page" + '\n'))
for i in range(15) :
       # print(글리스트[i]['href'] + '\n') 
    print(파일.write(글리스트[i]['href'] + '\n'))
 
# # print("8page" + '\n')
# # print(글리스트[0]['href'] + '\n')
# # print(글리스트[1]['href'] + '\n')
# # print(글리스트[2]['href'] + '\n')
# # print(글리스트[3]['href'] + '\n')
# # print(글리스트[4]['href'] + '\n')
# # print(글리스트[6]['href'] + '\n')
# # print(글리스트[7]['href'] + '\n')
# # print(글리스트[8]['href'] + '\n')
# # print(글리스트[9]['href'] + '\n')
# # print(글리스트[10]['href'] + '\n')
# # print(글리스트[11]['href'] + '\n')
# # print(글리스트[12]['href'] + '\n')
# # print(글리스트[13]['href'] + '\n')
# # print(글리스트[14]['href'] + '\n')

# # 파일.close()
 
time.sleep(2)
data = requests.get('https://search.naver.com/search.naver?display=15&f=&filetype=0&page=10&query=%EB%88%88%EB%B0%91%EC%A7%80%EB%B0%A9%EC%9E%AC%EB%B0%B0%EC%B9%98&research_url=&sm=tab_pge&start=121&where=web')
soup = BeautifulSoup(data.text.replace('\\',''),'html.parser')
 
글리스트 = soup.select('a.link_tit')

# # 파일 = open ('눈밑지방재배치(naver).txt','a')

print(파일.write("10page" + '\n'))
for i in range(15) :
       # print(글리스트[i]['href'] + '\n') 
    print(파일.write(글리스트[i]['href'] + '\n'))
 
# # print("9page" + '\n')
# # print(글리스트[0]['href'] + '\n')
# # print(글리스트[1]['href'] + '\n')
# # print(글리스트[2]['href'] + '\n')
# # print(글리스트[3]['href'] + '\n')
# # print(글리스트[4]['href'] + '\n')
# # print(글리스트[6]['href'] + '\n')
# # print(글리스트[7]['href'] + '\n')
# # print(글리스트[8]['href'] + '\n')
# # print(글리스트[9]['href'] + '\n')
# # print(글리스트[10]['href'] + '\n')
# # print(글리스트[11]['href'] + '\n')
# # print(글리스트[12]['href'] + '\n')
# # print(글리스트[13]['href'] + '\n')
# # print(글리스트[14]['href'] + '\n')

파일.close()
