# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 13:16:14 2021

@author: 박지은
BOJ While
"""

#A+B-5
#10952
"""
a, b = map(int, input().split())
while a+b != 0:
    print(a+b)

while sum(map(int, input().split())) != 0:
    print()
"""
"""
while True:
    a, b = map(int, input().split())
    if a+b == 0:
        break
    else:
        print(a+b)
        
p=input()
while p!='0 0':
    print(int(p[0])+int(p[2]))
    p=input()        
    
while True:
	print(eval(input().replace(' ','+').replace('0+0','exit()')))
"""    

#A+B-4
#10951
"""
##1
import sys
for line in sys.stdin:
    a, b = map(int, line.split())
    print(a + b)
#2    
while 1:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except:
        break
#3    
try:
    while 1:
        a, b = map(int, input().split)
        print(a+b)
except:
    exit()
"""    


#1110
#3. 더하기 사이클
"""
#1) 내가 짠 코드
코드가 너무 길고 , str대신에 int타입으로 불러와서 적절한 때에 str로 바꾸어주는 것이 편리.
i = 1
x = str(input())
old_x = x[:]
while True:
    if len(x) == 1:
        x = x*2  #이 부분에서 왜 *2를 하는지 모르겠다.
        if x == old_x:
            break
        elif "0"+old_x == x:
            break
        else:
            i += 1
    else:
        sum_x = str(int(x[0])+int(x[1]))
        x = '{0}{1}'.format(x[1], sum_x[-1])
        if x == old_x:
            break
        elif "0"+old_x == x:
            break
        else:
            i += 1
print(i)
#흐름 ex) 1 -> 12 -> 23 -> 35 ---

#미소언니가 짠 코드: int로 불러오고, 10의 자리를 //10으로(몫 정수), 1의 자리를 %10(나머지)
#표시함으로써 숫자로 자릿수를 계산할 수 있다. 보기에도 편하고 간단한 
n = int(input())
new=n
count = 0
while True:
    n1 = new//10
    n2 = new%10
    n3 = (n1+n2)%10
    new=10*n2+n3 
    count+=1
    if n==new:
        break
print(count)


#2) 다른사람이 짠 코드
N=int(input())
a=0
b=N
while b!=N or a==0:
    b=b%10*10+(b//10+b%10)%10
    a+=1
print(a)

#3) 다른사람이 짠 코드2
a = int(input())
b, c = a, 0           #b = a, c = 0 한 줄에 두 개의 변수를 할당하는 방법
while a!=b or c==0:
    a = a%10*10 + (a%10+a//10)%10
    c+=1
print(c)
""" 
