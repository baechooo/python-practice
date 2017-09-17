# coding: utf-8
# Assignmnet Number..: 2A
# Author.............: Bae Juyeon
# File name..........: hw2a.py
# Written Data.......: 2017/06/27
# Program Description:
# 1) 리스트, 튜플, 셋 그리고 딕셔너리를 생성하는 방법을 익힙니다.
# 2) 리스트와 튜플을 슬라이싱하는 방법을 익힙니다
# 3) 딕셔너리의 키를 통해 값에 접근하는 방법을 익힙니다 '''


numbers = [10, 15, 24, 17, 18, 29, 33, 35] # number 리스트 생성
print(numbers) # numbers 리스트 출력

print(len(numbers)) # numbers 리스트에 포함된 요소의 개수(length) 출력

for x in numbers :    # if-else 문을 사용해 number 리스트에 포함된 요소 중 홀수만 출력(한 줄에 하나씩)
    if x % 2 == 1 :
        print(x)

animals = ('tiger', 'lion', 'pig', 'dog', 'cat', 'snake', 'cheetah', 'monkey') # animal 튜플 생성
print(animals) # anmals 튜플 출력

animals_sub = animals[0:3] # anumals 튜플의 첫 세 요소만 포함한 animal_sub 튜플 생성
print(animals_sub) # anmals_sub 튜플 출력
animals[:] # animals 튜플 슬라이싱

age = dict({'Kim':25,'Lee':33, 'Park':22, 'Han':19}) # age 딕셔너리 생성

keys = age.keys() # age 딕셔너리의 모든 키를 원소로 가지는 셋 keys 생성
print(keys) #keys 출력

print(age['Kim']) # age 딕셔너리를 통해 Kim과 Han의 나이 출력
print(age['Han'])
