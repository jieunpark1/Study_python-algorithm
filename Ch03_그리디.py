# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 22:17:12 2021

@author: 박지은
Ch03_그리디
"""


#4. 1이 될 때까지
"""
start_t = time.time()
n, k = map(int, input().split())
result = 0

while True:
    target = (n//k)*k
    result += (n-target)
    n = target
    if n<k:
        break
    result += 1
    n //= k
    
result += (n-1)
print(result)
end_t = time.time()
run_t = end_t - start_t
print(run_t) #0.0026
"""
"""
s_t = time.time()
n, k = map(int, input().split())
cnt = 0
while n!= 1:
    if n % k == 0:
        n //= k
        cnt += 1
    else:
        n -= 1
        cnt += 1

print(cnt)
e_t = time.time()
r_t = e_t - s_t
print(r_t) #0.0027
"""

#2. 큰 수의 법칙
n, m, k = map(int, input().split())
num = sorted(list(map(int, input().split())), reverse=True)
result = 0

first_num = num[0]
sec_num = num[1]
#print(first_num)
#print(sec_num)
    
if first_num != sec_num:
    result += first_num * (m // k) * k
    result += sec_num * (m % k)
else:
    result = first_num * m
    print(result)
print(result)
#책의 예시
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

#가장 큰 수가 더해지는 횟수 계산
count = int(m / (k+1)) * k
count += m % (k+1)

result = 0
result += (count) * first #가장 큰 수 더하기
result += (m-count) * second  #두 번째로 큰 수 더하기

print(result)    



#3. 숫자 카드 게임
n, m = map(int, input().split())

mins = []
for _ in range(n):
    nums = input().split()
    mins.append(min(nums))
min_sort = mins.sort()
print(max(min_sort))
#2중 반복문 구조를 이용하는 답안 예시
n, m = map(int, input().split())

result = 0
for i in range(n):
    data = list(map(int, input().split()))
    #현재 줄에서 가장 작은 수 찾기
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
    #가장 작은 수들 중에서 가장 큰 수 찾기
    result = max(result, min_value)
print(result)




#기출문제 1. 모험가 길드
"""
num = int(input())
fri_num = input().split()

res = num
for i in range(len(fri_num)):
    fri_num[i] = int(fri_num[i])
    s_fri_num = sorted(fri_num, reverse=True)
    if fri_num[i] == max(fri_num):
        res -= fri_num[i]
        s_fri_num = 
"""        

#정답
n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0 #총 그룹 수
count = 0 #현재 그룹에 포함된 모험가의 수

for i in data: #낮은 공포도부터 확인
    count =+ 1 #현재 그룹에 i 멤버 포함시키기
    if count >=i: #현재 그룹에 포함된 모험가의 수가 공포도보다 높으면 그룹을 결성한다
        result += 1 #총 그룹의 수 증가시키기
        count = 0 #현재 그룹에 포함된 모험가의 수 초기화
print(result) #총 그룹의 수
        

#기출2. 곱하기 혹은 더하기
data = input()
result = int(data[0])
for i in range(1, len(data)):
    # 두 수 중에서 하나라도 0 혹은 1인 경우, 곱하지 말고 더하기 연산을 수행한다.
    num = int(data[i])
    if num<1 or result <=1:
        result += num
    else:
        result *= num
print(result)
#기출문제 2. 곱하기 혹은 더하기
"""
a = input()#숫자를 하나씩 쪼개서 받아옴.
a = sorted(a, reverse=True) #문제 잘못이해함.
print(a)
res = 0
if a[-1] == "0":
    res = int(a[-2])
    for i in range(len(a)-2):
        res *= int(a[i])
        print(int(a[i]))
        print(res)
else:
    for i in range(len(a)):
        print(a[i])
        res *= int(a[i])
print(res)
"""


#기출3. 문자열 뒤집기
n = input()
cnt_box = []

count_1 = n.split("0")
count_1 = [v for v in count_1 if v]
count_0 = n.split("1")
count_0 = [v for v in count_0 if v]
#print(count_1)
#print(count_0)

cnt_box.append(len(count_1))
cnt_box.append(len(count_0))
#print(cnt_box)
print(min(cnt_box))
#print(min(len(count_1), len(count_0)))

#답안 예시: 전체 리스트의 원소를 앞에서부터 하나씩 확인
data = input()
count0 = 0 #전부 0으로 만드는 경우
count1 = 0 #전부 1로 만드는 경우

#첫 번째 원소에 대해서 처리
if data[0] == "1": #첫번째 원소가 0이면 일단 전부1로 만드는 경우가 +1
    count0 += 1
else:
    count1 += 1
    
#두 번째 원소부터 모든 원소를 확인하며
for i in range(len(data) - 1): #두 번째 원소부터인데 왜 1부터 시작안하지
    if data[i] != data[i+1]: #0인덱스와 1인덱스를 비교
        #다음 수에서 1로 바뀌는 경우
        if data[i+1] == "1": #0에서 1로 바뀌면 전부0으로 만드는 경우를 +1
            count0 += 1
        #다음 수에서 0으로 바뀌는 경우
        else: 
            count1 += 1 #1에서 0으로 바뀌면 전부0으로 만드는 경우를 +1
print(min(count0, count1))