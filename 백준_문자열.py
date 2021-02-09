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

다른풀이: input을 map함수 적용하면 문자열 한 자리씩 잘려서 리스트형태로 나옴.
input()
print(sum(map(int, input())))
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

"""더 간단한 방법
#find는 찾는 문자가 문자열에 없으면 -1반환
#알파벳만 for문을 돌면 되고, 그 알파벳을 input에서 어디에 위치하는지 찾아라.(find)
import string

a = input()

for alpha in string.ascii_lowercase:
    print(a.find(alpha)) 
"""

"""다른 방법: ascii코드를 이용
word = input()
alphabet = list(range(97,123))  # 아스키코드 숫자 범위

for x in alphabet :
    print(word.find(chr(x))) 
    
    
    
    
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


t=int(input())
for i in range(t):
 a,b=input().split()
 for j in b:
  print(int(a)*j, end='')
 print()


"""



#5. 단어공부
"""
input으로 문자열을 받아서 upper를 적용한다.
(대소문자 가리지 않고 입력값 받기 때문에)

word에 set을 적용하여 단어에 포함되어 있는 unique한
character를 조사하여, 그것을 for문을 돌려서 몇개가 있는지
조사한다. 그리고 이것을 딕셔너리 형태로 저장

if를 사용하여 가장 많이 사용된 알파벳이 여러개 존재하는경우는
(
딕셔너리의 value를 list(set))했을 때의 리스트 길이가
value 길이보다 작을 때=> 개수가 똑같은 것이 있다
==> but, 이 경우 max개수가 아닐 때 중복발생해도 ?나옴
ex) aabbccc -> ?(원래는 3출력해야 함))<실패>)
?를 출력하고, 
else인 경우에는 가장 많이 사용된 알파벳을 출력한다.

--> 1. if max가 여러개이면 ->? / 아니면 max를 출력하라
--> 2. if max의 count가 1개이면 -> max 개수출력 / 아니면 ?

<실패>
import operator

word = input().upper()
uni_word = list(set(word))
num = {}    #max인 문자열을 찾아야 하므로 딕셔너리를 사용 
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

<max의 count를 세기>#uni_word와 num의 정보는 같은 인덱스에 위치->굳이 딕셔너리를 안써도된다
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


<max인 num의 count를 해서 1이면 알파벳 출력>
word = input().upper()
uni_word = list(set(word))  # 입력받은 문자열에서 중복값을 제거
print(uni_word)
num = []
for char in uni_word:
    n = word.count(char)
    num.append(n)  
print(num)

#max(num) -> 4
if num.count(max(num)) == 1 :  # count 숫자 최대값이 중복되면
    max_index = num.index(max(num)) 
    print(num.index(max(num))) #uni_word와 num의 정보는 같은 인덱스에 위치
    print(uni_word[max_index])

else :
    print("?")

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
"""
c=jc-jdz=jd-jljjnjjs=jz=joooooc=z=c-z=dz=z=d-z=ljz=njz=s=z=z
cro_com = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
a = input()
b = a[:]
res = []

for n in range(len(a)):
    if a[n:n+2] in cro_com:
        res.append(a[n:n+2])
    elif a[n:n+3] in cro_com:
        res.append(a[n:n+3])
        a = a.replace(a[n:n+3], " ") #dz=돌고 z=돌기 때문에 순서를 바꿔도 둘다 검색됨. 
        print(a) #근데 replace를 하면 해당되는 것이 여러개 있으면 모두 삭제되기 때문에 오답.


for char in res:
    b = b.replace(char, "")      
print(b)
print(len(res), res)
print(len(res) + len(b))

"""
"""답
1. 모두 "1"로 바꾼다 -> 크로아티아 문자열 시퀀스를 1개의 문자열로 치환시킨다. (2개 이상의 시퀀스 문자열이 1개로 바뀐다)
c = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
a = input()
for i in c:
  a = a.replace(i, "1")
print(len(list(a)))


2. 정규표현식을 사용, 원리는 1번과 동일하다.
import re
print(len(re.sub('dz=|[ln]j|\w\W','Z',input())))

"""

#10. 그룹단어 체커 
"""
그룹단어: 각 문자가 연속해서 나타나는 경우
그룹단어인 것: ccazzzbb -> c a z b / kin -> k i n
그룹단어가 아닌 것: zzbbbccb (b가 떨어져 나타나기 때문에)
-> 기준 
앞에 나왔던 문자가 뒤에 다시 나오면 그룹단어가 아니다
uni_Word가 한바퀴 돌고나서 다시 사용되면 그룹단어가 아니다
"""
"""중복문자 하나로 줄이기"""




