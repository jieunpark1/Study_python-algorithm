# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 12:54:35 2021

@author: 박지은
"""
#미소언니 괄호 코드 작동 잘 됨
#민화언니 괄호 코드 오류(런타임오류 Attribute)
#dfs/bfs 1 Queue class에서 push할 때
"""
    def push(self, data):
        return self._queue.insert(0, data)
#pull을 pop()함수를 하려면, 먼저 들어온 데이터를 뒤로 밀어주어야 한다
#그래서 새로 들어오는 데이터들을 리스트의 0자리에 붙여줘야 함 
#pop(0)일 경우에는 리스트의 0자리를 pop하므로 미소언니가 그 전에 적은대로 하면 됨!
"""
#요세푸스 문제 s-> group으로 변수이름 변경
#두 번째 요세푸스 답안 (%=사용) 순서가 안맞게 나왔는데 idx += n을 indx +=k로 바꾸어주면 된다.
"""
n,k = map(int,input().split())
group = [i for i in range(1,n+1)]
#print(group)
answer = []
idx = -1
for i in range(n):
    idx += n
    if idx >= len(group) :
        idx %= len(group)
    answer.append(str(group.pop(idx)))
    idx -=1

#print("<%s>" %(", ".join(answer)))
print("<",", ".join(answer),">",sep='')
"""



"""
#인접행렬 방식
inf = 999999

#2차원리 스트를 이용한 인접 행렬 표현
graph = [[0, 7, 5], [7, 0, inf], [5, inf, 0]]

print(graph)


#dfs (depth-first search): 최대한 깊숙이 들어가서 노드를 방문
#인접 노드에서 숫자가 작은 노드를 선택하고 push, 이것을 반복. 방문 안한 노드가 없다 = 인접한 노드를 모두 방문했다(가장 깊숙이 들어갔다) 그러면 pop.
#pop을 하면서 해당하는 노드의 인접노드를 체크한다. 방문 하지 않은 곳이 있다면 push한다.
#결국 넣고 -> 검사 -> 빼/넣 -> 검사 (가장 마지막에 들어온 것을 검사


#실제로 구현할 때는 스택을 쓰지 않아도 되고, 재귀함수로 구현하였을 때 간편하게 구현할 수 있다.
def dfs(graph, v, visited):
    #현재 노드를 방문처리
    visited[v] = True
    print(v, end = " ")
    print("visited[v]", visited[v])
    
    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]: #첫번째 노드안의 요소들 탐색
        if not visited[i]: #visited는 graph와 인덱스번호가 동일. #요소들 중에 visited가 없으면 다시 함수를 돌려서 탐색한다.
            #print(visited)
            dfs(graph, i, visited)
            
#각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [[], #인덱스 1부터 시작하도록 만들기 위해서 첫번째 0 인덱스는 만들어놓고 비워둠 
         [2, 3, 8], #1 
         [1, 7],  #2
         [1, 4, 5], #3
         [3, 5], #4
         [3, 4], #5
         [7], #6
         [2, 6, 8], #7 
         [1, 7] #8
         ] #6

#각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

#정의된 DFS 함수 호출
dfs(graph, 1, visited)


#bfs (breadth-first search): 횡단으로 모두 탐색한 후 아래로 내려감. 너비 우선 탐색
#인접노드를 모두 큐에 넣는다. 숫자가 작은 순서대로 인접한 노드 중 방문하지 않은 노드를 push한다(맨 뒤에 append)
#pop을 하고(맨 처음 들어온 노드를 pop) 거기에 해당되는 인접노드를 삽입한다.(삽입된 것은 맨 마지막에 들어감)
#먼저 들어온 것이 먼저 나가게 되어, 가까운 노드부터 탐색을 하게 된다.
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    
    #방문처리
    visited[start] = True
    
    #큐에 뭔가 있을 때 반복 = 큐가 빌 때까지 반복
    while queue:
        #큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end = " " )
        
        #v의 인접노드 중 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
visited = [False] * 9

bfs(graph, 1, visited)



#bfs/dfs 필요한 것
#2차원 형태의 graph(노드 번호 작은 순대로), 방문했는지 여부를 알 수 있는 리스트(노드 번호 작은 순서대로)
#dfs/bfs 함수 -> 매개변수: 시작노드, graph, visited
#           -> 기능: 노드를 방문처리 하고, 인접노드를 돌면서 방문하지 않았다면 노드에 추가하고 visit을 True로 만들어주는 기능 

"""
#실전문제1 음료수 얼려먹기
"""
#dfs
#0이 모여 있는 곳들을 찾아내서 개수를 센다
n, m = map(int, input().split())

#2차원 리스트로 graph 정보 받기
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))
    
#dfs 특정 노드 방문 후 연결된 모든 노드들 방문
def dfs_1(x,y):
    #주어진 범위를 벗어나는 경우에는 종료
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    
    #현재 노드 방문 안했다
    if graph[x][y] == 0:
        graph[x][y] = 1 #방문처리
        
        #상 하 좌 우 위치도 모두 재귀적으로 호출
        dfs_1(x-1, y) #상
        dfs_1(x+1, y) #하
        dfs_1(x, y-1) #좌
        dfs_1(x, y+1) #우
        return True
    
    #(else)현재 노드를 방문했다면(1이라면)
    return False

#모든 노드에 대해 음료수 채우기
result = 0
for i in range(n):
    for j in range(m): #행을 기준으로 열을 올라가면서 dfs를 수행한다
        #현재 위치에서 dfs 수행
        if dfs_1(i, j) == True:
            result += 1
            
print(result)
"""

#미로탈출
"""
from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
    info = list(map(int, input()))
    graph.append(info)
print(graph)

#이동방향 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

#bfs
def maze(x,y):
    #bfs 방식
    queue = deque()
    queue.append((x,y)) #튜플
    print(queue)
    while queue:
        x, y= queue.popleft()  #x,y 업데이트
        print("x :", x, "y: ", y)
        #현재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            #미로찾기 공간을 벗어난 경우 무시
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            
            if graph[nx][ny] == 0: #괴물인 
                continue
            
            #해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
                print("q: ", queue)
                print("Gra: ", graph)
                print("x :", x, "y: ", y)
                
    
    #가장 오른쪽 아래까지의 최단거리 반환
    return graph[n-1][m-1] #인덱스 번호 때문에 -1

print(maze(0,0))
"""
    
    



#기출문제15. 특정 거리의  도시 찾기
#dfs 이용 . (bfs인척하는 dfs)
#필요한 변수: graph, 방문했는지 여부 visited = [False] *노드개수
#n: 도시의 개수, m: 도로의 개수, 거리k, 출발도시 번호
#함수 -> dfs_2 : 그래프, 현재 위치, 방문여부

"""
n, m, k, x = map(int, input().split())
graph = []
for _ in range(n+1):
    graph.append([])
    
for i in range(1, m+1):
    road_sta, road_fin = map(int, input().split())
    graph[road_sta].append(road_fin)
print(graph)

#bfs로 풀기

from collections import deque
def city(x, k):
    queue = deque()
    queue.append(x)
    
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = visited[v] + 1 
                print(visited)     
                
    res = []
    if k in res == False:
        return -1
    else:
        for i in range(len(visited)):
            if visited[i] == k:
                res.append(str(i))
        res.sort()
        return " ".join(res)
    
visited = [0] * (n+1)
print(city(x, k))
"""
"""dfs
global cnt
cnt = 0
res = []
def dfs_2(graph, x, visited):
    visited[x] = True
    cnt = 0         #여기서 0을 초기화 하면 1 이후에는 더해질 수가 없다. 근데 global도 안먹는다.

    for i in graph[x]:
        if not visited[i]:
            dfs_2(graph, i, visited)
            cnt += 1
            print(i, cnt)
            if cnt == k:
                res.append(str(i))
                print("res", res)
                
visited = [False] * (n+1)

dfs_2(graph, x, visited)
if len(res) == 0:
    print(-1)
else:
    res.sort()
    print(" ".join(res))
"""


#예시 답안: bfs 를 수행하여 모든 도시까지의 최단거리를 계산한 뒤에 각 최단 거리를 하나씩 확인하여 그 값이 k인 경우에 해당 도시의 번호를 출력한다.
"""
from collections import deque
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    
#모든 도시에 대한 최단 거리 초기화
distance = [-1] * (n+1)
distance[x] = 0 #출발 도시까지의 거리는 0으로 설정

#bfs
q = deque([x])
while q:
    now = q.popleft()
    
    #현대 도시에서 이동할 수 있는 모든 도시를 확인
    for next_node in graph[now]:
        
        #아직 방문 안했다
        if distance[next_node] == -1:
            #최단 거리 갱신
            distance[next_node] = distance[now] + 1
            q.append(next_node)
            
#최단 거리가 k인 모든 도시의 번호를 오름차순으로 출력
check = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check = True
    
#만약 최단 거리가 k인 도시가 없다, -1출력
if check == False:
    print(-1)
"""

#기출문제 18. 괄호변환
#재귀함수 사용 (BFS)
#프로그래머스 괄호변환에서 76점. (시간초과)

def right_bracket(x):
    stack = []
    res = []
    for j in range(len(x)):
        if x[j] =="(":
            stack.append(x[j])
        elif x[j] ==")":
            if len(stack) != 0:
                stack.pop()
            else:
                res.append("NO")
                break
    if res: 
        return res
    elif len(stack) != 0:
        return "NO"
    else:
        return "YES"

def split_u_v(w):
    #2. w를 u,v로 분리한다.
    bracket_box = []
    for b in w:
        bracket_box.append(b)
        if bracket_box.count("(") == bracket_box.count(")"):
            u = "".join(bracket_box)
            break
    v = w[len(u):]
    return v, u 
    

def solution(w):
    #1. 입력이 빈 문자열일 경우, 빈 문자열을 반환한다.
    if w == "":
        return w
    #w자체가 올바른 괄호이면 w그대로 return
    if right_bracket(w) == "YES":
        return w
    
    #2. w를 u, v로 분리한다.
    v, u = split_u_v(w)
    

    #3. 수행한 결과를 u에 이어 붙인 후 반환한다.
    #print("u: ", u, "v: ", v)
    if right_bracket(u) == "YES":
        solution(v)
        return u+solution(v)

    #4. u가 올바르지 않다면,
    else:
        answer = "("
        answer += solution(v)
        answer += ")"
        
        u_li = []
        u_part = u[1:-1]
        for l in u_part:
            if l == ")":
                u_li.append("(")
            elif l == "(":
                u_li.append(")")
                
        answer += "".join(u_li)
        return answer
        
        
p = input()  
a = solution(p)
print(a)
