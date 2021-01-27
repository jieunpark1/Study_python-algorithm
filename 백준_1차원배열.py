# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 13:13:18 2021

@author: 박지은
BOJ 일차원 배열
"""

#1. 최소, 최대
"""
a = int(input())
b = list(map(int, input().split()))
print(min(b), max(b))
"""

#2. 최댒값
"""
n = []
for i in range(9):
    a = int(input())
    n.append(a)
b = max(n)
c = n.index(b)+1
print("{0}\n{1}".format(b,c))
"""

#3. 숫자의 개수
"""


mul = 1
for _ in range(3):
    mul *= int(intput())
for i in range(0,10):
    print(str(mul).count(str(i)))
    
"""   
"""
"""

#4. 나머지
"""
두 자연수가 있을 때 A%B는 A를 B로 나눈 나머지이다. 
수 10개를 입력받은 후 이를 42로 나눈 나머지를 구한다.
서로 다른 값이 몇 개 있는지 출력.
"""

"""
a = {int(input())%42 for i in range(10)}
print(len(a))
"""


#5. 평균
"""
점수의 최댓값을 골라서 M이라 하고,
모든 점수를 점수/M*100으로 고쳤다.
"""
"""
N = int(input())
n = list(map(int, input().split()))
M = max(n)
for i in range(N): n[i] = n[i]/M*100
print(sum(n)/N)
"""

#6.OX퀴즈
"""
for n in range(int(input())):
    a = input()
    a_list = a.replace("X", " ")
    a_list = a_list.split()
    #print(a_list)
    cnt = 0
    for li in a_list:
        res = li.count("O")
        cnt += (res*(res+1)//2)
    print(cnt)
"""
"""
다른 정답
    result = 0
    cnt = 0
    for i in r_line:
        if i == "O":
            cnt = cnt+1
            result = result+cnt
        else:
            cnt = 0
    print(result)

"""

#7. 평균은 넘겠지
"""
for _ in range(int(input())):
    a = [int(x) for x in input().split()]

    sum_stu = 0
    for x in a[1:]:
        sum_stu += x

    avg = sum_stu / (len(a)-1)
    
    cnt_stu = 0
    for stu in a[1:]:
        if stu > avg:
            cnt_stu += 1

    res = "%0.3f" % (cnt_stu/a[0]*100)
    print(str(res)+"%")
"""        
    
