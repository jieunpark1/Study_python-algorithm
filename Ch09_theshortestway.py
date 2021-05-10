# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 22:16:02 2021

@author: jieunpark
"""
##다익스트라와 플로이드 워셜 알고리즘 코드만 좀 외워놓으면 조금만 변형해서 사용이 가능하다 & 무슨 알고리즘써야하는지만 알기

#다익스트라 알고리즘(간단한 방법)
#방문하지 않은 노드 중에서 최단 거리가 가장 짧은
#노드를 선택하기 위해, 매 단계마다 
#1차원 리스트(최단거리 테이블)의 모든 원소를 확인(순차탐색)한다.


#import sys
#input = sys.stdin.readline #입력되는 데이터의 수가 많다는 가정

inf = int(1e9) #초기상태에서는 다른노드로 가는 최단거리를 '무한'으로 초기화(가장 큰 수 가정)

#노드의 개수(n), 간선의 개수(m) 받기
n, m = map(int, input().split())

#시작 노드 번호
start = int(input())

#노드 정보(다른 노드까지 가는{( 데 필요한 비용)담는 리스트
#(n+1)개의 인덱스를 만들 시, 노드 번호를 인덱스로 사용하여 바로 리스트에 접근이 가능
#인덱스번호(출발노드): (도착노드, 가는비용)
graph = [[] for i in range(n+1)]

#방문 유무
visited = [False] * (n+1)

#최단 거리 테이블 초기화
distance = [inf] * (n+1)

#간선 정보 입력받기
for _ in range(m):
    #a번 노드에서 b번 노드로 가는 비용이 c
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    

#방문하지 않은 노드 중에서, 가장 최단거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = inf
    index = 0 #가장 거리가 짧은 노드(인덱스)
    for i in range(1, n+1):
        #i노드를 방문하지 않았고, i노드의 최단거리(비용)이 inf보다 작을 때
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i #i는 for문의 변수이니 index에 할당하여 반환시킨다
    return index

#다익스트라(본함수) 정의
def dijkstra(start):
    distance[start] = 0 #자신 ~ 자신: 0경우
    visited[start] = True #자신은 방문처리
    
    #graph: 인덱스번호(출발노드) : (도착노드, 비용)
    #그래프 정보 등록
    for j in graph[start]:
        #j는 (도착노드, 비용)
        #j[0] = 도착노드
        #j[1] = 거리(비용)
        #distance: 해당하는 노드의 최단거리 테이블
        #input으로 받은 b, c 를 distance 리스트에 넣음
        distance[j[0]] = j[1]
    
    #시작 노드를 제외한 전체 n-1 개의 노드에 대해 반복
    for i in range(n-1):
        #현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문처리
        #앞에서 정의했던 "get_smallest_node"함수로 해당하는 인덱스를 반환
        now = get_smallest_node()
        visited[now] = True #방문표시
        
        #현재 노드와 연결된 다른 노드로 가는 최소 거리를 계산
        for j in graph[now]:
            cost = distance[now] + j[1]
            #현재 노드를 거쳐 다른 노드로 이동하는 거리가 더 짧은 경우 distance 그래프를 update
            if cost < distance[j[0]]:
                distance[j[0]] = cost
                
#다익스트라 알고리즘 수행
dijkstra(start)

#모든 노드로 가기 위한 최단 거리를 출력한다
for i in range(1, n+1):
    #도달할 수 없는 경우, 무한 이라고 출력한다
    if distance[i] == inf:
        print("INFINITY")
    #도달할 수 있는 경우 거리를 출력한다
    else:
        print(distance[i])
        
print("#################################")
#개선된 다익스트라 구조

#힙 라이브러리 사용 예제부터 보기
import heapq

#오름차순 힙 정렬
#최소 힙(작은 것 부터 빼낸다 )
def heapsort(iterable):
    h = []
    result = []
    
    #모든 원소를 차례로 힙에 삽입한다
    for value in iterable:
        heapq.heappush(h, value)
    
    #힙에 삽입된 모든 원소를 차례대로 꺼내서 담는다
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result = heapsort([1,3,5,6,8,2,4,7,9,0])
print(result)


#최대 힙(큰 것 부터 빼낸다 )-- 최소 힙에서 
#부호를 바꾸어서 붙임, 최대힙이 따로 라이브러리가 x
def heapsort(iterable):
    h = []
    result = []
    
    #모든 원소를 차례로 힙에 삽입한다
    for value in iterable:
        heapq.heappush(h, -value)
    
    #힙에 삽입된 모든 원소를 차례대로 꺼내서 담는다
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

result = heapsort([1,3,5,6,8,2,4,7,9,0])
print(result)


#개선된 다익스트라 알고리즘
import heapq
#import sys
#input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)
#visited 는 x
#get_smallest_ 필요x

#그래프 정보 저장(비용, 도착)
for _ in range(m):
    a, b, c= map(int, input().split())
    graph[a].append((b,c))

def dijkstra_simple(start):
    #우선순위 q
    q = []
    #큐에 (거리, 도착노드) 저장
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q: #q가 True일 동안
        #heap에서 가장 먼저 나오는(즉, 최소거리인)
        #거리, 현재꺼낸 노드
        dist, now = heapq.heappop(q)
        
        #현재 노드가 이미 처리된 적이 있다면 무시
        #visited사용x
        #거리값을 비교해서 현재의 거리가 더 길면 무시
        if distance[now] < dist:
            continue
        
        #현재 노드와 연결된 인접한 노드를 확인
        for i in graph[now]:
            #i[1]: 인접노드의 거리
            #cost= 현재까지의 노드 + 현재~인접노드까지의 거리
            cost = dist + i[1]
            #distance[i[0]]: distance 리스트에 저장된 값
            #그것보다 cost가 작으면 (=최소거리가 도출되면)
            if cost < distance[i[0]]:
                #distance리스트의 값을 갱신한다
                distance[i[0]] = cost
                #q에 cost를 기준으로 push한다.
                heapq.heappush(q, (cost, i[0]))
                
dijkstra_simple(start)

for i in range(1, n+1):
    
    #도달할 수 없는 경우, 무한 출력
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])


#플로이드 워셜 알고리즘
#모든 노드에서 다른 모든 노드까지의 최단경로
#단계별로 거쳐가는 노드를 기준으로 알고리즘을 수행
#매 단계마다 방문하지 않은 노드를 탐색하지 않아도 된다
#2차원테이블에 최단 거리 정보를 저장
#점화식에 따라 갱신 -> 다이나믹 프로그래밍 유형에 속함

#각 단계마다 특정 노드k를 거쳐 가는 경우를 확인한다
#a~b로 가는 최단거리보다 a에서 k를 거쳐 b로 가는 거리가 더 짧은지 검사한다
#D ab = min (D ab, D ak+ D kb)
#k는 해당 그래프의 모든 node, 자신~자신 : 0, a와 b는 k를 뺀 node

#플로이드 워셜 알고리즘 소스코드
INF = int(1e9)

n = int(input()) #노드 개수
m = int(input()) #간선 개수
#최소 거리를 저장할 2차원 리스트, graph리스트를 만듦
graph = [[INF] * (n+1) for _ in range(n+1)] #노드개수 * 노드개수

#행=열 동일한 경우 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a== b:
            graph[a][b] = 0

#간선 정보 입력받은 것 넣기
for _ in range(m):
    #A~B 가는 비용은 C
    a, b, c = map(int, input().split())
    graph[a][b] = c
    
#점화식에 따라 플로이드 워셜 알고리즘 수행
#a,b돌릴때 k는 안빼도 되는지?!
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


#결과출력
for a in range(1,n+1):
    for b in range(1,n+1):
        
        if graph[a][b] == INF:
            print("INFINITY", end = " ")
        #도달할 수 있는 경우 거리를 출력한다
        else:
            print(graph[a][b], end = " ")
    print()
            
    
#실전문제. 미래도시
#다익스트라: 한 지점에서 다른 지점까지의 최소거리
#플루이드워셜: 모든 지점에서 모든 지점까지의 최소거리
#무슨 모델을 써야할지 모르겠다!!!
#이 문제는 전형적인 플루이드 워셜 알고리즘이다. n의 범위가 한정적이어서 플로이드로 써도 빠르게 풀 수있음.
#핵심아이디어: 1번 노드에서 k를 거쳐 x로 가는 최단거리는 1~k + k~x라는 점이다
#그림 그리는 것도 좋은 방법.


n, m = map(int, input().split())
INF = int(1e9)
graph = [[INF] * (n+1) for _ in range(n+1)]

for a in range(1, 1+n):
    for b in range(1, 1+n):
        if a==b:
            graph[a][b] == 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
    
    
X , K = map(int, input().split())

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


#내가 알고 싶은 값(최단거리 graph다 작성해놓고, 1~K~X(1~K + K~X) 구하기)
distance =  graph[1][K] + graph[K][X]

if distance >= INF: #not ==
    print(-1)
else:
    print(distance)


#실전문제. 전보
#다익스트라: 한 지점에서 다른 지점까지의 최소거리
#플루이드워셜: 모든 지점에서 모든 지점까지의 최소거리

#플루이드 워셜로 쓰는 게 나을거같다. 왜냐하면 한 지점에서 여러 지점까지를 알아야 하기 때문에
#--> 답지는 다익스트라를 쓰라고 한다.. n과 m의 범위가 충분히 크기 때문에 플로이드로 하면 너무 계산량이 많아질것도 같긴하다
#그래서 한 도시에서 다른도시까지의 최단 거리로 치환할 수 있는 문제!
#시작도시는 하나로 정해져있고, 여기에서 필요한 도착도시만 distance의 값에서 추출하면 될듯!
#1 2 3 4 5..
#0 1 3 4 5    -> 갈 수 있는 도시가 4,5만이라고 하면 distance[4]+distance[5]하면 된다

#개선된 다익스트라 알고리즘 사용

import heapq
#import sys
#input = sys.stdin.readline
N, M, C = map(int, input().split())
INF = int(1e9)
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)
#visited 는 x
#get_smallest_ 필요x

#그래프 정보 저장(도착, 비용)
for _ in range(m):
    a, b, c= map(int, input().split())
    #b=도착노드
    #c=비용
    graph[a].append((b,c))

def dijkstra_simple(C):
    q = []
    
    #큐에 (거리, 도착노드) 저장
    heapq.heappush(q, (0, C))
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        
        #현재 노드가 이미 처리된 적이 있다면 무시
        #visited사용x
        #거리값을 비교해서 현재의 거리가 더 길면 무시
        if distance[now] < dist:
            continue
        
        #현재 노드와 연결된 인접한 노드를 확인
        for i in graph[now]:
            #graph:(도착, 비용)
            #i[0]: 도착노드
            #i[1]: 비용
            #cost= 현재까지의 노드 + 현재~인접노드까지의 거리
            cost = dist + i[1]
            #distance[i[0]]: distance 리스트에 저장된 값
            #그것보다 cost가 작으면 (=최소거리가 도출되면)
            if cost < distance[i[0]]:
                #distance리스트의 값을 갱신한다
                distance[i[0]] = cost
                #q에 cost를 기준으로 push한다.
                heapq.heappush(q, (cost, i[0]))
                
dijkstra_simple(C)


#count = 도달할 수 있는 노드의 개수
count = 0
#max_distance = 도달할 수 있는 노드 중 가장 멀리 있는 노드와의 최단거리
max_distance = 0


for d in distance:
    #도달할 수 있는 노드인 경우만
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)

#시작노드는 제외해야 하므로 count-1을 출력
print(count-1, max_distance)

#기출문제 37. 플로이드
n = int(input())
m = int(input())

INF = int(1e9)
graph = [[INF]*(n+1) for _ in range(n+1)]


for _ in range(1, m+1):
    a, b, c = map(int, input().split())
    if graph[a][b] != INF:
        graph[a][b] = min(graph[a][b], c)
    else:
        graph[a][b] = c

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

print(graph)

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print("0")
        else:
            print(graph[a][b], end = " ")
    print()
    
#기출문제 39. 화성탐사
#2차원 공간, 가장 왼쪽위에서 가장 오른쪽 아래로 이동하는 최소 비용. 
#상하좌우인접으로 1칸씩 이동이 가능하다
    
#node의 개수는 n^2이기 때문에 n>=125이라면 전체 노드의 개수는 10,000을 넘을 수 있으므로, 플로이드를 사용하기 보다는 다익스트라를 사용
#2차원에서의 다익스트라는??


import heapq
#import sys
#input = sys.stdin.readline
INF = int(1e9)

def func(N):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    #graph: 각 노드에 연결된 노드 정보
    graph = []
    for i in range(N):
        graph.append(list(map(int, input().split())))
    
    #distance: 
    distance = [[INF] * N for _ in range(N)]
    
    #시작노드 ~ 시작노드 : 최단거리 = 0
    x, y = 0, 0
    
    #큐에 저장되는 순서 (거리, x시작, y도착)
    q = [(graph[x][y], x, y)]
    print(q)
    
    distance[x][y] = graph[x][y]
    print(distance)
    
    while q:
        dist, x, y = heapq.heappop(q)
        if distance[x][y] < dist:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx <0 or nx>=N or ny<0 or ny>=N:
                continue
            
            cost = dist + graph[nx][ny]
            
            if cost<distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))
    return distance[N-1][N-1]
#test case T
T = int(input())
for _ in range(T):
    N = int(input())
    res = func(N)
    print(res)
    
    
    
