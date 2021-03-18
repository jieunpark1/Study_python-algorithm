# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 09:57:29 2021

@author: 박지은
"""

#실전문제 2. 위에서 아래로
"""
box = []
for _ in range(int(input())):
    box.append(input())
box.sort(reverse=True)
print(" ".join(box))
"""

#실전문제 3. 성적인 낮은 순서로 학생 출력하기
"""#이름 순대로 정렬됨.. -> 다시 풀기
info = []
for _ in range(int(input())):
    a= list(input().split())
    info.append(a)
info.sort()

for inf in info:
    print(inf[0], end = " ")
"""

"""
민화언니
N=int(input())
name_list=[]
score_list=[]

#각각 리스트에 넣기
for i in range(N):
  name, score=input().split()
  name_list.append(name)
  score_list.append(int(score))
#score_list=list(map(int, score_list))  #숫자로 바꾸기

#선택정렬로 풀어보기
for i in range(len(score_list)):
  min_index=i
  for j in range(i+1, len(score_list)):
    if score_list[min_index] > score_list[j]:
        min_index=j
  score_list[i], score_list[min_index]=score_list[min_index], score_list[i]
  name_list[i], name_list[min_index]=name_list[min_index], name_list[i]

for i in name_list:
  print(i, end=' ')

"""

"""
예시답안
튜플 정렬 관련 https://leedakyeong.tistory.com/entry/python-%ED%8A%9C%ED%94%8C-%EC%A0%95%EB%A0%AC%ED%95%98%EA%B8%B0%EB%91%90-%EB%B2%88%EC%A7%B8-%EC%9B%90%EC%86%8C%EB%A1%9C-%EC%A0%95%EB%A0%AC%ED%95%98%EA%B8%B0-tuple-sorting-in-python
n = int(input())
array = []
for i in range(n):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1]))
    
#키(key)를 이용하여, 점수를 기준으로 정렬한다.
array = sorted(array, key=lambda student: student[1])

#수행 결과 확인
for student in array:
    print(student[0], end = " ")

"""
    
#실전문제 4. 두 배열의 원소 교체
"""
n: 배열 a,b의 원소의 개수 
배열 a의 젤 작은 게 b의 젤 큰것보다 작아야 교체가능
k: 최대로 교체할 수 있는 횟수
"""    

"""
n, k = map(int, input().split())


A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort(reverse=True)



for i in range(k):
    if A[i] < B[i]:
        A[i], B[i] = B[i], A[i]
      
print(sum(A))
"""

#실패율
"""
미소언니
def solution(n, stages):
    answer = []
    length = len(stages)
    for i in range(1, n+1):
        count = stages.count(i)
        # 스테이지에 도달한 유저가 없는 경우 
        if count == 0:
            fail = 0
        else:
            fail = count / length
        answer.append([i, fail])
        # 도달못한 인원 빼기
        length -= count
    # 실패율 내림차순
    sorting = sorted(answer, key=lambda t: t[1], reverse=True)
    answer = []
    for failure in sorting:
        answer.append(failure[0])
    return answer
"""


"""
def solution(N, stages):
    res = []
    for i in range(1, N+1):
        user = stages.count(i) #분자
        user_ch = 0 #분모
        for j in stages:
            if j >= i:
                user_ch += 1 #분모 = 도전한 사람의 수
        if user == 0: #분자가 0이면 실패율이 0
            fail = 0
        else:
            fail = user / user_ch
        res.append((i, fail))
    res = sorted(res, key = lambda x: -x[1]) #람다 내림차순
    answer = []
    for n in res:
        answer.append(n[0])
    return answer
    
    
N = 4
stages = [4, 4, 4, 4, 4]
a = solution(N, stages)
print(a)
"""


"""
다른사람 풀이
def solution(N, stages):
    result = {} #딕셔너리
    denominator = len(stages) #전체 참가자 수
    for stage in range(1, N+1):   
        if denominator != 0:
            count = stages.count(stage) #해당 스테이지에 참여한 사람의 수
            result[stage] = count / denominator #result 딕셔너리에 있는 stage key의 value =  참여한 사람 수 / 전체 참여자 수
            denominator -= count  #전체 참여자 수에서 count를 뺀다.ex) 1번 스테이지에서 끝 -> 2번 스테이지에서는 참여x
        else: #참가자가 0스테이지다. #deno에서 count를 계속 빼서 결국 0이 된다면..
            result[stage] = 0
    print("Res", result)
    
    #for i in result:
    #    print(result[i]) #0.125, 0.42.. , 0.5, 0.5
    
    return sorted(result, key=lambda x : result[x], reverse=True) #sort하면 딕셔너리의 key값만 나옴?!
#https://velog.io/@kylexid/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%97%90%EC%84%9C-%EB%94%95%EC%85%94%EB%84%88%EB%A6%AC-%EC%9E%90%EB%A3%8C-%EC%A0%95%EB%A0%AC%ED%95%98%EA%B8%B0
# ---> sorted, sorted lambda로 해주면 결과는 key의 리스트를 반환한다.
    
N = 4
stages = [2, 1, 2, 6, 2, 4, 3, 3]
a = solution(N, stages)
print(a)

---------------------------------------------------------------------------------
def solution(N, stages):
    fail = {}
    for i in range(1,N+1):
        try:
            fail_ = len([a for a in stages if a==i])/len([a for a in stages if a>=i])
        except:
            fail_ = 0
        fail[i]=fail_
    answer = sorted(fail, key=fail.get, reverse=True) #fail.get = 값에 따라 정렬하여 key를 불러오기
    print(fail)
    return answer

N = 4
stages = [2, 1, 2, 6, 2, 4, 3, 3]
a = solution(N, stages)
print(a)


#get() : https://m.blog.naver.com/PostView.nhn?blogId=sw4r&logNo=221546720733&proxyReferer=https:%2F%2Fwww.google.com%2F
#sorted key 매개변수에서 get: https://fenderist.tistory.com/256
"""

#카드 정렬하기 https://www.acmicpc.net/problem/1715
"""
가장 작은 카드부터 차례로 2개씩 더해 나간다.
#큐??
"""
num = []
sums = []

for i in range(int(input())):
    num.append(int(input()))
    if len(num) == 2:
        sums.append(sum(num))
        num.remove
    else:
        try:
            new_sums = sums[-1] + num[-1]
            sums.append(new_sums)
        except:
            continue
        
sum_total = sum(sums)
print(sum_total)


    

    