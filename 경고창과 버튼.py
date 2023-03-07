import requests
from bs4 import BeautifulSoup
import urllib
import pyautogui
import time


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
