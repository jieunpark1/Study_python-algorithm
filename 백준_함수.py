# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 19:14:00 2021

@author: 박지은
"""

#1. 정수 N개의 합
"""
정수 n개가 주어졌을 때, n개의 합을 구하는 함수를 작성하시오
"""

"""
def solve(a):
    ans = 0
    for i in a:
        ans += i
    return ans
"""

#2. 셀프 넘버
"""
n, d(n), d(d(n)), d(d(d(n)))..
n이 33이라면, d(n) = 33 + 3+ 3 = 39, d(d(n)) = 39 + 3+ 9 = 51..
33은 39의 생성자, 39는 51의 생성자이다.

생성자가 없는 숫자를 셀프 넘버라고 한다. 100보다 작은 셀프넘버는
총 13개가 있다. 1, 3, 5, 7, 9, 20, 31, 42, 53, 64, ,,
n이 만보다 작거나 같을 동안 셀프넘버인 수를 재귀함수를 사용하라 
d(n)이 되게 하는 n이 없다.
"""


"""
def selfnum():
    i = 0
    bx = []
    for i in range(1, 1001):
        res = i + i//10 + i%10 #결국 자기 자신의 값을 더해나가는 것으로 일반화시킬 수 있다.
        bx.append(str(res))

    for j in range(1, int(max(bx))+1):
        if str(j) not in bx:
            print(j)
selfnum()


#민화
def self_number():
    num_list=set(range(1, 10001)) #같은 자료형끼리 뺄 수 있음
    not_self_num=set()
    for num in num_list:
        for n in str(num):
            num+=int(n)
        not_self_num.add(num)
    cha=num_list-not_self_num
    for c in sorted(cha):
        print(c)

self_number()

#미소
def self_number():
    lst = []
    for i in range(1,10001):
        st = str(i)
        sum = i #한수는 자기 자신에 각 자리의 수를 더한 값이므로, sum에 먼저 자기 자신을 넣어놓는다.
        for char in st: #i의 각 자리를 하나씩 불러옴
            sum+= int(char) #각 자리를 int로 바꾸고 sum에 더한다
            lst.append(sum) 


#내가 다시 해보기
def self_number():
    lst = []
    for i in range(1,10001):
        st = str(i)
        sum = i #한수는 자기 자신에 각 자리의 수를 더한 값이므로, sum에 먼저 자기 자신을 넣어놓는다.
        for char in st: #i의 각 자리를 하나씩 불러옴
            sum+= int(char) #각 자리를 int로 바꾸고 sum에 더한다
        lst.append(sum) 
#10000까지 중 여기에 없는
    for i in list(set(range(1,10001))):
        if i not in lst:
            print(i)
            
self_number()
"""

#3. 한수
"""
어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 
그 수를 한수라고 한다. 등차수열은 연속된 두 개의 수의 차이가 
일정한 수열을 말한다. N이 주어졌을 때, 1보다 크거나 같고, 
N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오. 
ex) 110 -> 99 / 1 -> 1
"""
"""
def f(n):
    i = 0        
    for j in range(1, n+1):
        n = str(n)
        j = str(j)
        if int(j) < 100:
            i += 1
        elif (int(j[1]) - int(j[0])) == (int(j[2]) - int(j[1])):
            i += 1
    return i

n = int(input())
print(f(n))
     

#민화언니: 한수 직접 계산
n=input()
def hansu(n):
    hansu_list=[111,123,135,147,159,210,222,234,246,258,321,333,345,357,369,420,432,444,456,468,531,543,555,567,579,630,642,654,666,678,741,753,765,777,789,840,852,864,876,888,951,963,975,963,975,987,999]
    if len(n)==1:
        print(n)
    elif len(n)==2:
        print(n)
    elif len(n)==3:
        n=int(n)
        selected_list=[]
        for i in hansu_list:
            if i<=n:
                selected_list.append(i)
        print(len(selected_list)+99)
    elif len(n)==4:
        print(len(selected_list)+99)
hansu(n)
"""
"""
다른 풀이
100의 자리 -> n // 100
10의 자리 -> n % 100의 //10 ==> n %100 //10
1의 자리 -> i %10
"""
    
        
        

