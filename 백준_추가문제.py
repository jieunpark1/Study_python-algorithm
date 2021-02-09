# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 16:16:08 2021

@author: 박지은
"""
import time
#1. 모음의 개수(10987번)
"""
user = input()
arr = ["a", "e", "i", "o", "u"]
cnt = 0
for i in range(len(user)):
    if user[i] in arr:
        cnt += 1
print(cnt)
"""     

#2. 세로읽기(10798번) 
"""
1. 인덱스가 모자란 곳 -> max length만큼 공백을 추가한다.->이후 공백제거

"""
"""
box = []
leng = []
for _ in range(5): #단어와 단어의 길이(내림차순)를 리스트에 저장한다.
    q = input()
    box.append(q)
    leng.append(len(q))
    leng.sort(reverse=True)

    
#print(box)
#print(leng)

output = ""

for idx in range(leng[0]): #max길이에 맞춰 문자열 인덱스 움직임
    for b in box:
        b += (leng[0]-len(b))*" " #max길이 - 해당 문자열 길이만큼 공백을 추가한다
        output += b[idx] 
        #print(output)
    
print(output.replace(" ", "")) #공백제거
"""

#3. 문자열 폭발(9935번) (스택)

""" replace와 find를 사용하게 되면 글자를 반복하여 탐색하게 됨.
start_time = time.time()
a = input()
b = input()
while a.find(b) != -1:
    a = a.replace(b, "")

if a == "":
    print("FRULA")
else:
    print(a)
end_time = time.time()
print("Time:", end_time - start_time #Time: 20.856285095214844
"""

"""
문제접근 - 스택 (선형 탐색)

1. 입력문자열을 앞에서부터 차례차례 한 글자씩 스택에 push 합니다.

2. 현재 글자가 폭발 문자열의 마지막 글자와 일치하면 스택의 top부터 폭발문자열의 길이까지 확인하여 폭발문자열이 만들어지는지 확인합니다.

3. 폭발문자열이 만들어진다면 만들어지는 폭발문자열을 스택에서 pop합니다.

4. 1~3을 반복합니다.

5. 문자열 순회를 마치고 스택이 비어있으면, FRULA를 출력, 비어있지 않다면 스택 속 문자열을 차례로 출력합니다.
"""
"""
start_time = time.time()
def main():
 
    string = input()    # 전체 문자열
    bomb = input()      # 폭발 문자열
 
    lastChar = bomb[-1] # 폭발 문자열의 마지막 글자
    print(lastChar)
    stack = []
    length = len(bomb)  # 폭발 문자열의 길이
 
    for char in string:
        stack.append(char) #string한 문자열씩 stack에 저장
        print(stack)
        print(''.join(stack[-length:])) #bomb의 length만큼 stack의 뒷 부분을 조사한다.
        if char == lastChar and ''.join(stack[-length:]) == bomb:
            del stack[-length:] #pop
 
    answer = ''.join(stack)
    print(answer)
 
    if answer == '':
        print("FRULA")
    else:
        print(answer)
main()
end_time = time.time()
print("Time:", end_time - start_time) #Time: 6.712092876434326
"""

#4. 잃어버린괄호(1541) (그리디)
#괄호를 쳐서 가장 최소로 나올 수 있는 값을 구하라

"""
1.최솟값 = 가장 작은 값 - 가장 큰 값
2.빼려는 값이 클수록 좋다.
"""
"""
s = input().split("-")

sum = 0
for i in s[0].split("+"):
    sum += int(i)

for i in s[1:]:
    for j in i.split("+"):
        sum -= int(j)
        
print(sum)
"""

#5. 균형잡힌 세상 (스택 - 괄호짝 맞추기)

#6. 시그마 함수(11692번)
#시그마 함수 = 정수n의 약수의 합
# 1~m 중에 시그마(n)이 짝수인 것의 개수를 구해라
# n의 약수를 구해서, 약수의 합을 더하고, m까지 돌린 후 짝수인 것을 구해라

#약수 구현하기
#시간초과
"""
cnt = 0
for n in range(1, int(input())+1):
    
    #i의 약수 구하기
    yak = [] #약수 리스트 초기화
    for j in range(1, n+1):
        if n % j == 0 : #약수: 어떤 수로 나누어 나머지가 0인 수
            yak.append(j) #약수 리스트에 추가
            
    #i의 약수 합(시그마 함수)
    yak_sum = sum(yak)
    
    #i의 약수 합이 짝수인 것 구하기
    if yak_sum % 2 ==0:
        cnt += 1
print(cnt)
"""

#7. 팩토리얼(10872번)
"""
user = int(input())
res = 1
if user == 0:
    print(1)
else:
    for i in range(1, user+1):
        res *= i
    print(res)
"""
"""다른풀이: math모듈의 factorial 함수
import math

n=int(input())
print(math.factorial(n))
"""

#8. 피보나치 수 5(10870번)
"""
0번째 : 0
1번째 : 1
2번째: 바로 앞 두 피보나치 수의 합
"""
"""
def fibonacci(n):
    fibo = [0, 1]
    for i in range(2, n+2):
        fibo_new = fibo[i-1] + fibo[i-2]
        fibo.append(fibo_new)
    return fibo[n]
print(fibonacci(int(input())))
"""

"""다른풀이: 재귀함수 사용
def fibonacci(num):
    if num <= 1:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)

"""

#9. 재귀함수가 뭔가요?
"""
어느 한 ~
재귀함수가 뭔가요?
잘 들어보게.~~~물었어.
 ----재귀함수가 뭔가요?
 ----잘 들어보게.~~물었어.
 (8칸)
 
 http://pythontutor.com/visualize.html#mode=display
 d = [0] * 6	
 def fibo(x):
    if x ==1 or x==2:
	        return 1
	    if d[x] != 0:
	        return d[x]
	    d[x] = fibo(x-1) + fibo(x-2)
	    return d[x]
	print(fibo(5))
 
"""
print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
def ask(n):
    if n:
        print((n*4)*4)*"_"+"재귀함수가 뭔가요?")
        print((n*4)*4)*"_"+"재귀함수는 자기 자신을 호출하는 함수라네")
        print((n*4)*4)*"_"+"라고 답변하였지")
    else:
        ask(n-1)
        print((n*4)*"_"+"재귀함수가 뭔가요?")
        print((n*4)*4)*"_"+"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.")
        print((n*4)*4)*"_"+"마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.")
        print((n*4)*4)*"_"+"그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.")
ask(2)
    

