# Assignmnet Number..: 3C
# Author.............: Bae Juyeon
# File name..........: hw3C.py
# Written Data.......: 2017/06/30
# Program Description: str 자료형의 변수를 생성하고 슬라이싱합니다. 중첩된 if-else문과 for/while 문을 만듭니다.


#1
telephone = '0312152580' # telephone 변수 생성 
print(telephone) # telephone 변수 출력

#2
area_code = telephone[0:3] # area_code 변수를 생성하고 telephone 변수에서 전화번화의 지역변호 할당 
print(area_code) # area_code 변수 출력 
number = telephone[3:] # number 변수를 생성하고 telephone 변수에서 지역번호를 제외한 번호 할당 
print(number) # number 변수 출력

#3
print(type(area_code)) # area_code 와 number 변수의 자료형 출력
print(type(number)) 

#4
area_code_input = input('What is the area code of your telephone number? : ') # 사용자의 지역번호를 물어보고 그 결과를 area_code_input 변수에 할당

number_input =  input('What is your telephone number, without the area code? : ') # 지역번호를 제외한 사용자의 전화번호를 물어보고 그 결과를 number 변수에 할당

#5
if area_code == area_code_input: # (바깥 if-else문) area_code와 area_code_input 변수 비교. 두 변수가 같은 값을 가지고 있으면 안쪽 if-else문으로 들어갑니다. 
	if number == number_input:  # (내부 if-else문) number와 number_input 변수 비교. 두 변수가 같으면 'your telephone number is verified 출력'. 다르면 'number is incorrect'출력
		print('Your telephone number is verified!!') 
	else :
		print('Number is incorrect')
else: 
	print('Area code is incorrect') #(바깥 if-else문) area_code와 area_code_input 변수 값이 다르면 'Area code is incorrect'를 출력

#6
range(10) # 0부터 9까지 10갸의 각 정수를 10으로 나눈 결과 출력(for문 활용 )
for x in range(10) :
	print(x/10)

#7
y = 0 # 0부터 9까지 10갸의 각 정수를 10으로 나눈 결과 출력 (while문 활용)
while True :
	if y < 10 :
		print(y/10)
		y +=1
	else :
		break



''' # 조교님 질문이 있는데요. 아래처럼 하면 if-else 안 쓰고 while문 종료할 수 있는데 문제에서 if-else문 사용하라고 하신 이유가 뭐예요????
	y = 0
	while y < 10:
		print(y/10)
		y +=1 
'''

