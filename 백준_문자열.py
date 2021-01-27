# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 14:49:23 2021

@author: 박지은

BOJ 문자열
"""

#1. 아스키코드
"""
ord(a): 문자 -> 아스키코드
chr(a): 아스키코드 -> 문자 

a = input()
a = ord(a)
print(a) 
"""

#2. 숫자의 합
'''
실패 : y를 split해서 쪼개기 -> x가 쓸 데가 없음
x = map(int, input())
y = map(int, input())
l = str(y).split('')
s = sum(l)
'''
"""
성공: input을 두 줄에 걸쳐서 받은 다음, for문을 사용하여
첫번째 input a가 input으로 받은 두 번째 숫자의 자리수를 지정해주고,
자리수에 해당하는 숫자의 합을 모아놓을 변수를 하나 설정하여,
그 변수에 숫자 계속 저장해 나가는 방식.

a = int(input())
l = input()
s = 0
for i in range(a):
    c = l[i]
    c = int(l[i])
    s += c
print(s)
"""

#3. 알파벳 찾기
"""
실패: a~z를 어떻게 구현할 것인가
a = input()
for a in [a:z]:
    for c in range(len(a)):
    if c != 

"""
"""
성공: string 모듈을 불러오면 영어 소문자 전체를 불러올 수 있다.
소문자전체가 for문으로 하나씩 도는 동안
input으로 받아온 (if) string의 char하나하나를 for문으로 돌려서

소문자와 input의 두 문자가 똑같으면 index를 result에 담고
 해당 알파벳에 대한 for문은 빠져나온다, 
그렇지 않으면 else로 -1을 result에 담는다.

a가 끝나면 result에 담겼던 숫자를 res에 추가하고
b가 끝난 후 result를 res에 추가하고.. z까지 반복한다.
마지막으로 result를 print한다.

import string

a = input()
res = ""

for alpha in string.ascii_lowercase:
    for c in range(len(a)):
        if alpha in a:
            result = str(a.index(alpha))
            break
        else:
            result = "-1"
    res += result+" "
print(res)
"""    
        
#4. 문자열 반복
"""
input에 몇 개의 케이스가 들어올 것인지 저장하고,
그 숫자대로 for문을 돌려서 (문자열개수, 문자열) input을 받는다.

문자열개수, 문자열을 split" "으로 잘라서 리스트에 넣고
for문에 넣어서 "문자열개수"만큼 돌린다.

 결과를 담을 res변수를 만들고, '반복할 문자열개수'만큼 
 돌린 결과를 res변수에 계속 담고 프린트한다. "\n"넣기
"""
"""
a = int(input())
res = ""
for i in range(a):
    a, b = input().split(" ")
    for j in range(len(b)):
        #print(j)
        res += b[j] * int(a)
    res += "\n"
print(res)
"""

#5. 단어공부
"""
input으로 문자열을 받아서 lower를 적용한다.
(대소문자 가리지 않고 입력값 받기 때문에)

word에 set을 적용하여 단어에 포함되어 있는 unique한
character를 조사하여, 그것을 for문을 돌려서 몇개가 있는지
조사한다. 

if를 사용하여 가장 많이 사용된 알파벳이 여러개 존재하는경우는
(list(set))했을 떄의 리스트 길이가 문자열 길이보다 작을 때)
?를 출력하고, 
else인 경우에는 가장 많이 사용된 알파벳을 출력한다.

아래 코드 정답인 것같은데 인정이 안됨

import operator

word = input().upper()
uni_word = list(set(word))
num = {}
for char in uni_word:
     n = word.count(char)
     num[char] = n
#print(num)
#print(len(list(set(num.values()))))
#print(len(num.values()))
if len(list(set(num.values()))) < len(num.values()):
    print("?")
else:
    res = tuple(sorted(num.items(), key=operator.itemgetter(1), reverse=True))
    print(res[0][0])
"""
"""
다른풀이   

word = input().upper()
uni_word = list(set(word))  # 입력받은 문자열에서 중복값을 제거
num = []
for char in uni_word:
    n = word.count(char)
    num.append(n)  

if num.count(max(num)) > 1 :  # count 숫자 최대값이 중복되면
    print("?")
else :
    max_index = num.index(max(num))  # count 숫자 최대값 인덱스(위치)
    print(uni_word[max_index]) 
"""

#6. 단어의 개수
"""
w = input().split()
print(len(w))
"""    
#7. 상수(거꾸로 출력하기)
"""
nums = input().split()
new_n= ""
new_nums = []
for n in nums:
    for char in n:
        new_n = char + new_n
    new_nums.append(new_n)
    new_n = ''
#print(new_nums)
print(max(map(int,new_nums)))
"""     
"""
다른 답
print(max(input()[::-1].split()))

문자열 거꾸로 출력하는 방법
##1. 뒤쪽의 문자열을 새로운 문자열 앞으로 끌어와서 붙이는 방법
s = "abcde"
s_reverse = ''
for char in s:
    s_reverse = char + s_reverse
print(s_reverse) 

##2. 문자열을 리스트로 바꾸어서 reverse()를 적용하여 join
s_list = list(a)
s_list.reverse()
print("".join(s_list))

##3. reversed()사용
print("".join(reversed(s))) 

##4. 슬라이싱 사용
print(s[::-1]) 
    #[::-1]을 사용하면 문자열을 뒤집어서 반환한다. 튜플도 가능
"""

#8. 다이얼
"""
숫자와 알파벳을 대응하고, 알파벳이 입력되면 숫자를 대응시킨다.
그리고 나온 숫자에 모두 +1을 하여 모두 더한다.

num_str = {"A":2, "B":2, "C":2, "D":3, "E":3, "F":3, "G":4, "H":4, "I":4, "J":5, "K":5, "L":5, "M":6, "N":6, "O":6, "P":7, "Q":7, "R":7, "S":7, "T":8, "U":8, "V":8, "W":9, "X":9, "Y":9, "Z":9}
string = input()
res = []
for n in string:
    res.append(num_str[n]+1)
print(sum(res))
"""

"""
다른풀이: 영어대문자를 한 뭉텅이씩 리스트에 저장하고, 
        input에 해당하는 영어단어가 리스트에 in 하다면 리스트의 인덱스에 +3한다.
        (인덱스는 0부터 시작하고, abc는 3초부터 시작하기 때문에)
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
a = input()
ret = 0
for j in range(len(a)):
    for i in dial:
        if a[j] in i:
            ret += dial.index(i)+3
print(ret)

"""

#9. 크로아티아 문자열
""" 
리스트에 변경문자열을 넣고 이것이 input문자열에 포함되어 있다면
replace하고 count를 센다. 
"""
"""
실패: 똑같은 것이 두 번 출현하게 되면
for문은 한번만 돌기 때문에 뒤에 적용되어야 할 게 적용되지 않음
-> input문자열을 검사하는 게 낫다.
cro_com = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
a = input()
cnt = 0
for string in cro_com:
    if string in a:
        print(string)
        cnt += 1
        a = a.replace(string, "")
        print(a)
        
print(cnt+len(a))
"""

""" 모르겠다 
cro_com = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
a = input()
b = a[:]
res = []

for n in range(len(a)):
    if a[n:n+2] in cro_com:
        res.append(a[n:n+2])
    elif a[n:n+3] in cro_com:
        res.append(a[n:n+3])
        a = a.replace(a[n:n+3], " ")
        print(a)


for char in res:
    b = b.replace(char, "")      
print(b)
print(len(res), res)
print(len(res) + len(b))
"""

#10. 그룹단어 체커 
"""
그룹단어: 각 문자가 연속해서 나타나는 경우
그룹단어인 것: ccazzzbb -> c a z b / kin -> k i n
그룹단어가 아닌 것: zzbbbccb (b가 떨어져 나타나기 때문에)
-> 그룹단어를 판단하는 기준 set해서 앞에 나온 알파벳이 뒤에 나오지 않으면 된다.
--> 중복되지 않으면 된다.
"""
"""
a = int(input())

for i in range(a):
    w = input()
     = list(set(w))
    cnt = 0
    if list(set(a))<list(a): #그룹단어
        pass
    else:
        cnt += 1
print(cnt)
  
cnt = 0
for i in range(a):
    w = input() 
    res = ""
    for i in range(len(w)):
        if w[i] == w[i+1]:
            res += w[i]
            i += 1

        else:
            break
print(res)
"""