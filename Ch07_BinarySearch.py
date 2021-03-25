# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 11:46:42 2021

@author: 박지은
"""

#순차탐색
"""
def sequential_search(n, target, array):
    #각 원소를 하나씩 확인하며
    for i in range(n):
        if array[i] == target:
            return i+1

        
print("생성할 원소의 개수를 입력한 후 한 칸 띄고 찾을 문자열을 입력하세요")
#n은 array리스트의 원소의 개수
input_data = input().split()
n      = int(input_data[0])
target = input_data[1]

print("앞서 적은 원소 개수만큼 문자열을 입력하세요.")
array = input().split() #리스트 형식으로 원소가 들어감

#순차 탐색 수행 결과 출력
print(sequential_search(n, target, array))
# 5 dongbin
#hanul jonngu dongbin taeil sangwook
"""



#이진탐색; 재귀함수로 구현
#시작, 끝점, 중간점(찾고자 하는 데이터와 비교)
#정렬 필요
#단순히 정렬된 배열에서 특정한 데이터를 찾는 문제에서는 -> bisect 모듈을 사용. (사용방법 알아두기)
"""
def bi_search(array, target, start, end):
    if start>end: #탐색하려는 범위에 데이터가 존재하지 않는 경우
        return None
    mid = (start + end) // 2 #소수점을 버린 몫 구하기
    
    #찾은 경우 중간점 인덱스를 반환한다.(mid가 trget일 경우 탐색완료)
    if array[mid] == target:
        return mid
    elif array[mid] > target:  #mid보다 target이 작은 경우, 왼쪽구간을 탐색한다(end점을 mid의 인덱스 -1로 변경)
        return bi_search(array, target, start, mid-1)
    else: #mid보다 target이 큰 경우, 오른쪽 구간을 확인(start점을 mid+1로 변경)
        return bi_search(array, target, mid+1, end) 
    
#n(원소의 개수)과 target(찾고자 하는 문자열)을 입력받기
n, target = list(map(int, input().split()))
print(n)
print(target)
array = list(map(int, input().split()))

#이진탐색 수행 결과 출력
result = bi_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result+1)
"""

#; 반복문 구현
"""
def bi_search(array, target, start, end):
    while start <= end: #array에 원소가 존재하는 동안에 while문을 돌린다
        mid = (start + end) //2
        
        if array[mid] == target: #mid가 target일 경우 함수종료
            return mid
        
        elif array[mid] > target: #중간점의 값보다 찾고자 하는 값이 작은 경우  mid의 오른쪽을 버리고 mid의 왼쪽을 확인한다
            end = mid - 1
        
        else: #중간값보다 target이 큰 경우 왼쪽은 버리고 mid의 오른쪽 구간을 확인한다.
            start = mid + 1
    return None

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = bi_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다")
else:
    print(result + 1)
     
"""


#Bisect 모듈 사용하기

from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 5]
x = 4
print(bisect_left(a, 4)) #2 #bisect_right/left(배열이름, 찾고자 하는 값) -> 인덱스를 반환
print(bisect_right(a, 4)) #4
#둘을 빼면 4가 몇개 존재하는지 알 수 있다.


 


#실전문제 2. 부품찾기
"""
def stock(n_list, target, start, end):
    while start<=end: #n_list에 원소가 존재한다.
        mid = (start + end ) //2
        if n_list[mid] == target:
            return mid
        elif n_list[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None
        

n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))
    
n_list.sort() #이진정렬 하려면 '정렬'은 필수

for i in m_list:
    res = stock(n_list, i, 0, n-1)
    if res == None:
        print("no", end = " ")
    else:
        print("yes", end=" ")
"""
##추가풀이: 계수정렬. (n이 백만까지 갈 수 있으므로 중복되는 정수가 있을 것! ->정수의 범위가 한정되어 있고 데이터의 개수가 많을 때)
#1<m<100,000
#1<n<1,000,000
"""내가 푼 계수정렬
n = int(input())
n_list = list(map(int, input().split())) 
m = int(input())
m_list = list(map(int, input().split())) #array = 찾고자 하는 거


count = [0] * (max(m_list)+1)
print(count)
for i in n_list:
    count[i] += 1
    print(count)

for j in m_list:
    if count[j] == 0:
        print("no", end = " ")
    else:
        print("yes", end = " ")

"""
#계수정렬: 답안예시
"""
n = int(input()) #가게의 부품 개수
array = [0] * 1000001

#가게에 있는 전체 부품 번호를 받아서 기록
for i in input().split():
    array[int(i)] = 1

#m(손님이 확인 요청한 부품의 개수) 입력받기
m = int(input())
x = list(map(int, input().split()))

#손님이 확인 요청한 부품번호 하나씩 확인
for i in x:
    if array[i] ==1:
        print("yes", end = " ")
    else:
        print("no", end = " ")
"""

##집합 자료형을 이용해서 풀기
"""
n = int(input())
array = set(map(int, input().split())) #가게에 있는 전체 부품 번호를 받아서 set으로 기록
print(array)

m = int(input())
x = list(map(int, input().split())) #고객이 요청한 전체 부품 번호

#손님이 확인 요청한 부품 번호를 하나씩 확인
for i in x:
    if i in array:
        print("yes", end = " ")
    else:
        print("no", end = " ")
"""

#실전문제3. 떡볶이 떡 만들기
#떡n개에 대해서 떡을 절단기로 h길이 만큼 잘라서 남은 떡의 총 길이의 합이 적어도 m이 되기 위한 h의 최댓값을 구하라

"""나
def bi_search(ddeok, m, start, end):
    if start >end:
        return None
    h = (ddeok[start]+ddeok[end]) // 2 #값
    mid = (start + end) //2 #인덱스값
    print("mid:", mid, ", h: ", h)
    
    new_ddeok = 0
    res = []
    if ddeok[mid] < h:
        return bi_search(ddeok, m, mid+1, end)
    
    elif ddeok[mid] >= h:
        for new_h in range(h, end):
            for i in range(ddeok[mid], end):
                new_ddeok += (ddeok[i]-new_h)
            res.append([new_h, new_ddeok])
            print(res)
            new_ddeok = 0
    
        
            
    


n, m = map(int, input().split())
ddeok = list(map(int, input().split()))
ddeok.sort()
bi_search(ddeok, m, 0, n-1)
"""

#답안예시
# 자르고 남은 것들의 합이 6보다 작다 -> 끝점을 감소 / 자르고 남은 것들의 합이 6보다 크다 -> 끝점을 늘린다.
"""
n, m = map(int, input().split())
ddeok = list(map(int, input().split()))

#이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(ddeok)

#이진 탐색 수행(반복 , not재귀)
result = 0
while (start <= end):
    total = 0
    mid = (start + end ) //2
    
    for x in ddeok:
        #잘랐을 떄의 떡의 양 계산
        if x > mid:
            total += x - mid #해당 mid에서의 잘라져 나오는 떡의 합
    
    if total < m:  #이 total이 m보다 작을 때는, (떡의 양이 모자르다) end를 mid-1로 가져와서 while문으로 재탐색한다
        end = mid -1
    else:
        result = mid #total이 m보다 클 경우에는,(떡의 양이 남음) start를 mid+!로 가져와서 오른쪽 부분을 탐색
        start = mid + 1
print(result)
"""
            
#기출문제 27. 정렬된 배열에서 특정 수의 개수 구하기
#bisect으로 풀기 (O (logN))의 시간복잡도로 풀어야 함.
#이미 정렬된 수열의 원소 중에서 값이 x인 원소의 개수를 출력하라. 값이 x인 원소가 하나도 없다면 -1을 출력하라
"""
n, x = map(int, input().split())
a = list(map(int, input().split()))
res = bisect_right(a, x) - bisect_left(a, x)
if res == 0:
    print(-1)
else:
    print(res)
"""

#답안예시

#1. bisect사용
"""
def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index

count = count_by_range(array, x, x)
if count == 0:
    print(-1)
else:
    print(count)
"""

#2. 가장 첫 번째 위치를 찾는 이진 탐색 함수, 가장 마지막 위치를 찾는 이진함수, 이 2개를 각각 실행한 뒤 답을 도출. 
#이진탐색을 요구하는 고난이도 문제에서 자주 사용할 수 있는 테크닉
"""??"""
"""
def count_by_value(array, x):
    n = len(array) #데이터 개수
    
     #x가 처음 등장한 인덱스 계산
    a = first(array, x, 0, n-1)
    if a == None:
        return 0  #x가 존재하지 않는 경우 0을 반환
    #x가 마지막으로 등장한 인덱스 계산
    b = last(array, x, 0, n-1)
    return b-a+1


def first(array, target, start, end):
    if start>end:
        return None
    mid = (start + end) //2
    
    #해당 값을 가지는 원소 중에서 가장 왼쪽에 있는 경우에만 인덱스를 반환한다 -- 첫번째값을 찾아야 하므로 mid에서 최대한 왼쪽에꺼를 찾음
    if (mid == 0 or target > array[mid-1]) and array[mid] == target: 
        return mid
    
    #중간점의 값보다 찾고자 하는 값이 작거나 같은 경우 왼쪽 확인
    elif array[mid] >= target:
        return first(array, target, start, mid-1)
    #중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return first(array, target, mid+1, end)
    
    
    
def last(array, target, start, end):
    if start>end:
        return None
    mid = (start+end) //2
    
    if (mid == n-1 or target<array[mid+1]) and array[mid] == target:
        return mid
    # 중간점의 값 보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return last(array, target, start, mid-1)
    #중간점의 값보다 찾고자 하는 값이 크거나 같은 경우 오른쪽 확인
    else:
        return last(array, target, mid +1, end)    

n, x = map(int, input().split())
array = list(map(int, input().split()))

count = count_by_value(array, x)

if count == 0:
    print(-1)
else:
    print(count)
"""    
    

#기출문제 28. 고정점 찾기
#오름차순 정렬 되어 있음. 값이 인덱스와 동일한 원소를 찾기

from bisect import bisect_left, bisect_right

def fix_point(array, start, end):
    start = bisect_right(array, start) #start와 end값을 조정한다. 인덱스값은 0부터 시작이므로 값이 0인것부터 start범위를 잡고 
    end = bisect_left(array, end) -1  #인덱스값은 end값보다 큰 것은 나타날 수 없으므로 end범위도 조정한다.
    print("start: ", start, ", end: ", end)
    
    while start <= end: #start가 end보다 작거나 같을 때 while문을 돈다
        mid = (start + end) // 2
        print("start:", start, ", end = ", end, ", mid:", mid)
        if array[mid] == mid:
            return mid
        elif mid > array[mid]: #인덱스값(mid) 가 값보다 크면 start를 mid뒤로 움직인다.(오름차순 정렬이므로) 오른쪽을 확인
            start = mid + 1
        elif array[mid] > mid: #값이 인덱스보다 크면 end를 mid앞으로 움직인다 왼쪽부분을 확인 ex)index = 2 , 값=4 
            end = mid - 1
    return -1 #while문이 끝나도 아무것도 해당안된다면 -1을 반환한다.
        
        
n = int(input())
array = list(map(int, input().split()))

result = fix_point(array, 0, n-1)
print(result)

#답안예시
"""
def fix_point_2(array, start, end):
    if start > end:
        return None
    mid = (start + end ) // 2
    
    if array[mid] == mid:
        return mid
    elif array[mid] > mid: #중간점이 가리키는 위치의 값보다 중간점이 작은 경우 왼쪽을 확인한다
        return fix_point_2(array, start, mid-1)
    else: #중간점이 가리키는 인덱스보다 중간점이 큰 경우 오른쪽을 확인한다.
        return fix_point_2(array, mid+1, end)

n = int(input())
array = list(map(int, input().split()))

index = fix_point_2(array, 0, n-1)

if index == None:
    print(-1)
else:
    print(index)
"""  
    

