# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 13:26:37 2021

@author: 박지은
"""

#1. 두 수 비교하기
"""
A, B = map(int, input().split())
if A == B :
    print("==")
elif A > B :
    print(">")
else:
    print("<")
"""

#2. 시험 성적
"""
A = int(input())
if A >=90:
    print("A")
elif A >=80:
    print("B")
elif A >=70:
    print("C")
elif A >=60:
    print("D")
else:
    print("F")
"""

#3. 윤년
"""
윤년이면 1(연도가 4의 배수이면서, 100의 배수가 아닐 때 혹은 400의 배수일 때)
윤년이 아니면 0을 출력
"""
"""
a = int(input())
if a % 4 == 0 and (a % 100 != 0 or a % 400 == 0) :
    print("1")
else:
    print("0")
"""

#4. 4분면 고르기
"""
점의 좌표를 입력받아 어느 사분면에 속하는지 알아내기 1234사분면 중 하나
"""
"""
a = int(input())
b = int(input())
if a<0 and b<0:
    print("3")
elif a>0 and b>0:
    print("1")
elif a>0 and b<0:
    print("4")
else:
    print("2")
"""

#5. 알람시계
"""
H, M = map(int, input().split())
if M > 45:
    print(H, M-45)
elif M == 45:
    print(H)
else:
    if H == 0:
        print("23", 60-(45-M))
    else:
        print(H-1, 60-(45-M))

n = int(input())  #int : not iterable
for n in 10:
    print("2 * {0} = {1}".format(n, 2*n))    

n = input()
for i in range(1,10):
    print("{0} * {1} = {2}".format(n, i, int(n)*i))
"""