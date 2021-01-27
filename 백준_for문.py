# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 13:32:29 2021

@author: 박지은
BOJ for문
"""

#1. 구구단
"""
주어진 N을 가지고 *1 ~*9까지 출력한다.
"""
"""
n = input()
for i in range(1,10):
    print("{0} * {1} = {2}".format(n, i, int(n)*i))
"""


#2. A+B-3
"""
T = int(input())
for n in range(1, T+1):
    A, B = map(int, input().split())
    print(A+B)
"""
"""
for 안에 n이 for문 안에서 쓸모가 없을 때 -> _ 로 표기

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(a+b)
"""

#3. 합
"""
#for문 사용
a = int(input())
i = 0
for n in range(1, a+1):
    i += n
print(i)
"""
"""
#등차수열 이용
a = int(input())
print(a*(a+1)//2)
"""



#4. 빠른 A+B
"""
import sys
a = int(input())
for i in range(a):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)

"""
"""
import sys
#여기에서는 range안에 들어가는 "숫자"가 중요한 것이라 "n회"라는 것이 중요함! -> range(1,11)까지 이렇게 안써도 됨!
for i in range(int(input())):
    print(sum(map(int, sys.stdin.readline().split())))
    
import sys
a = int(input())
for i in range(a):
    a, b = map(int, sys.stdin.readline().split()) #split->list/ list 안의 숫자의 합을 더하는 것이 sum()
    print(a+b)
"""


#5. N찍기
"""
for i in range(int(input())):
    i += 1
    print(i) #i가 진행될수록 1씩 더한다 
    
for i in range(1, int(input())+1):
    print(i)
"""    

#6. 기찍N
"""
N = int(input())
for n in range(N, 0, -1):
    print(n)

for n in range(int(input()), 0, -1):
    print(n)
    
#range 거꾸로 찍기 -> range(시작숫자, 마지막숫자-1, -1)
for n in range(6, 1, -1):
print(n)    #6, 5, 4, 3, 2
"""

"""
다른 정답
a = map(str,range(int(input()),0,-1))
print("\n".join(a))

간단히 한 버전->
print("\n".join(map(str, range(int(input()), 0, -1))))
"""



#7. A+B-7
"""
for n in range(1, int(input())+1):
    print("Case #{0}: {1}".format(n, sum(map(int, input().split()))))
"""
          
#8. A+B-8 (#7과 동일)
"""
for i in range(n):
    x,y = map(int, input().split())
    print("Case #%d: %d" % (i+1,x+y))
"""
"""
for N in range(int(input())):
    a, b = map(int,input().split())
    print("Case #{0}: {1} + {2} = {3}".format(N+1, a, b, a+b))
"""



#9. 별찍기 -1
"""
for n in range(1, int(input())+1): print("*"*n)
"""

#10. 별찍기 -2
"""
첫째 줄에 별 1개, 둘째 줄에 별 2개...
오른쪽 정렬
"""
"""
#실패
N = int(input())
for n in range(N+1):
    print('{0:>{0}}'.format(N,"*"*n))

#성공
N = int(input())
for n in range(1,N+1):
    print('{0}{1}'.format(" "*(N-n),"*"*n)) #1 -> 4, 1/ 2-> 3, 2
    
    #or " "*(N-n)+"*"n
"""

#11. X보다 작은 수
#10871

N, X = map(int,input().split())
for n in map(int,input().split()):
    if n<X:
        print(str(n), end=" ")
        
        #B = []
        #B.append(n)
#print(' '.join(B))

 
"""
#if n<X == True: 왜 안되지
n, x = map(int, input().split())
a = [ i for i in input().split() if int(i) < x ]
print(' '.join(a))
"""

