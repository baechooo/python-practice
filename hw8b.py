# Assignmnet Number..: 8
# Author.............: 배주연
# File name..........: hw8b.py
# Written Data.......: 2017/07/30
# Program Description: 넘파이 모듈을 불러오고 어레이를 생성하는 방법을 배운다.


#넘파이 모듈 불러오기
import numpy as np

#genfreomtxt로 'wine_quality.csv' 불러오기

data = np.genfromtxt('wine_quality.csv', dtype=float, delimiter = ',') # 값들을 실수형태로 불러옴


# fixed_acidity와 volatile acidity 변수의 값으로 이루어진 리스트 생성하기 
fixed_acidity = data[1: , 0] # 1행은 변수 이름들이라 스킵. 1열을 fixed_acidity로 저장 
volatile_acidity = data[1: , 1] # 2열을 volatile_acidity로 저장

print(fixed_acidity[0:5]) # fixed_acidity 리스트의 처음 5개 값을 출력. 
print(type(fixed_acidity))

# 넘파이 모듈을 활용해 fixed_acidity 변수의 통계량 계산하기
print(np.mean(fixed_acidity)) # fixed_acidity의 평균 출력 
print(np.std(fixed_acidity)) # fixed_acidity의 표준편차 출력

# 넘파이 모듈을 활용해 fixed_acidity와 volatile_acidity 변수간의 표본 상관계수를 계산하고 출력
print(np.corrcoef(fixed_acidity, volatile_acidity))
