'''

나동빈 이코테 2021 강의 몰아보기
https://www.youtube.com/watch?v=2zjoKjt97vQ&list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC&index=3

[Dynamic Programming] 다이나믹 프로그래밍 (동적 계획법)
메모리를 적절히 사용하여 수행 시간 비효율성을 비약적으로 향상시키는 방법
이미 계산된 결과(작은 문제)는 별도의 메모리 영역에 저장하여 다시 계산하지 않도록 함
구현: top down(하향식), bottom up(상향식)

*일반적인 프로그래밍 분야에서의 Dynimic (동적)은
자료구조에서 Dynamic Allocation (동적 할당); 프로그램이 실행되는 도중에 실행에 필요한 메모리를 할당하는 기법을 의미
*여기서의 Dynamic은 별다른 의미 없이 사용된 단어

문제가 다음의 조건을 만족할 때 사용할 수 있음
1) Optimal Substructure (최적 부분 구조)
   큰 문제를 작은 문제로 나눌 수 있으며, 작은 문제의 답을 모아 큰 문제를 해결할 수 있음 
2) Overlapping Subproblem (중복되는 부분 문제)
   동일한 작은 문제를 반복적으로 해결해야 함

'''

# e.g. fibonacci
#      1,1,2,3,5,8,13,21,34,55,89,...

# time complexity: O(2^N) (중복되는 부분 문제 발생)

def fibonacci_recursive(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Memoization 
# 이전에 계산된 결과를 일시적으로 기록해 놓는 넓은 개념을 의미하므로
# 다이나믹 프로그래밍에 국한된 개념은 아님 (담아 놓고 다이나믹 프로그래밍을 위해 활용하지 않을 수도 있음)
# 값을 기록해 놓는다는 점에서 caching 이라고도 함
# 결과 저장용 리스트는 cache, memo_table, dp, d, dp_table 등으로 부름

# Top down (하향식) 방식
# 한번 계산한 결과를 메모리 공간에 메모하는 기법, 구현과정에서 재귀함수를 이용
# 같은 문제를 다시 호풀하면 메모했던 결과를 그대로 가져옴
def fibo_top_down(n, d=[0]*100):
    if n == 1 or n == 2:
        return 1
    if d[n-1] != 0:
        return d[n-1]
    d[n-1] = fibo_top_down(n-1, d) + fibo_top_down(n-2, d)
    return d[n-1]

# Bottom up (상향식) 방식 - 다이나믹 프로그래밍의 전형적인 형태
# 먼저 계산했던 것들을 활용해서 그 다음 것을 계산, 반복문이 이용됨 (dp table)
def fibo_bottom_up(n):
    arr = [1,1]
    for i in range(2, n):
        arr.append(arr[i-2] + arr[i-1])
    return arr[n-1]

# --> Dynamic Programming time complexity: O(N)



'''
[Dynamic Programming (다이나믹 프로그래밍) vs Divide and Conquer (분할 정복)]

둘은 모두 최적 부분 구조를 가질 때 사용할 수 있음
(큰 문제를 작은 문제로 나눌 수 있으며 작은 문제의 답을 모아서 큰 문제를 해결할 수 있는 상황)

차이점은 "부분 문제의 중복"
다이나믹 프로그래밍 문제에서는 각 부분 문제들이 서로 영향을 미치며 부분 문제가 중복 (e.g. top down/bottom up fibonacci)
분할 정복 문제에서는 동일한 부분 문제가 반복적으로 계산되지 않음 (e.g. quick sort)
--> e.g. Quick Sort: 한 번 기준 원소(pivot)가 자리를 변경해서 자리를 잡으면, 그 기분 원소의 위치는 바뀌지 x
        분할 이후에 해당 피벗을 다시 처리하는 부분 문제는 호출하지 않음


[다이나믹 프로그래밍 문제에 접근하는 방법]
주어진 문제가 다이나밍 프로그래밍 유형임을 파악하는 것이 중요
가장 먼저 그리디, 구현, 완전 탐색 등의 아이디어로 문제를 해결할 수 있는지 검토
    다른 알고리즘으로 풀이 방법이 떠오르지 않으면 다이나믹 프로그래밍 고려
일단 재귀 함수로 비효율적인 완전 탐색 프로그램을 작성한 뒤에 (탑다운) 작은 문제에서 구한 답이
큰 문제에서 그대로 사용될 수 있으면, 코드를 개선하는 방법을 사용할 수 있음
'''



# 연습 문제 1) 개미 전사
# 각 식량 창고의 식량의 개수들이 나열된 리스트가 주어지고
# 개미는 인접한 창고를 약탈할 수는 없음
# 이때 개미 전사가 얻을 수 있는 식량의 최댓값은?
# e.g. food_robber([1,3,1,5]) -> 8

# 재귀 함수로 비효율적인 완전 탐색 프로그래밍
def food_robber_inefficient(l, start, total):
    if start >= len(l):
        return total 
    x = food_robber_inefficient(l, start+2, total+l[start])
    if start+1 == len(l):
        return x
    else:
        return max(x, food_robber_inefficient(l, start+3, total+l[start+1]))

# 문제 해결 아이디어
# ai = i번째 식량 창고까지의 최적의 해 (얻을 수 있는 식량의 최댓값)
# ki = k번째 식량 창고에 있는 식량의 양
# ai = max(a(i-1), a(i-2)+ki)
# 한 칸 이상 떨어진 식량 창고는 항상 털 수 있으므로 (i-3)번째 이하는 고려할 필요가 없음
# 다이나믹 프로그래밍(bottom top)
def food_robber_dp(l):
    dp = []
    for i in range(len(l)):
        if i<=1:
            dp.append(l[i])
        else:
            dp.append(max(dp[i-1], dp[i-2]+ l[i]))
    return dp[-1]


# 연습 문제 2) 1로 만들기
# 정수 X -> 4가지 연산 가능
#          i)   5로 나누어 떨어지면, 5로 나눔
#          ii)  3으로 나누어 떨어지면, 3으로 나눔
#          iii) 2로 나누어 떨어지면, 2로 나눔
#          iv) 1을 뺌
# 연산 4개를 이용해서 값을 1로 만들려고 함. 연산의 최소 사용 횟수는?
# e.g. minimum_calcuation(26) -> 3
#      (26 -> 25 -> 5 -> 2)

# Top down
# RecursionError: maximum recursion depth exceeded in comparison
def minimum_calculation(x):
    dp = [0] * (x+1)
    if x == 1:
        return dp[x]
    if x%5 == 0:
        dp[x//5] = dp[x] + 1
    if x%3 == 0 and dp[x//3] != -1:
        dp[x//3] = dp[x] + 1
    if x%2 == 0 and dp[x//2] != -1:
        dp[x//2] = dp[x] + 1
    dp[x-1] = dp[x] + 1
    return minimum_calculation(min(dp[x//5], dp[x//3], dp[x//2], dp[x-1]))

# Botton up
def minimum_calculation_sol(x):
    dp = [0]*(x+1)
    for i in range(2, x+1):
        dp[i] = dp[i-1] + 1
        if i%5 == 0:
            dp[i] = min(dp[i], dp[i//5] + 1)
        if i%3 == 0:
            dp[i] = min(dp[i], dp[i//3] + 1)
        if i%2 == 0:
            dp[i] = min(dp[i], dp[i//2] + 1)
    return dp[x]



# 연습 문제 3) 효율적인 화폐 구성
# N가지 종류의 화폐가 있을 때, M원을 만들기 위한 최소한의 화폐 개수
# 1 <= N <= 100, 1 <= M, 10,000
# e.g. minumum_change([2,3],15)     -> 5
# e.g. minimum_change([3,5,7], 4)   -> -1 (불가능할 때)

# 문제 해결 아이디어
# ai = 금액 i를 만들 수 있는 최소한의 화폐 개수
# k = 각 화폐의 단위
# 점화식 = 각 화폐 단위인 k를 "하나씩 확인하며"
# a(i-k)를 만드는 방법이 존재하는 경우, ai = min(ai, a(i-k) + 1)
# a(i-k)를 만드는 방법이 존재하지 않는 경우, ai = INF

# time complexity: O(N*M) = O(1,000,000) = 백만
# 무한대는 10,001로 표현 가능
def minimum_change(l, m):
    dp = [0] + [10001]*m
    for coin in l:
        for i in range(coin, m+1):
            if dp[i-coin] != 10001:
                dp[i] = min(dp[i-coin] + 1, dp[i])
    return dp[m] if dp[m] != 10001 else -1



# 연습 문제 4) 금광
# n*m 크기의 금광, 각 칸에는 특정한 크기의 금이 들어있음
# 첫 번째 열부터(column) 금을 캐기 시작, 맨 처음에는 첫째 열의 어느 행에서든(row) 출발할 수 있음
# 이후에 m-1번에 결쳐서 매번 오른쪽 위, 오른쪽, 오른쪽 아래 3가지 중 하나의 위치로 이동해야함 (대각선 위, 대각선 아래, 옆)
# 채굴자가 얻을 수 있는 금의 최대 크기는?

# n m
# 3 4
# 1 3 3 2 2 1 4 1 0 6 4 7   -> 19
# 1 3 3 2
# 2 1 4 1
# 0 6 4 7

# 문제 해결 아이디어
# 금광의 모든 위치에 대하여 세 가지만 고려하면 됨
# 왼쪽 위에서 오는 경우, 왼쪽에서 오는 경우, 왼쪽 아래에서 오는 경우
# dp[i][j]: i행 j열까지의 최적의 해 (얻을 수 있는 최댓값)
# (i-1, j-1), (i, j-1), (i+1, j-1)
# 최댓값은 가장 오른쪽의 값일 것임
def mining_gold(n,m, area):
    dp = [[area[i][0]] + [0 for i in range(m-1)] for i in range(n)]
    for i in range(n):
        for j in range(1, m):
            dp[i][j] = max(dp[i-1][j-1] if i-1 >= 0 and j-1 >=0 else 0,
                           dp[i][j-1],
                           dp[i+1][j-1] if i+1 < n and j-1 >=0 else 0) + area[i][j]

    return(max([dp[i][-1] for i in range(n)]))



# 연습 문제 5) 병사 배치하기
# 전투력이 높은 병사가 앞쪽에 오도록 내림차순 배치
# 배치 과정 중 특정한 위치의 병사 열외시킴
# 남아있는 병사의 수가 최대로
# 병사에 대한 정보가 주어졌을 때, 남아있는 병사의 수가 최대가 되도록 하기 위해
# 열외시켜야하는 병사의 수를 출력하는 프로그램
# e.g. leave_out_solider([15,11,4,8,5,2,4]) -> 2

# 문제 해결 아이디어: 가장 긴 증가하는 부분 수열(Longest Increasing Subsequence)

# Longest Increading Subsequence (LIS) 알고리즘
# D[i] = array[i]를 마지막 원소로 가지는 부분 수열의 최대 길이
# 0 <= j < i에 대하여, D[i] = max(D[i], D[j]+1) if array[j] < array[i]
def longest_increasing_subsequence(l):
    dp = [1 for i in range(len(l))]
    for i in range(1, len(l)):
        for j in range(i):
            if l[j] < l[i]:
                dp[i] = max(dp[i], dp[j] +1)
    return max(dp)

def leave_out_solider(l):
    dp = [1 for i in range(len(l))]
    for i in range(1, len(l)):
        for j in range(i):
            if l[j] >= l[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return len(l) - max(dp)




if __name__ == '__main__':

    print(fibonacci_recursive(1))           # 1
    print(fibonacci_recursive(2))           # 1
    print(fibonacci_recursive(3))           # 2
    print(fibonacci_recursive(6))           # 8
    # print(fibonacci_recursive(50))        taking too long

    print(fibo_top_down(1))                 # 1
    print(fibo_top_down(2))                 # 1
    print(fibo_top_down(3))                 # 2
    print(fibo_top_down(6))                 # 8
    print(fibo_top_down(50))                # 12586269025
    print(fibo_top_down(99))                # 218922995834555169026

    print(fibo_bottom_up(1))                # 1
    print(fibo_bottom_up(2))                # 1
    print(fibo_bottom_up(3))                # 2
    print(fibo_bottom_up(6))                # 8
    print(fibo_bottom_up(50))               # 12586269025
    print(fibo_bottom_up(99))               # 218922995834555169026

    print("- - - - - - - - - - - - - - -")

    # 연습 문제 1) 개미 전사
    print(food_robber_inefficient([1,3,1,5],0,0))       # 8
    print(food_robber_inefficient([1,3,1,5,7],0,0))     # 10

    print(food_robber_dp([1]))              # 1
    print(food_robber_dp([1,3]))            # 3
    print(food_robber_dp([1,3,1,5]))        # 8
    print(food_robber_dp([1,3,1,5,7]))      # 10

    print("- - - - - - - - - - - - - - -")

    # 연습 문제 2) 1로 만들기
    print(minimum_calculation)                  # Top down      3
    print(minimum_calculation_sol(26))          # Bottom up     3

    print("- - - - - - - - - - - - - - -")

    # 연습 문제 3) 효율적인 화폐 구성
    print(minimum_change([2,3],15))             # 5
    print(minimum_change([3,5,7],4))            # -1
    print(minimum_change([2,3,5],7))            # 2

    print("- - - - - - - - - - - - - - -")

    # 연습 문제 4) 금광
    # input 받기
    # n, m = map(int, input().split())
    # array = list(map(int, input().split()))
    # d = []
    # index = 0
    # for i in range(n):
    #     d.append(array[index:index+m])
    #     index += m

    print(mining_gold(3,4,[[1,3,3,2], [2,1,4,1], [0,6,4,7]]))

    print("- - - - - - - - - - - - - - -")

    # 연습 문제 5) 병사 배치하기
    print(longest_increasing_subsequence([10,9,2,5,3,7,101,18])) # 4
    print(leave_out_solider([15,11,4,8,5,2,4]))                  # 2