# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 10:29:51 2021

@author: 박지은
"""

#저번시간 구현 남은 문제
#문자열 압축
# 변수: 들어온 문자열 / 단위(하나씩 늘림) / 새로 만들어진 문자열 / 새로 만들어진 문자열의 len 리스트
# 기능: 들어온 문자열을 단위별로 탐색 / 이전과 지금이 같다면 count늘려서 새로운 문자열에 갖다 붙임  or 같지 않다면 그대로 붙임 
#/ 만들어진 문자열의 len을 센다 / 가장 짧은 len의 개수를 반환한다.

#길이만 중요! 숫자는 상관 없음.

s =  "abcabcabc"
#input()

len_news = []
for i in range(1, (len(s)//2)+1): #i = 글자단위 / 글자 단위를 늘리는 for문
    new = ""
    #print(i)
    #문자 단위i별로 문자들을 슬라이싱
    count = 1
    unit = s[0:i]
    for j in range(0, len(s), i):
        #print("단위", s[j:j+i])
        if unit == s[j+i:j+i+i]:
            unit = s[j+i:j+i+i]
            print(unit)
            print("전:", s[j:j+i])
            print("후:", s[j+i:j+i+i])
            if s[j+i:j+i+i] == "":
                print("aa")
                break
            else:
                print("bb")
                count += 1
                new += str(count)
                new += s[j:j+i]
                print(new)

        elif s[j+i:j+i+i] == "":
            print("blank")
            break
        elif s[j:j+i] != s[j+i:j+i+i]: 
            new += s[j:j+i] 
            print("dd")
        count = 1 #초기화
            
    len_news.append(len(new))
    print("new", new)
    
print(len_news)
#return min(len_news)
   



#기출문제10. 자물쇠와 열쇠
        
#기둥과 보 설치


"""

#스택
stack = []

#5push - 2 push - 3push-7push- pop - 1push - 4 push - pop
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop

print(stack) #하단 원소부터 출력
print(stack[::-1]) #상단 원소부터 출력


#큐
from collections import deque
queue = deque()

#5push - 2 push - 3push-7push- pop - 1push - 4 push - pop
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) #먼저 들어온 순서대로
queue.reverse()
print(queue) #나중에 들어온 원소부터 출력

#재귀함수
def recursive_function():
    print("재귀함수를 호출합니다.")
    recursive_function() #자기가 자기를 불러옴
    
recursive_function()


def recursive_function(i):
    if i == 100:
        return
    print(i, "번째 재귀함수에서", i+1, "번째 재귀함수를 호출합니다.")
    recursive_function(i+1) #재귀부분 -> 다시 54line 실행
    print(i, "번째 재귀함수를 종료합니다.")
recursive_function(1)

#팩토리얼
def factorial_recursive(n):
    if n<=1:
        return 1
    print(n)
    return n * factorial_recursive(n-1)
print(factorial_recursive(5))
"""
#유클리드 호제법: A를 B로 나눈 나머지를 R이라고 할 때, A와 B의 최대공약수는 B와 R의 최대공약수와 같다.(A>B)
"""
def GCD(a,b):
    if a%b == 0: #배수 관계이다
        return b #b가 최대 공약수
    else:
        print("b:",b, "나머지", a%b)
        return GCD(b, a%b) #b가 a자리로 오고, b자리에는 나머지가 온다.
print(GCD(192, 162))
"""

#스택문제 
#괄호 https://www.acmicpc.net/problem/9012
#괄호짝이 맞으면 YES, 아니면 NO
"""실패 #())(() --> NO인데 yes라 
def vps(i):
    front = []
    back = []
    for j in range(len(i)):
        if i[j] == "(":
            front.append(i[j])
        elif i[j] == ")":
            back.append(i[j])
    #print(front)
    #print(back)
    if len(front) == len(back):
        return "YES"
    else:
        return "NO"
        
        
    

for _ in range(int(input())):
    i = input()
    print(vps(i))
"""
"""성공!!!
stack = []
res = ""
for _ in range(int(input())):
    i = input()
    for j in range(len(i)):
        if i[j] =="(":
                stack.append(i[j])
        elif i[j] ==")":
            if len(stack) != 0:
                stack.pop()
            else:
                res = "NO"
                break
    if res: 
        print(res)
    elif len(stack) != 0:
        print("NO")
    else:
        print("YES")
    stack = [] 
    res = []
"""           
"""다른사람
from sys import stdin

n = int(input())
for _ in range(n):
    str_ = stdin.readline().strip()
    stack = 0
    for chr_ in str_:
        if chr_ == '(':
            stack += 1
        else:
            stack -= 1
            if stack < 0:
                break
    if stack == 0:
        print('YES')
    else:
        print('NO')
"""

#큐 https://www.acmicpc.net/problem/10845
#선입선출popleft 
"""
from collections import deque
queue = deque()

#5push - 2 push - 3push-7push- pop - 1push - 4 push - pop
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) #먼저 들어온 순서대로
queue.reverse()
print(queue) #나중에 들어온 원소부터 출력

#push -> 0자리에 insert
#pop -> 가장 먼저 들어온 res의 마지막을 pop #-1
#size -> len
#empty -> len = 0
#front -> [-1]인덱스 추출 #-1
#back -> [0] 인덱스 추출. #-1

"""
"""안됨
import sys
res = []
N = int(sys.stdin.readline())

for _ in range(N):
    cmd = sys.stdin.readline()
    if "push" in cmd:
        a = cmd.split()[1]
        res.insert(0, a)
        
    elif cmd == "pop":
        if len(cmd) != 0:
            a = res.pop()
            print(a)
            
        else: print(-1)
            
    elif cmd == "size":
        print(len(res))
    
    elif cmd == "empty":
        if len(cmd) == 0: print(1)
        else: print(0)
        
    elif cmd == "front":
        if len(cmd) == 0: print(-1)
        else: print(res[-1])
    else:
        if len(cmd) == 0: print(-1)
        else: print(res[0])
"""
#요세푸스 순열 0 https://www.acmicpc.net/problem/11866
#한 사람 죽이고 나서 다음 사람 죽일 때는 끝난 자리에서 시작
""""큐"로는 안풀었..
a, b = map(int, input().split())
value = []
res = "<"
for i in range(1, a+1):
    value.append(i)

position = 0
while len(value) != 1:
    position = position + (b-1)
    if len(value) > position:
        res += str(value[position])+", "
        del value[position]

    else:
        position = position % len(value)
        res += str(value[position])+", "
        del value[position]
        
res += str(value[0])+">"
print(res)
"""        

#재귀함수가 뭔가요 https://www.acmicpc.net/problem/17478
"""재귀함수 틀
def 함수이름():
    종료조건 if ~~ return
    반복할 문장
    재귀함수 함수이름(+1 등등)
    모두 반복한 후 나올 문장
"""

        
"""        
rep = int(input())
print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")

def whatRecursive(i, rep):
    if i == rep+1:
        return
    print((rep-(rep-i)) * 4 *"_" + "\"재귀함수가 뭔가요?\"")
    if i == rep:
        print((rep-(rep-i)) * 4 *"_" +"\"재귀함수는 자기 자신을 호출하는 함수라네\"")
    else:
        print((rep-(rep-i)) * 4 *"_" + "\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.")
        print((rep-(rep-i)) * 4 *"_" + "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.")
        print((rep-(rep-i)) * 4 *"_" + "그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"")
    whatRecursive(i+1, rep)
    print((rep-(rep-i)) * 4 * "_" + "라고 답변하였지.")

whatRecursive(0, rep)

#global i 쓰는거 
"""
"""다른사람
n = int(input())
def rec(i):
    global n
    if i < 0:
        return
    print("____"*(n-i) + '"재귀함수가 뭔가요?"')
    if i == 0:
        print("____" * (n - i) + '"재귀함수는 자기 자신을 호출하는 함수라네"')
    else:
        print("____" * (n - i) + '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
        print("____" * (n - i)+'마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.')
        print("____" * (n - i)+'그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')
        rec(i-1)
    print("____" * (n - i) + '라고 답변하였지.')
print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
rec(n)
"""

#별찍기 10 - https://www.acmicpc.net/problem/2447
#어떻게 구현해야 할지 아예 감이 안온다
#3*3 에서 가운데를 비우면 된다. / k가 3을 넘어갈 때가 이해가 안된다.