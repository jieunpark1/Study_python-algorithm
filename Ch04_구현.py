# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 20:31:13 2021

@author: 박지은
Ch04_구현
"""

#예제 4-1. 상하좌우
"""
a = int(input())
b = input().split()

x, y = 1, 1
x_list = [1]
y_list = [1]
for alpha in b:
    if alpha == "L":
        y -= 1
        y_list.append(y)
    elif alpha == "R":
        y += 1
        y_list.append(y)
    elif alpha == "U":
        x -= 1
        x_list.append(x)
    elif alpha == "D":
        x += 1
        x_list.append(x)
    #print(x_list)
    #print(y_list)
    if x == 0 or  x > a:
        x_list.pop()
        x = x_list[-1]
    elif y == 0 or y > a:
        y_list.pop()
        y = y_list[-1]
print(x, y)

#답안 예시
n = int(input())
x, y = 1, 1
plans = input().split()

#L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ["L", "R", "U", "D"]

#이동 계획을 하나씩 확인
for plan in plans:
    #이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    
    #공간을 벗어나는 경우는 무시한다. nx가 0일 때 nx가 x로 할당되는 것을 막아줌. 
    #따라서 x는 이 이전에 정상적으로 옮겨진(nx가 x로 할당된 좌표) x의 좌표가 된다.
    if nx<1 or ny<1 or nx>n or ny>n: 
        continue
    
    x, y = nx, ny #64라인의 조건 확인 후 nx를 x에 할당함으로써 조건에 맞지 않으면 x에 할당하지 않음. 
                    #x, ny 2개의 변수가 필요한 이유
print(x, y)

"""   
#민화언니
"""
n=int(input())
move_list = list(input().split())
#현재 위치
dx=[0, 0, -1, 1] #왼오위아래
dy=[-1, 1, 0, 0]
x,y=1,1
#print(move_list)

for j in move_list:
    if j=='L':
            x+=dx[0]
            y+=dy[0]
    elif j=='R':
            x+=dx[1]
            y+=dy[1]
    elif j=='U':
            x+=dx[2]
            y+=dy[2]
    elif j=='D':
            x+=dx[3]
            y+=dy[3]
    #보정
    if x<1:
        x+=1
    elif y<1:
        y+=1
    elif x>n:
        x-=1
    elif y>n:
        y-=1
print(x, y)
"""
#미소언니
"""
n = int(input())
direction = input().split()

x=1; y=1

for dir in direction:
    if dir == "R" and y<n:
        y+=1
    elif dir == "L" and y>1:
        y-=1
    elif dir == "U" and x>1:
        x-=1
    elif dir == "D" and x<n:
        x+=1

print(x,y)
"""
#예제 4-2 시각
"""
n = input()
cnt = 0
for h in range(int(n)+1):
    for m in range(60):
        for s in range(60):
            s = str(s)
            m = str(m)
            h = str(h)
            if "3" in h or "3" in m or "3" in s:
                cnt += 1
print(cnt)

#답안 예시
h = int(input())

count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            #매 시각 안에 3이 포함되어 있다면 카운트 즈가
            if "3" in str(i)+str(j)+str(k):
                count += 1
print(count) #ex 03시 20분 35초 -> "032035"로 제작 -> 3이 in 하는지 봄.

#미소언니
h = int(input())
ms = 0 #분과 초를 한번에 

for i in range(60):
    if i//10 == 3 or i%10 == 3: #10의자리가 3, 1의 자리가 3
        print(i)
        ms+=1
h3=60*60 #3시일 경우 -> 모든 분, 초에 대해서 카운트 가능
over3 = h*ms*60*2+h3 #3시 넘었을 때
under3 = (h+1)*ms*60*2 #3시 안넘었을 때

if h >= 3:
    print(over3)
else:
    print(under3)

"""
#민화언니
"""
N=int(input())
three=[3,13,23]  #n<=23
k=0
#n=3일때 60 * 60 = 3600개 -> n=5일때 11475개-3600/5 = 1575개
#n이 3일 때를 지정해놓고, 그 외의 n숫자이면 1575를 더한다
if N==0:
    print(1575)
elif N!=0:
    for i in range(N+1): #0시를 포함해야하기 때문
        if i in three:
           k+=3600
        else:
            k+=1575
    print(k)
#숫자가 어떻게 도출되는지 변수로 나타내주는게 좋다
"""


#실전문제2. 왕실의 나이트
"""
c,r = input()
c = ord(c) #a = 97 (문자 -> 숫자 변환: 유니코드 사용 )
r = int(r)
dx = [2, 2, -2, -2, 1, -1, 1, -1]
dy = [-1, 1, -1, 1, 2, 2, -2, -2]

cnt = 0
for i in range(8):      
    nx = c + dx[i]
    ny = r + dy[i]
    #print(nx, ny)
    if nx>0 and ny>96 and nx < 9 and ny < 105:
        print(nx, ny)
        cnt += 1
print(cnt)

#미소언니
xy = input()
x=ord(xy[0])-96; y=int(xy[1])

if (x<=2 or x-6>0)and (y<=2 or y-6>0):
    if x==y==1 or x==y==8:
        print(2)
    elif x==y==2 or x==y==7:
        print(4)
    elif x==1 or x==8 or y==1 or y==8:
        print(3)
    else:
        print(6)
else:
    print(8)
        
#답안예시
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord("a")) +1 #초깃값=1 

#나이트가 이동할 수 있는 8가지 방향
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)] #튜플로

#8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    #이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    #해당 위치로 이동이 가능하다면 카운트 증가
    if next_row>=1 and next_row<=8 and next_column>=1 and next_column<=8:
        result += 1
print(result)
"""

#실전문제3. 게임 개발
#답안 예시
"""
n, m = map(int, input().split())

d = [[0] * m for _ in range(n)] #방문 위치를 저장하기 위한 맵을 생성
print(d)
x, y, direction = map(int, input().split()) #캐릭터의 x,y,방향 입력받기
d[x][y] = 1 #현재 좌표 방문처리
print(d)
#전체 맵 정보 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))
    
#북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

#왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3
        
#시뮬레이션 시작
count = 1
turn_time = 0
while True:
    #왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    
    #회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if [nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    #회전한 이후 정면에 가보지 않은 칸이 없거나(모두 가봤거나) 바다인 경우
    else:
        turn_time += 1
    
    #네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        
        #뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0:
            x = nx
            y = ny
        #뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time = 0
print(count)

"""

#기출문제7. 럭키 스트레이트
"""
n = input()
sum_prev = 0
sum_lat = 0
for i in range(len(n)):
    if i >= len(n)//2:
        #print(i)
        sum_lat += int(n[i])
    else:
        sum_prev += int(n[i])

if sum_prev == sum_lat:
    print("LUCKY")
else:
    print("READY")
"""
#민화 풀이
"""
n=input()
half_len=len(n)//2-1

#문자열 반으로 자르기
#각각 리스트에 따로 넣어서 더한 뒤에 같은지, 다른지 확인해보면 되겠네
left=[]
right=[]

i=0
for j in n:
    if i<=half_len:
        left.append(j)
        i+=1
    elif i>half_len:
        right.append(j)

#각 리스트의 요소를 숫자로 바꾸기
left = list(map(int, left))
right = list(map(int, right))
#print(left)
#print(right)

#같은가 다른가 비교
if sum(left)==sum(right):
    print("LUCKY")
elif sum(left)!=sum(right):
    print("READY")
"""

#윤우
"""
n = list(input())
lucky_left = 0
lucky_right = 0

for i in range(len(n)//2):
  lucky_left += int(n[i])
  

for j in range(len(n)//2, len(n)):
  lucky_right += int(n[j])
  

if lucky_left == lucky_right:
  print('lucky')
else:
  print('ready')
"""
#미소언니
"""
point=input()
half=int(len(point)/2)
left=0
right=0

for i in range(half):
    left+=int(point[i])

for j in range(len(point),half,-1): #point의 range를 거꾸로 돌림()
    print(point[j-1]) #마지막 index-> 5 / len은 6 --> 인덱스에서 1을 빼주어야 한다.
    right+=int(point[j-1])


#for j in range(half, len(point)): #이렇게 써도 동일!
#    right+=int(point[j])


if left == right:
    print("LUCKY")
else:
    print("READY")
"""

#예시답안
"""
n = input()
length = len(n)
summary = 0

for i in range(length//2):
    summary += int(n[i])
for i in range(length//2, length):
    summary -= int(n[i])    #앞부분은 summary에 더하고, 뒷부분은 다시 summary에서 빼서 0이면 lucky
if summary == 0:
    print("LUCKY")
else:
    print("READY")
"""

#기출문제8. 문자열 재정렬
"""실패
s = input()
nums = 0

for i in s:
    try:
        if int(i) in list(range(10)):
            nums+= int(i)
            s.pop(i)
    except:
        pass

print("{0}{1}".format(s.sort(), nums))"""

"""
import re
n = input()
alpha = re.compile("[A-Z]")
result = alpha.findall(n)
result.sort()

nums = re.compile("[0-9]")
result2 = nums.findall(n)
result2 = sum(map(int, result2))

print("{0}{1}".format("".join(result), result2))
"""
#답안예시
"""
data = input()
result = []

value = 0

for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)
result.sort()

if value != 0:
    result.append(str(value))
print("".join(result))
"""

#기출문제9.문자열 압축
#어렵다..

"""
s = input()
print(solution(s))


s = "abcabcabc"
for i in range(len(s)//2):
    print("i", i)
    for j in range(len(s)):
        print(s[i:j+i])

def solution(s):
    box = []
    for i in range(len(s)):
        for j in range(0, len(s), i+1):
            .append(s[0:i]
"""    
        
#답안 예시
#ex) aabcc
"""
def solution(s):
    answer = len(s)
    
    #1개 단위(step)부터 압축 단위를 늘려가며 확인
    #step: 문자열 1개단위, 문자열2개단위...
    #왜 range(1, len(s)//2+1)인가? 최대로 큰 문자열 단위는 s의 절반길이이기 때문
    for step in range(1, len(s) // 2 + 1):
        compressed = "" #압축 후 결과 문자열
        prev = s[0:step] #s의 인덱스0부터 조사해야 함(조건), 기준이 되는 문자열
        print("crit",prev)
        count = 1
        
        #단위(step) 크기만큼 증가시키며 이전 문자열과 비교<검색>
        for j in range(step, len(s), step):#s의 문자열단위 인덱스부터 s의 끝자리까지 s의 문자열단위 인덱스 스텝만큼 for문 돌림
            #step = 1(s의 인덱스 1), step = 1
            
            #이전 상태와 동일하다면 압축 횟수(count)증가
            if prev==s[j : j+step]: 
                count +=1
                print("prev", prev, "count", count)
            #다른 문자열이 나온다(압축x)
            else:
                compressed += str(count) + prev if count>=2 else prev #count가 2이상이면 count+문자열 / 아니면 그냥 문자열만 compressed에 담기
                print("compr", compressed)
                prev = s[j : j+step] #prev초기화 - prev를 다음 문자열 기준으로 하게 만들기
                print("new_prev", prev)
                count = 1
        
        #남아 있는 문자열에 대해서 처리
        compressed += str(count) + prev if count >= 2 else prev
        print(compressed)
        #만들어지는 압추 문자열이 가장 짧은 것이 정답
        answer = min(answer, len(compressed)) #answer를 계속 update해서 for문 후에 나오는 결과answer과 계속 비교
        print(answer)
    return answer

s = input()
print(solution(s))               
        
"""    
#기출문제10. 자물쇠와 열쇠
        