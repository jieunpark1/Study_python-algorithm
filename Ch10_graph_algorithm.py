# -*- coding: utf-8 -*-
"""
Created on Tue May 11 09:47:10 2021

@author: jieunpark
"""
"""    
#서로소 집합 - 트리구조, union/find 기능 2개
def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split()) #v=노드개수, e=간선개수
parent = [0] * (v+1)

#부모테이블을 먼저 자기자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

#union연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

#각 원소가 속한 집합 출력
print("각 원소가 속한 집합: ", end = "")
for i in range(1, v+1):
    print(find_parent(parent, i), end=" ")
print()

#부모테이블 내용 출력
print("부모테이블: ", end = "")
for i in parent:
    print(i, end=" ")    
    
    
    
#개선된 경로압축 기법
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split()) #v=노드개수, e=간선개수
parent = [0] * (v+1)

#부모테이블을 먼저 자기자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

#union연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

#각 원소가 속한 집합 출력
print("각 원소가 속한 집합: ", end = "")
for i in range(1, v+1):
    print(find_parent(parent, i), end=" ")
print()

#부모테이블 내용 출력
print("부모테이블: ", end = "")
for i in parent:
    print(i, end=" ")    
 
    
 
    
#크루스컬 알고리즘(최소 신장 트리 알고리즘)
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split()) #v=노드개수, e=간선개수
parent = [0] * (v+1)

#부모테이블을 먼저 자기자신으로 초기화
for i in range(1, v+1):
    parent[i] = i


#모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

#간선에 대한 정보 받아오기
for _ in range(e):
    a, b, cost = map(int, input().split())
    #비용 순으로 정렬하기 위해 튜플의 첫 번째 원소를 비용으로 설정한다.
    edges.append((cost, a, b))
edges.sort()

#간선을 하나씩 확인하며 
for edge in edges:
    cost, a, b = edge
    #사이클이 발생하지 않는 경우에만 집합에 포함(두 노드의 root node가 같지 않으면 union을 수행하여 같은 집합에 포함시켜라)
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
print(result)



#위상정렬
from collections import deque

v, e = map(int, input().split()) #v=노드 수, e=간선 수
indegree = [0]* (v+1) #진입차수
graph = [[] for i in range(v+1)] #인덱스가 노드 번호가 되며, 그것과 연결된 노드를 기록.

#그래프의 모든 간선 정보를 입력받는다
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b) #graph의 인덱스번호=간선번호, 여기에 연결된 b노드를 append
    #a->b인 경우, b의 진입차수는 +1
    indegree[b] += 1
    
def topology_sort():
    result = [] #큐에서 나가는 노드를 기록
    q = deque()
    
    #진입차수가 0인 노드를 큐에 삽입한다
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
    #큐가 빌 때까지 계속
    while q:
        now = q.popleft() #맨 먼저 들어있는 원소를 pull한다. pull하면 result에 append
        result.append(now)
        #해당 원소와 연결된 노드들의 진입차수에서 1빼기
        for i in graph[now]: #now 간선과 연결된 i들에 진입차수를 1뺀다.
            indegree[i] -= 1
            if indegree[i] == 0: #1뺀 후 만약 i의 진입차수가 0이라면 큐에 push한다.
                q.append(i)
                
    for i in result:
        print(i, end= " ")
        
topology_sort()
"""    

#실전문제 2. 팀결성
"""
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split()) #n=노드개수, m=간선개수
parent = [0] * (n+1)
check = []
#부모테이블을 먼저 자기자신으로 초기화
for i in range(1, n+1):
    parent[i] = i

#union연산을 각각 수행
for i in range(m):
    code, a, b = map(int, input().split())
    if code == 0:
        union_parent(parent, a, b)
    else:
        check.append((a, b))
        

for i in check:
    if parent[i[0]] == parent[i[1]]:
        print("YES")
    else:
        print("NO")

"""

#실전문제 3. 도시 분할 계획
#-조건: 집합을 2개 이상으로 만들어라 -> 가장 cost가 큰 간선(last)를 뺀다면 최소 신장트리가 2개의 부분 그래프로 나누어진다.
#조건2: 임의의 두 집 사이에 경로가 항상 존재하게 하면서 길을 더 없애라(최소 비용으로->최소신장알고리즘)
"""
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split()) #v=노드개수, e=간선개수
parent = [0] * (v+1)

#부모테이블을 먼저 자기자신으로 초기화
for i in range(1, v+1):
    parent[i] = i


#모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

#간선에 대한 정보 받아오기
for _ in range(e):
    a, b, cost = map(int, input().split())
    #비용 순으로 정렬하기 위해 튜플의 첫 번째 원소를 비용으로 설정한다.
    edges.append((cost, a, b))
    
#cost기준으로 sort
edges.sort()
last = 0 #최소 신장 트리에 포함되는 간선 중에서 가장 비용이 큰 간선을 제거한다.

#간선을 하나씩 확인하며 
for edge in edges:
    cost, a, b = edge
    #사이클이 발생하지 않는 경우에만 집합에 포함(두 노드의 root node가 같지 않으면 union을 수행하여 같은 집합에 포함시켜라)
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        last = cost
print(result - last)
"""

#실전문제 4. 커리큘럼
from collections import deque
import copy

n = int(input())#v=노드 수, 간선 수
indegree = [0] * (n+1) #진입차수
graph = [[] for i in range(n+1)] #인덱스가 노드 번호가 되며, 그것과 연결된 노드를 기록.
hour = [0] * (n+1) #인덱스가 강의번호에 해당되며, 그 강의의 시간을 값으로 기록


#그래프의 모든 간선 정보를 입력받는다
for i in range(1, n+1):
    temp = list(map(int, input().split()))[:-1]
    for j in range(len(temp)):
        if j == 0:
            hour[i] = temp[j]
        else:
            graph[temp[j]].append(i)  #graph의 인덱스번호=간선번호, 여기에 연결된 b노드를 append
            indegree[i] += 1
    #a->b인 경우, b의 진입차수는 +1
#print("graph:", graph)
#print("indegree:", indegree)
print("hour:", hour) 

def topology_sort():
    result = copy.deepcopy(hour) #처음 hour의 상태로 result에 박제하고, hour이 변하더라도 result에 영향X
    print("ini", result)
    q = deque()
    
    #진입차수가 0인 노드를 큐에 삽입한다
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
    #큐가 빌 때까지 계속
    
    while q:
        now = q.popleft() #맨 먼저 들어있는 원소를 pull한다. pull하면 result에 append
        
        #해당 원소와 연결된 노드들의 진입차수에서 1빼기
        for i in graph[now]: #now 간선과 연결된 i들에 진입차수를 1뺀다.
            result[i] = max(result[i], result[now] + hour[i]) #graph[2]=[1], result[1]+hour[2] vs result[2]
            print("333", result[i])
            indegree[i] -= 1
            if indegree[i] == 0: #1뺀 후 만약 i의 진입차수가 0이라면 큐에 push한다.
                q.append(i)
                
    for i in range(1, n+1):
        print("res",result[i])
        
topology_sort()

#해당하는 과목마다 최소시간 찾는거 어케하는지 어렵다
