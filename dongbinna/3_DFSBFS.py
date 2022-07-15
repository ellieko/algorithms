'''

나동빈 이코테 2021 강의 몰아보기
https://www.youtube.com/watch?v=7C9RgOcvkvo&list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC&index=3

--- Depth First Search (깊이 우선 탐색) ---
그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘
스택 자료구조(혹은 재귀 함수)를 이용
1) 탐색 시작 노드를 스택에 삽입하고 방문 처리
2) 스택의 최상단 노드에 방문하지 않은 인접 노드가 하나라도 있으면
   그 노드를 스택에 넣고 방문 처리
   방문하지 않은 인접 노드가 없으면, 스택에서 최상단 노드를 꺼냄
3) 2번의 과정을 수행할 수 없을 때까지 반복

e.g. 방문 기준: 번호가 낮은 인접 노드부터
'''
# 각 노드가 연결된 정보를 표현 (주로 2차원 리스트로 그래프 표현)
graph = [
    [],
    [2,3,8],    # 1번 노드는 2번, 3번, 8번하고 연결되어 있음
    [1,7],      # ...
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
# 각 노드가 방문된 정보를 표현 (1차원 리스트)
# visited = [False]*9

def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end= ' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for node in graph[v]:
        if not visited[node]:
            dfs(graph, node, visited)


'''
--- Breadth First Search (너비 우선 탐색) ---
그래프에서 가까운 노드부터 우선적으로 탐색하는 알고리즘
큐 자료구조를 이용
1) 탐색 시작 노드를 큐에 삽입하고 방문 처리
2) 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서
   방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리
3) 2번의 과정을 수행할 수 없을 때까지 반복

e.g. 방문 기준: 번호가 낮은 인접 노드부터

각 단위 선의 비용이 모두 동일한 선에서 
최단거리 문제를 해결하는데에도 사용됨
'''
from collections import deque

def bfs(graph, start, visited):
    q = deque([start])
    visited[start] = True
    while q:
        v = q.popleft()
        print(v, end = ' ')
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True


'''
[예제 1. 음료수 얼려먹기]
N*M 크기의 얼음 틀, 구멍이 뚫려있는 부분은 0, 칸막이 존재하는 부분은 1
구멍이 뚫려있는 부분끼리 상, 하, 좌, 우로 붙어있는 경우 서로 연결되어 있는 것으로 간주
얼음 틀이 주어졌을 때 생성할 수 있는 총 아이스크림의 개수
e.g. 4 5
     00110
     00011
     11111
     00000
     -> 총 3 생성 가능
'''
# n: 세로 길이, m: 가로 길이

# 해결 아이디어 - 값이 1인 지점은 방문할 수 없는 지점!
# DFS - 특정 지점의 주변 상,하,좌,우 를 살펴본 뒤에
#       주변 지점에서 값이 0이면서 아직 방문하지 않은 지점이 있다면 방문
#       방문한 지점에서 다시 상,하,좌,우 살펴보며 방문 진행하면
#       연결된 모든 지점을 방문할 수 있음
#       모든 노드에 대하며 1-2번의 과정 반복하며 지점의 수 카운트
n, m = 4, 5
g = [[0,0,1,1,0],
     [0,0,0,1,1],
     [1,1,1,1,1],
     [0,0,0,0,0]]
visited = [[False]*m]*n

def icecream_dfs():
    result = 0
    for i in range(n):
        for j in range(m):
            if dfs_for_icecream(i, j) == True:
                result += 1
    return result

def dfs_for_icecream(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if g[x][y] == 0:
        g[x][y] = 1   # 방문 처리!!!!
        # 근접한 노드들도 방문 처리
        dfs_for_icecream(x+1, y)
        dfs_for_icecream(x, y+1)
        dfs_for_icecream(x+1, y+1)
        # print('Print a current graph')
        # for i in range(n):
        #    print(g[i])
        return True
    return False


'''
[예제 2. 미로 탈출]
N*M 크기의 직사각형 형태의 미로
동빈이의 위치는 (1,1) 출구는 (N,M), 한칸씩 이동
괴물이 있는 칸은 0, 없는 칸은 1, 반드시 탈출할 수 있음
탈출을 위해 움직여야하는 최소 칸의 개수? (시작, 마지막 칸 포함)
e.g. 5 6
     101010
     111111
     000001
     111111
     111111
     -> 10
'''
def escape_maze(arr, x, y):
    n, m = len(arr), len(arr[0])
    q = deque()
    q.append((x,y))
    while q:
        x, y = q.popleft()
        if x+1 < n and arr[x+1][y] == 1:
            arr[x+1][y] = arr[x][y] + 1
            q.append((x+1, y))
        if y+1 < m and arr[x][y+1] == 1:
            arr[x][y+1] = arr[x][y] + 1
            q.append((x, y+1))

    for i in range(n):
        print(arr[i])
    return(arr[n-1][m-1])


# 유클리드 호제법
# 두 자연수 a, b에 대하여 (a > b) a를 b로 나눈 나머지를 r이라고 할 때
# a와 b의 최대 공약수는 b와 r의 최대 공약수와 같다
def gcd(a,b):
    if a%b == 0:
        return b
    return gcd(b, a%b) 

if __name__ == '__main__':
    print("Result of Depth-First Search")
    dfs(graph, 1, [False]*len(graph))
    print()

    print("- - - - - - - - - - - - - - -") 

    print("Result of Breadth-First Search")
    bfs(graph, 1, [False]*len(graph))
    print()

    print("- - - - - - - - - - - - - - -") 

    print('Result of make icecream with dfs')
    print(icecream_dfs())
    #print(dfs_for_icecream(0,0))

    print("- - - - - - - - - - - - - - -") 

    print('Result of escape maze with bfs')
    array = [[1,0,1,0,1,0],
             [1,1,1,1,1,1],
             [0,0,0,0,0,1],
             [1,1,1,1,1,1],
             [1,1,1,1,1,1]]
    print(escape_maze(array, 0, 0))