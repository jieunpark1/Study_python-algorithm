# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 20:37:17 2021

@author: jieunpark
"""
#다이나믹 프로그래밍
# 이미 계산된 결과는 별도의 메모리 영역에 저장하여 다시 계산하지 않도록 한다.
#top-down(하향식) & bottom up(상향식) 

#동적 계획법 
#일반 프로그래밍에서 Dynamic = 프로그램이 실행되는 도중에 필요한 메모리를 할당하는 기법
#즉 메모리 필요할 때마다 필요한 공간을 프로그램 실행 도중에 갖다 쓰는 것
# 다이나믹 프로그래밍에서의 다이나믹은 별 다른 의미가 없음

#다이나믹 프로그래밍 조건
#최적 부분 구조: 큰 문제를 작은 문제로 나눌 수 있을 때, 작은 문제의 답을 모아서 큰 문제를 해결 할 수 있을 떄
#중복되는 부분 문제: 부분 문제가 중첩되어 여러번 등장한다. 동일한 작은 문제를 반복적으로 해결해야 할 떄
#ex) 피보나치 수열 -> 어떤 피보나치 수열은 전과 전전의 피보나치 수를 더한 것이다.


#피보나치(다이나믹 프로그래밍 적용 x)
def fibo(x):
    print("f(", x, ") 호출됨")
    if x == 1 or x == 2:
        return 1
    return fibo(x-1) + fibo(x-2)

print("#동적 프로그래밍으로 작성하지 않은 피보나치 배열")
print(fibo(6))

#문제: n이 커지면 중복되는 n이 많아진다.
#해결: 다이나믹 프로그래밍 알고리즘 사용!
"""  
조건1. 최적 부분 구조
큰 문제 하나를 해결하기 위해 작은 것이 필요하다.
조건2. 중복되는 부분 문제
중복되는 부분문제 n이 여러번 반복된다.
=> 따라서 하나의 큰 문제가 해결되는 과정에서
동일한 작은 문제가 반복적으로 해결되는 것을
요구하고 있으므로, 피보나치 수열을 다이나믹 프로그래밍
사용할 수 있다.

구현은 상향과 하향 두 가지 방식이 있다.
#하향식: top-down 메모이제이션
-한 번 계산한 결과를 메모리 공간에 메모하는 기법
-작은 문제의 값을 별도의 공간에 저장해놓았다가 다시 가져오는 것. 
-값을 기록해 놓는다는 점에서 '캐싱'이라고도 한다.
-기억해 두는 변수 이름: memo, cache, table, dp, d
-작은 문제들을 재귀적으로 돌려서 기록해놓고 메모기법 

#상향식: bottom-up 상향식
-아래쪽에서부터 작은 문제를 하나씩 해결해가면서
그것을 해결해서 큰 것을 해결해나간다
-반복문 이용
-다이나믹 프로그래밍의 전형적인 타입은 bottom up방식
-결과 저장용 리스트는 dp 테이블 (리스트=다른 언어의 배열)

#메모이제이션은 다이나믹 프로그래밍에 국한된 개념은 아니고,
한번 기록해 놓은 것을 따로 저장해둔다는 포괄적인 개념으로 사용가능
그것이 동적 프로그래밍을 위해 활용되지 않아도 된다.


"""

#동적 프로그래밍을 적용한 피보나치 배열
#1. top-down(재귀함수 사용)
d = [0] * 7 #0~99까지의 인덱스, 99번째 피보나치 구하고 싶어서

def fibo_topdown(x):
    print("f(", x, ") 호출됨")
    if x == 1 or x == 2:
        return 1
    
    #메모이제이션 된 x가 있다면, 거기에서 데이터를 끌어온다
    if d[x] != 0:
        print(x) #f(3), f(4)는 메모이제이션에서 불러옴
        return d[x]
    
    #메모이제이션 되지 않았다면 점화식에 따라서 결과를 반환한다.
    d[x] = fibo_topdown(x-1) + fibo_topdown(x-2)
    return d[x]

print("#동적 프로그래밍으로 작성한 (하향식) 피보나치 배열")
print(fibo_topdown(6))
print(d)

#bottom-up (반복문 사용)
print("#동적 프로그래밍으로 작성한 (상향식) 피보나치 배열")

d = [0] * 100
#첫번째 피보나치 수와 두 번째 피보나치수는 1
d[1] = 1
d[2] = 1
n = 6

for i in range(3, n+1):
    print("F(", i, ") 호출됨")
    d[i] = d[i-1] + d[i-2] #작은 수부터 해결해나가는 방식
print(d[n])


#1로 만들기
#정수x가 주어졌을 때, 5로 나누거나 3으로 나누거나 2로 나누거나 1을 빼서 1을 만들려고 하는데, 연산을 사용하는
#회수의 최솟값을 출력해라
#왜 다이나믹으로 풀수 있는가? - 큰 문제를 작은 문제로 풀 수 있는가? / 중복되는가?
#큰 -> 작으로 중복적으로 자를 수 있는가? 
#==

#재귀 point: 어떤 같은 수의 연산의 최솟값은 항상 같다. 이것을 memorization한다면 데이터 공간 효율적 사용이 가능

#횟수의 최솟값은 어떻게 구할 것인가? --> 1. 탑다운: 가능한 경우를 모두 계산한 후 최솟값 min으로 도출한다.
                                        #2. 바텁업: 1에서 해당하는 수까지 갈 수 있는 최소 횟수를 구한다.
"""
x = int(input())
cnt = 0
dp = [0]*(x+1)
for x in range(2, x+1):
    cnt += 1
    min_box = []
    
    if x % 5 == 0:
        y = x//5
        min_box.append(cnt)
        min_box.append(dp[y]+1)
    if x % 3 == 0:
        y = x//3
        min_box.append(cnt)
        min_box.append(dp[y]+1)
    if x %2 == 0:
        y = x//2
        min_box.append(cnt)
        min_box.append(dp[y]+1)
    if True:
        y = x - 1
        min_box.append(cnt)
        min_box.append(dp[y]+1)
        
    dp[x] = min(min_box)
print(dp[x])
"""
"""
x = int(input())
matrix = [0] * 30001
cnt = 0
def making_one(x, cnt):
    while x != 1:
        if x % 5 == 0:
            x /= 5
            cnt += 1
            return making_one(x, cnt)
        if x % 3 == 0:
            x /= 3
            cnt += 1
            return making_one(x, cnt)
        if x % 2 == 0:
            x /= 2
            cnt += 1
            return making_one(x, cnt)
        if True:
            x = x - 1
            cnt += 1
            return making_one(x, cnt)
    return cnt
                                        
a = making_one(x, cnt)
print(a)                    
"""                
"""실패 -> 이렇게 작성하게 되면 작성된 것을 저장할 공간이 없고, 최소의 cnt를 도출해낼 수 없다.
그렇다면? 저장할 공간을 만들어놓고 갖다 쓰게 한다 / 이전에 도출된 결과에 +1을 한 결과가 해당 결과의 cnt결과이다. 
-> 이 작은 문제들이 해결되어 모이면 큰 문제를 해결할 수 있게 된다.
x = int(input())
cnt = 0

while x != 1:
    if x % 5 == 0:
        x = x//5
        print("5")
    elif x % 3 == 0:
        x = x//3
        print("3")
    elif x %2 == 0:
        x = x//2
        print("2")
    else:
        x -= 1
        print("-1")
    cnt += 1
    
print(cnt)
"""
#상향식 풀이 for문 반복문 사용
"""
x = int(input()) #x가 어떻게 줄어드는 게 중요한 게 아니라 count가 중요하다

d = [0] * 30  #d배열의 인덱스 = 수(x), 해당 인덱스에 들어가는 값 = 횟수

for i in range(2, x+1): #왜2부터 시작하나? 1은 cnt가 0이라서, 
    
    d[i] = d[i-1] +1 #일단 1빼는 경우를 가정하여 횟수1 추가
    if i % 2 == 0:
        #아까 업데이트 했던 d[i]와 다이나믹으로 해결한 d[i//2]를 비교하여 작은 것으로 업데이트
        d[i] = min(d[i], d[i//2]+1) 
        print(d)

    if i % 3 == 0:
        d[i] = min(d[i], d[i//3]+1)
        print(d)
        
    if i%5 == 0:
        d[i] = min(d[i], d[i//5]+1)
        print(d)
        
print(d[x])
"""
#개미전사
#큰 것은 작은 것으로 쪼개서 계산할 수 있다. (4개가 있는 array의 max를 계산하려면 맨 처음부터 하나씩 max를 계산해야 한다)
#dp_table에서 이 전에 계산했던 것을 불러와서 비교해야 하는 것이 반복해서 실행되어야 한다.

"""
n = int(input())
array = list(map(int, input().split()))

dp_table = [0] * n #dp_table은 i창고까지 가져갈 수 있는 가장 최대의 식량의 수를 표현하는 테이블이다.

dp_table[0] = array[0] #array의 첫 번째 요소를 dp_table의 첫 번째에 넣음
dp_table[1] = max(array[0], array[1]) #dp_table의 두 번째 요소는 그 전에꺼와 array[1], 둘 중에 하나를 택해야 함.(연속으로 된 것 둘다 못취함)
for i in range(2, n): #2부터 n-1까지 range
    #바로 앞에 있는 것 / 전전에 있는 것과 현재 array의 합, 둘 중에 큰 것을 택해서 dp_table에 넣는다(나란히 있는 것은 합하는 것이 불가)
    dp_table[i] = max(dp_table[i-1], dp_table[i-2] + array[i]) 
    
print(dp_table[n-1])
"""
#바닥공사
#상향식. 
#큰 문제는 이전의 결과값에서 도출이 가능하다. 
#작은 문제에서 구한 답은 큰 문제에서 반복적으로 사용된다.
"""
n = int(input())

d = [0] * 1001
d[1] = 1
d[2] = 3
for i in range(3, n+1):
    d[i] = (d[i-1] + 2*[i-2]) % 7967964
print(d[n])
"""
#효율적인 화폐 구성
#1로 만들기와 비슷하게? -> but if문을 작성할수가 없음..
#큰 문제는 작은 문제로 쪼개서 해결이 가능하다.(15원을 만들어야 한다면 2원을 만들 때의 최소값이 필요하다)
#반복적인 업무가 필요하다. 각각의 돈을 만족하기 위한 최소의 화폐개수를 계산해야 한다.

#내가 짠 코드 --> 8, 10, 13의 경우 정답이 아니게 나온다.
"""
n, m = map(int, input().split())
money = []
for _ in range(n):
    money.append(int(input()))
    
d = [0] * (m+1)

for mon in money: #화폐 단위를 기준으로
    for i in range(mon, m+1, mon):
        d[i] = d[i-mon] + 1 #한 화폐단위의 배수들은 이전 배수에 필요한 동전의 개수에 +1
        
for i in range(2, len(d)):
    if d[i] == 0: #0인 것들을 처리
        print(i)
        comp = []
        for mon in money:
            comp.append(d[i-mon] + 1)
        d[i] = min(comp)
        print(comp)

        
        
print(d)
res = d[m]

if res == 0:
    print(-1)
else:
    print(res)
"""


"""
#정답코드
n, m = map(int, input().split())
array = []
for _ in range(n):
    array.append(int(input()))
d = [10001] * (m+1)

d[0] = 0
for i in range(n):
    for j in range(array[i], m+1):
        if d[j - array[i]] != 10001:
            d[j] = min(d[j], d[j-array[i]] + 1)
print(d[:30])
if d[m] == 10001:
    print(-1)
else:
    print(d[m])

###################################################
n, m = map(int, input().split())
# list_n은 화폐 종류를 저장하는 리스트
list_n = []
# 화폐 종류 입력받기
for i in range(n):
    list_n.append(int(input()))

# [10001]은 무한대(할수 없는 값)라고 생각하면 된다
d = [10001] * (m+1)
# d[x]에 저장되는 값은 x원을 만들기 위한 최소한의 화폐 갯수이다.
d[0] = 0

# 화폐 종류를 하나 정하고
for i in range(n):
    # 하나씩 확인하며 d의 값을 확인하고 저장
    for j in range(list_n[i], m+1):
        # (i-k)원을 만드는 방법이 존재하는 경우
        if d[j - list_n[i]] != 10001:
            d[j] = min(d[j],d[j - list_n[i]] + 1)
print(d)
if d[m] == 10001:
    print('-1')
else:
    print(d[m])
"""

#기출문제 35. 못생긴 수
#못생긴 수? 2,3,5만을 소인수로 가진 수. 1은 못생긴 수라 가정한다.
#n번째에 존재하는 못생긴 수를 찾아라.
"""
#실패: 2,3,5를 제외한 숫자들을 소인수로 가질 때가 포함됨.
n = int(input())
cnt = 1
num = 2
d = [1]
while cnt != n:
    if num % 2 == 0 and num %3 == 0 and num%5 == 0 :
        d.append(num)
        cnt += 1
    elif num % 2 == 0 and num % 3 == 0:
        d.append(num)
        cnt += 1
    elif num % 2 == 0 and num % 5 == 0:
        d.append(num)
        cnt += 1
    elif num % 3 == 0 and num % 5 == 0:
        d.append(num)
        cnt += 1
    elif num %2 == 0:
        d.append(num)
        cnt += 1
    elif num %3 == 0:
        d.append(num)
        cnt += 1
    elif num %5 == 0:
        d.append(num)
        cnt += 1

    a = num / 2
    if a % 2 != 0 or a %3 != 0 or a%5 != 0:
        pass
    a = num / 3
    if a % 2 != 0 or a %3 != 0 or a%5 != 0:
        pass
    a = num / 5
    if a % 2 != 0 or a %3 != 0 or a%5 != 0:
        pass
    d.append(num)
    num += 1
    print(d)
    if len(d) == n:
        print(num)
        break
"""


#소인수분해하는 코드
"""
target = int(input())
i = 2
li = [1]
while  i <= target:
    if target % i == 0:
        li.append(i)
        i += 1
    else:
        i += 1
print(li)
"""
"""
def soinsu(x):
    target = x
    i = 2
    li = {1}
    while  i <= target:
        if target % i == 0:
            li.add(i)
            i += 1
        else:
            i += 1
    return li


n = int(input())
cnt = 1
num = 2

b = {1, 2, 3, 5}
while cnt <= n:
    a = soinsu(num)
    print(a)
    if len(a-b) != 0:
        print("!!!")
        continue
    else:
        cnt += 1
        num += 1
        if cnt == n:
            print(num-1)
            break
"""
#답안
n = int(input())
ugly = [0] * n
ugly[0] = 1

i2 = i3 = i5 = 0
next2, next3, next5 = 2, 3, 5

#1부터 n까지의 못생긴 수를 찾기
for l in range(1, n):
    ugly[1] = min(next2, next3, next5)
    if ugly[l] == next2:
        i2 += 1
        next2 = ugly[i2] * 2
        
    if ugly[l] == next3:
        i3 += 1
        next3 = ugly[i3] * 3
    
    if ugly[l] == next5:
        i5 += 1
        next5 = ugly[i5] * 5

print(ugly[n-1])
#생각해야 할 변수가 너무 많아서 어려움..

#36. 편집거리 -- 너무 어렵다
"""
2차원 dp테이블 사용 
1. 두 문자열이 서로 같다면, 왼쪽 위에 해당하는 수(이전 문자까지의 최소 편집거리)
2. 두 문자가 다른 경우, 
"""
def edit_dist(str1, str2):
    n = len(str1)
    m = len(str2)
    
    #다이나믹 프로그래밍을 위한 2차원 dp테이블 초기화
    dp = [[0] * (m+1) for _ in range(n+1)]
    
    #dp 테이블 초기 설정
    for i in range(1, n+1):
        dp[i][0] = i
    for j in range(1, m+1):
        dp[0][j] = j
    
    #최소 편집거리 계산
    for i in range(1, n+1):
        for j in range(1, m+1):
            #문자가 같다면, 왼쪽 위에 해당하는 수를 그대로 대입
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            #문자가 다르다면, 3가지 경우 중에서 최솟값 찾기
            else:
                dp[j][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
    return dp[n][m]


str1 = input()
str2 = input()

print(edit_dist(str1, str2))

 
        
        
        
