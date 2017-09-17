# Assignmnet Number..: 7
# Author.............: 배주연
# File name..........: hw7b.py
# Written Data.......: 2017/07/28
# Program Description: 콤마로 분리된 데이터 셋(.csv)을 불러오고 파싱하는 방법을 익힌다. 데이터 전처리하는 방법을 익힌다. 범주형 데이터를 인코딩한다.

# unicodecsv 모듈을 불러온다
import unicodecsv


with open('wine_quality.csv', mode='rb') as file: # open 함수를 이용해 csv 파일을 연다
    reader = unicodecsv.DictReader(file) # unicodecsv 모듈의 DictReader() 함수를 이용해 데이터를 불러오고 딕셔너리 형태로 변환한다
    file_list = list(reader) # 데이터를 리스트로 변환한다

print(file_list[0]) #리스트에서 첫 요소를 출력한다

for a in file_list[0]: 
	file_list[0][a] = float(file_list[0][a]) # 각 변수를 float 타입으로 바꿔준다 
print(file_list[0]) #리스트에서 첫 요소를 출력한다
