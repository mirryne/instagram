중고차재고 = ['k5','BMW','tico']

if 'k4' in 중고차재고 :
  print('지금주문가능합니다')

else :
   print('지금주문불가라가능합니다')   


파일 = open ('a.txt','w')
파일.write('안녕하세요')
파일.close()

파일 = open ('a.txt','a')
파일.write('\n반가워')
파일.close()


파일 = open('a.txt','r')
print(파일.read())
파일.close()

파일 = open('data.csv','w')
파일.write('김,이,박')
파일.close()
