# Assignmnet Number..: 4c
# Author.............: Bae Juyeon
# File name..........: hw4c.py
# Written Data.......: 2017/07/04
# Program Description: 새로운 함수를 정의하는 방법과 람다함수를 익힙니다.


def area_triangle(h, w): # 삼각형의 면적을 구하는 area_triangle()함수를 정의. 두 개의 인수 h와 w로 삼각형의 높이와 밑변의 길이를 받습니다.
	result = 0.5 * h * w   # 결과값으로 삼각형의 면적을 돌려주는 코드입니다.	
	return result

print(area_triangle(10, 15)) # 함수를 불러와 인수값으로 h = 10, w = 15를 입력하고 그 결과를 출력하는 코드입니다.


def distance(a , b): # 2차원 공간 상에서 두 점 사이의 거리를 계산하는 distance() 함수를 정의 

	return ((a[0]-b[0])**2 + (a[1]-b[1])**2) ** 0.5 # 두 점 사이의 거리를 계산하는 연산

a = (1, 2)
b = (5, 7)

print(distance(a, b)) # 함수를 불러와 a, b 사이의 거리를 출력

def count(n):   # 하나의 인수 n을 갖는 count() 함수를 정의   
	if n > 0 :   # 만약 n이 0보다 크면 n을 출력하고 count(n-1) 호출 
		print(n)
		return count(n-1)

	elif n == 0: # 만약 n이 0과 같아지면 'zero!!'를 출력
		print('Zero!!')

count(5) # count 함수를 불러와 인수 값으로 n = 5를 입력하고 그 결과 출력


area_triangle_ld = (lambda h, w : 0.5 * h * w) # 삼각형의 넓이를 계산하는 람다함수 생성

print(area_triangle_ld(10, 15)) # h = 10, w = 15의 인자값을 전달해 그 결과를 출력

