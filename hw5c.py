# Assignmnet Number..: 5c
# Author.............: Bae Juyeon
# File name..........: hw5c.py
# Written Data.......: 2017/07/07
# Program Description: 패키지와 모듈을 불러오는 법을 익힙니다. 또한 csv 파일을 불러와 읽는 방법을 익힙니다.


import datetime # datetime 모듈 불러오기
now = datetime.datetime.now() # now 변수에 현재시간 저장(datetime 함수 이용)
now = now.strftime('%Y-%m-%d-%H:%M:%S') #시간표현 형식 정의
print(now) # 결과 출력


for line in open('students.csv'): #open() 함수 이용해 students.csv 파일 읽어옴, for 문을 이용해 각 줄 출력
	print(line) 

import csv # csv 모듈 불러옴
file = open('students.csv') # open() 함수를 이용해 'student.csv' 파일을 읽어오고 file 변수에 저장
file_csv = csv.reader(file) # reader() 함수를 이용해 file의 내용을 읽어오고 file_csv 변수에 저장

for line in file_csv: # 각 줄의 내용을 출력
	print(line)


