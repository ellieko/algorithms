'''

나동빈 이코테 2021 강의 몰아보기
https://www.youtube.com/watch?v=acqm9mM1P6o&list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC&index=7

[다익스트라 (Dijkstra) 최단 경로 알고리즘]
특정한 노드에서 출발하여 다른 모든 노드로 가는 최단 경로를 계산
음의 간선이 없을 때 정상적으로 동작 (e.g., 현실 세계의 도로(간선) 음의 간선 x)
그리디 알고리즘으로 분류됨: "매 상황에서 가장 비용이 적은 노드를 선택"
"매 상황에서 방문하지 않은 가장 비용이 적은 노드를 선택해 임의의 과정을 반복"
(일반적으로, 최단 경로 알고리즘은 다이나믹 프로그래밍으로 분류되기도)

1) 출발 노드 설정
2) 최단 거리 테이블 초기화 (출발 노드는 0, 나머지는 무한대)
3) 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택
4) 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신
5) 3번과 4번을 반복

알고리즘 동작 과정에서 최단 거리 테이블은 각 노드에 대한
현재까지의 최단 거리 정보를 가지고 있음
처리 과정에서 더 짧은 경로를 찾으면 그 값으로 다시 갱신

단계를 거치며 한 번 처리된 노드의 최단 거리는 고정되어 더 이상 바뀌지 x
따라서 방문 처리가 된 노드는 다시 비교해주지 않아도 됨

+ 사실 마지막 노드는 처리하지 않아도 전체 결과를 얻을 수 있음
(이미 다른 노드까지의 최단 거리 값들은 바뀌지 않기 때문에)

알고리즘 수행 뒤에 테이블에 각 노드까지의 최단 거리 정보가 저장됨
완벽한 형태의 최단 경로를 구하려면 소스코드에 추가적인 기능을 더 넣어야함
'''

# 다익스트라 알고리즘 간단한 구현 방법
# 단계마다 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택하기 위해
# 매 단계마다 1차원 테이블의 모든 원소를 확인 (순차 탐색)

# V가 노드의 개수일때, time complexity 는 O(V^2)
# 전체 노드의 개수가 5,000개 이하일때에만 이 구현 방식 사용 가능
# 25,000,000 (2천 5백만)

import sys
input = sys.stdin.readline
INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수, 간선의 개수를 입력 받기
n, m = map(int, input().split())
# 시작 노드 번호를 입력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n+1)]
# 방문한 적이 있는지 체크하는 목적의 리스트 만들기
visited = [False] * (n+1)
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a,b,c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b,c))

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0   # 가장 최단 거리가 짧은 노드(인덱스)
    for i in range(1, n+1):
        if distance[i] < min_value:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
    for i in range(n-1):
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost

# # 다익스트라 알고리즘을 실행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
    # 도달할 수 없는 경우, 무한(INFINITY)라고 출력
    if distance[i] == INF:
        print('INFINITY')
    # 도달할 수 있는 경우, 거리를 출력
    else:
        print(distance[i])



# 노드의 개수가 10,000개를 넘어간다면
# 연산의 갯수가 100,000,000 (1억) 을 넘어가게 됨 (시간 초과 판정) 

'''
[우선순위 큐 (Priority Queue)]
우선순위가 가장 높은 데이터를 가장 먼저 삭제하는 자료 구조
e.g., 여러 개의 물건 데이터를 자료구조에 넣었다가
      가치가 높은 물건 데이터부터 꺼내서 확인해야하는 경우에 이용할 수 있음
표준 라이브러리 형태로 지원

|   자료구조              추출되는 데이터
|   stack               가장 나중에 삽입된 데이터
|   queue               가장 먼저 삽입된 데이터
|   priority queue      가장 우선순위가 높은 데이터


[힙 (Heap)]
우선순위 큐를 구현하기 위해 사용하는 자료구조 중 하니
최소 힙(Min Heap)과 최대 힙(Max Heap)이 있음
Min Heap: 값이 낮은 데이터부터 꺼내는 방식
Max Heap: 값이 높은 데이터부터 꺼내는 방식
다익스트라 최단 경로 알고리즘을 포함, 다양한 알고리즘에서 사용됨

|   우선순위 큐 구현 방식   삽입 시간       삭제 시간  
|   list               O(1)          O(N)
|   heap               O(logN)       O(logN)

'''
import heapq # min heap

# 힙 라이브러리 사용 예제: Min Heap (값이 낮은 데이터부터 꺼내는 방식)
# 오름차순 (Asending) 힙 정렬 (Heap Sort)
# time complexity: O(nlogn)
def heapsort_min(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

# 힙 라이브러리 사용 예제: Max Heap (값이 높은 데이터부터 꺼내는 방식)
# 내림차순 (Desending) 힙 정렬 (Heap Sort)
# time complexity: O(nlogn)
def heapsort_max(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, -value)
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result


# 다익스트라 알고리즘 개선된 구현 방법 (우선순위 큐)
# 단계마다 방문하지 않은 노드 중에서
# 최단 거리가 가장 짧은 노드를 선택하기 위해 Heap 자료구조를 이용
# 기본 동작 원리는 동일, 가장 가까운 노드를 저장해 놓기 위해 힙 자료구조를 추가적으로 이용할 뿐
# 현재의 최단 거리가 가장 짧은 노드를 선택해야 하므로 최소 힙 사용

# N, V가 각각 노드의 개수, 간선의 총 개수일 때
# time complexity는 O(ElogV)
# 직관적으로 E개의 원소를 우선순위 큐에 넣었다가 모두 빼내는 연산과 매우 유사
# -> O(ElogE) -> 중복 간선을 포함하지 않는 경우에 O(ElogV^2) -> O(ElogV)

# 노드의 개수가 10,000개를 넘어간다해도 대체적으로 1초 이내의 시간안에 연산됨

distance = [INF] * (n+1)
def dijkstra_pq(start):
    q = []
    # 시작 노드로 가기 위한 최단 거리는 0으로 설정하여 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:    # 큐가 비어있지 않다면 
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


'''
[플로이드 워셜 (Floyd-Warshall) 알고리즘]
모든 노드에서 다른 모든 노드까지의 최단 경로를 계산
다익스트라 알고리즘과 마찬가지로 단계별로 거쳐 가는 노드를 기준으로 알고리즘 수행
(다만 매 단계마다 방문하지 않은 노드 중에 최단 거리를 갖는 노드를 찾는 과정이 필요 x)
플로이드 훠셜은 2차원 테이블에 최단 거리 정보를 저장
다이나믹 프로그래밍 유형에 속함

각 단계마다 특정한 노드 k를 거쳐 가는 경우를 확인 
a에서 b로 가는 최단 거리보다 a에서 k를 거쳐 b로 가는 거리가 더 짧은지 검사
점화식: Dab = min(Dab, Dak + Dkb)

행(row):    출발 노드
열(column): 도착 노드

e.g.,
    1   2   3   4
1   0   4   INF 6       from node 1, to node 2, takes 4
2   3   0   7   INF     there's no way to get node 4 from node 2
3   5   INF 0   4
4   INF INF 2   0

1번 노드를 거쳐 가는 경우를 고려하여 테이블 갱신
2번 ...
3번 ...
4번 ...
'''

# # 노드의 개수 및 간선의 개수 입력 받기
# n = int(input())
# m = int(input())
# # 2차원 리스트를 만들고, 무한으로 초기화
# graph = [[INF] * (n+1) for _ in range(n+1)]
# # 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
# for i in range(1, n+1):
#     graph[i][i] = 0
# # 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
# for _ in range(m):
#     # A에서 B로 가는 비용은 C라고 설정
#     a, b, c = map(int, input().split())
#     graph[a][b] = c

# suppose we have initialized graph as above

# time complexity: O(N^3) (노드의 개수가 N개일 때)
# 노드의 개수가 500개 이하 정도여야 함 (500도 넉넉하진 않음)

def floyd_warshall(graph):
    # 노드 k를 거쳐서 갈 때
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    return graph

# 수행된 결과 graph를 출력
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if graph[i][j] == INF:
#             print("INFINITY", end=" ")
#         else:
#             print(graph[i][j], end=" ")
#     print()


# 연습 문제 1) 전보
# N개의 도시가 있고 X에서 Y로 전보를 보내려면 X->Y 통로가 있어야함, 전보 시 일정 시간도 소요됨
# 메세지는 도시 X에서 출발하여 각 도시 사이에 설치된 통로를 거쳐 최대한 많이 퍼져나갈 것
# 도시 X의 번호와 통로의 정보가 주어졌을 때
# 1) 메세지를 받게 되는 도시의 개수는 총 몇개이며
# 2) 도시들이 모두 메세지를 받는 데까지 걸리는 시간은 얼마인지? (동시에 전달되면 Max 시간인데...)

# e.g., 
# 3 2 1 - 도시의 개수 3, 통로의 개수 2, 도시 1이 메세지를 보낼 것임
# 1 2 4 - 도시1에서 도시2까지의 통로 존재, 메세지 전달 시간은 4
# 1 3 2 - 도시1에서 도시3까지의 통로 존재, 메세지 전달 시간은 2
n, m, c = 3, 2, 1
g = [[] for i in range(4)]
for line in ['1 2 4', '1 3 2']:
    a,b,t = map(int, line.split())
    g[a].append((b,t))
distance = [INF]* (n+1)

# 한 도시에서 다른 도시까지의 최단 거리 문제로 치환할 수 있음
# N과 M의 범위가 충분히 크기 떄문에 우선순위 큐를 활용한 다익스트라 알고리즘을 구현
# INF가 아닌 distance element의 개수 = 메세지 전달 가능한 도시
# 도달 가능한 노드 중, 가장 오래 걸리는 노드와의 거리(시간)

def telegraph(c):
    # suppose our dijkstra_pq returns distance list
    list = dijkstra_pq(c)
    count, max_d = -1, 0         # count: excluding the first index
    for d in list:
        if d != INF:
            count += 1
            max_d = max(max_d, d)
    print(count, max_d)
 


# 연습 문제 2) 미래 도시
# 1번부터 N번까지의 회사 (N, M <= 100), 연결된 2개의 회사는 양방향으로 연결되어 있음
# 연결된 회사는 각각 모두 1의 시간 소요 (M: 경로의 개수)
# 1번 회사에서 출발, K번 회사 찍고, X번 회사로 가는 것이 목표
# 최소 시간? 도달할 수 없다면 -1 출력

# suppose connections is a list of tuple; connected companies; (a, b)
# 1 -> k -> x
def future_city(n, connections, x, k):
    g = [[INF] * (n+1) for _ in range(n+1)]
    time = 0
    for a,b in connections:
        g[a][b] = 1
        g[b][a] = 1
    graph = floyd_warshall(g)
    if INF in (graph[1][k], graph[k][x]):
        return -1
    else:
        return graph[1][k] + graph[k][x]