# Assignmnet Number..: 6b
# Author.............: Bae Juyeon
# File name..........: hw6b.py
# Written Data.......: 2017/07/11
# Program Description: HTML과 웹 크롤링(web crawling)의 기초를 익힌다. 웹 크롤링을 실습해 본다.


# 웹 크롤링을 위한 python 모듈 불러오기
from bs4 import BeautifulSoup  
from urllib.request import urlopen

# url변수에 웹페이지 주소 저장 
url = 'http://simple.wikipedia.org/wiki/List_of_U.S._states' 

# urlopen()함수를 통해 url 열고 web 변수에 저장
web = urlopen(url) 

# BeautifulSoup()함수로 url 파싱, source 변수에 저장
source = BeautifulSoup(web, 'html.parser')

# table 변수에 표 내용 저장
table = source.find(attrs={'class' : 'wikitable'})
# state_name 변수에 내용 저장
state_name = table.find_all('a')

i = 0 # 인덱스 나타내는 임의의 변수 i 형성
for i in range(10): # for문을 활용해 i가 range(10)까지 돌게 함  
	print(state_name[i].get_text()) # i 인덱스 가지는 state_name 값 출력 
	i =+ 1
	


# 조교님 22번 줄에서 table = source.find_all('table', {'class': 'wikitable'}) 이렇게 하면 왜 안돌아가나요???