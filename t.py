import requests
from bs4 import BeautifulSoup
import urllib
import pyautogui
import time
 


btn_3 = pyautogui.prompt(title='네이버키워드랭킹확인기',default='원하는 키워드를 입력하세요',text='리쥬란힐러, 리쥬란, 눈밑지방재배치, 눈밑지방제거')
if btn_3 == '리쥬란힐러' :

        파일 = open ('rejuran-n.txt','w')

        # print(파일.write("1페이지" + '\n'))

        k = '리쥬란힐러'
        encoded_keyword = urllib.parse.quote(k)
        data = requests.get('https://search.naver.com/search.naver?display=15&f=&filetype=0&page=2&query=[k]&research_url=&sm=tab_pge&start=1&where=web')
        
        soup = BeautifulSoup(data.text.replace('\\',''),'html.parser')
        
        글리스트 = soup.select('a.link_tit')

        # 파일 = open ('rejuran-naver.txt','w')

        print(파일.write("1페이지" + '\n'))

        for i in range(15) :
           print(파일.write(글리스트[i]['href'] + '\n'))
        파일.close()

elif btn_3 == '눈밑지방재배치' :
        파일 = open ('noon.txt','w')

        # print(파일.write("1페이지" + '\n'))

        k = '리쥬란힐러'
        encoded_keyword = urllib.parse.quote(k)
        data = requests.get('https://search.naver.com/search.naver?display=15&f=&filetype=0&page=2&query=[k]&research_url=&sm=tab_pge&start=1&where=web')
        
        soup = BeautifulSoup(data.text.replace('\\',''),'html.parser')
        
        글리스트 = soup.select('a.link_tit')

        # 파일 = open ('rejuran-naver.txt','w')

        print(파일.write("1페이지" + '\n'))

        for i in range(15) :
           print(파일.write(글리스트[i]['href'] + '\n'))
        파일.close()     




# btn_1 = pyautogui.alert(text='경고',title='네이버키워드랭킹확인기',button='확인')
# print(btn_1)
# print(type(btn_1))

# btn_2 = pyautogui.confirm(text='테스트',title='네이버키워드랭킹확인기',buttons=['확인','취소'])
# if btn_2 == '확인' :
#     print('okdlqslek.')



btn_3 = pyautogui.prompt(title='네이버키워드랭킹확인기',default='원하는 키워드를 입력하세요',text='키워드 분석기')
print(btn_3)

# k = '리쥬란힐러'
# encoded_keyword = urllib.parse.quote(k)
# print(k)