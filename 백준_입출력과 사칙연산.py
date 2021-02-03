# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 19:34:11 2020

@author: 박지은
BOJ 입출력과 사칙연산
"""
#1. Hello World
print("Hello World!")

#2. We love kriii
print("강한친구 대한육군\n"*2)

#3. 고양이
print("\    /\\\n )  ( \')\n(  /  )\n \(__)|")

#print("\     /\\n)   ( ')\n(  /  )\n \(__)|")
#print("\    /\\\n )  ( ')\n(  /  )\n \(__)|")
#print("\    /\\\n )  ( \')\n(  /  )\n \(__)|")

#4. 개
print("|\\_/|\n|q p|   /}\n( 0 )\"\"\"\\\n|\"^\"`    |\n||_/=\\\\__|")
"""
print("|\\_/|\n|q p|    /}\n( ⊙ )\"\"\"\\\n|\"^\"\'     |\n||_/=\\\\__|")
print("|\\_/|\n|q  p|    /}\n( ⊙ )\"\"\"\\\n|\"^\"\'    |\n||_/=\\\\__|")

print("| \\_/|\n|q  p|    /}\n( ⊙ )\"\"\"\\\n|\"^\"\'    |\n||_/=\\\\__|")

print("dd")

print("|\\_/|\n|q  p|   /}\n( ⊙ )\"\"\"\\\n|\"^\"\'    |\n||_/=\\\\__|")

print("|\\_/|\n|q p|    /}\n( ⊙ )\"\"\"\\\n|\"^\"\'     |\n||_/=\\\\__|")

print("|\\_/|\n|q  p|   /}\n( ⊙ )\"\"\"\\\n|\"^\"\`     |\n||_/=\\\\__|")

print("|\\_/|\n|q  p|   /}\n( ⊙ )\"\"\"\\\n|\"^\"\`    |\n||_/=\\\\__|")

print("|\\_/|\n|q  p|   /}\n( ⊙ )\"\"\"\\\n|\"^\"\`   |\n||_/=\\\\__|")

print("|\\_/|\n|q  p|   /}\n( ⊙ )\"\"\"\\\n|\"^\"\`    |\n||_/=\\\\__|")

print("|\\_/|\n|q  p|   /}\n( ⊙ )\"\"\"\\\n|\"^\"`    |\n||_/=\\\\__|")

print("|\\_/|\n|q p|   /}\n( 0 )\"\"\"\\\n|\"^\"`    |\n||_/=\\\\__|")
"""

#5. A+B
"""
두 수를 입력받아 더하기
"""
"""

A = int(input())
B = int(input())
print(A+B)
"""

"""
다른 방법 (더 유용)
A, B = input().split()  #한번에 두 변수를 받는 방법
print(int(A)+int(B))

a, b = map(int, input().split())
print(a+b)  
#map(바꾸고 싶은 특징, 리스트 등등)
#: 리스트 각 요소들의 특징을 한번에 바꿀 수 있는 함수
#즉, for문을 돌려서 실행해야 할 것을 map 함수로 한번에 가능하게 함.
"""

#6. A-B
"""
a, b = map(int, input().split())
print(a-b)
"""

#7. A*B
"""
a, b = map(int, input().split())
print(a*b)
"""

#8. A/B
"""
a, b = map(int, input().split())
print(a/b)
"""

#9. 사칙연산
"""
A, B = map(int, input().split())
print(A+B)
print(A-B)
print(A*B)
print(A//B)
print(A%B)
"""
 
#10. 나머지
"""
A, B, C = map(int, input().split())
print((A+B)%C, ((A%C)+(B%C))%C, (A*B)%C, ((A%C)*(B%C))%C)
"""

#11. 곱셈
"""
곱셈의 각 위치에 들어갈 값을 구하는 프로그램
"""

"""
틀림
A = int(input())
B = input()
c = A*int(B[-1])
d = A*(int(B[-2:])-int(B[-1]))  #a*b[:-2]-c
e = A*(int(B[:])-int(B[-2:]))  #a*b-d
print(c)
print(d/10)
print(e/100)
print(c+d+e)

"""



"""
a = int(input())
b = input()
b1 = int(b[0])
b2 = int(b[1])
b3 = int(b[2])

x3 = a*b3
x4 = a*b2
x5 = a*b1
x6 = x3+(x4*10)+(x5*100)
print(x3, x4, x5, x6)
"""


"""
다른풀이
a,b = map(int, open(0))
print(b%10*a, b%100//10*a, b//100*a, b*a)

#%는 나머지를 구하는 것
#//는 몫을 구하는 것
472
385
------
2360 -> 472*5 
37760 -> 472*8 
141600 -> 472*3


다른풀이
# 문자열의 인덱스를 이용해서 두번째 입력 받은 문자를 하나씩 숫자로 반환하고 A와 곱한다.
AxB2 = A * int(B[2])
AxB1 = A * int(B[1])
AxB0 = A * int(B[0])
AxB = A * int(B)

print(AxB2, AxB1, AxB0, AxB, sep='\n')
# sep='\n'로 줄바꿈
"""




        