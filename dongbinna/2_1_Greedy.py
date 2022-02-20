'''

나동빈 이코테 2021 강의 몰아보기
https://www.youtube.com/watch?v=2zjoKjt97vQ&list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC&index=3

그리디 알고리즘 (Greedy Algorithm)
현재 상황에서 지금 당장 좋은 것만 고르는 방법 - 정당성 분석이 중요
"단순히 가장 좋아보이는 것을 반복적으로 선택해도 최적의 해를 구할 수 있는가?"

일반적인 상황에서 그리디 알고리즘은 최적의 해를 보장할 수 없을 때가 많음
(하지만 코딩 테스트에서는 이렇게 얻은 해가 최적의 해가 되는 상황에서 이를 추론할 수 있어야 풀리도록 출제제

'''

# PROBLEM 1. 거스름 돈 with 최소의 동전 갯수
# 알고리즘: 가장 큰 화폐 단위부터 돈을 거슬러준다.
# 정당성 분석: coin_list안의 큰 단위 동전이 항상 작은 단위 동전의 배수이므로 가능
#           이러면 작은 단위의 동전들을 통합해 다른 해가 나올 수 없음
#           counter example) change = 800, coin_list = [500, 400, 100, 50]
#                            우리의 해는 (500:1, 300: 3) -> 4, 최적의 해는 (400: 2) -> 2
# time complexity: O(K), K는 동전의 갯수, change에 대해서는 영향을 받지않음

def minimum_change(change):
    coin_list = [500, 100, 50, 10]
    change_num = 0
    for coin in coin_list:
        change_num += change // coin
        change = change % coin
    return change_num

''' (*** until_one_v2 코드 리뷰 필요, 이해 잘 X ***) '''
# PROBLEM 2. 1이 될 때까지의 step들의 최소 횟수 
# 어떠한 수 N이 1이 될 때까지 아래 두 과정 중 하나를 반복적으로 선택, 수행.
# N에서 1을 뺀다 or N을 K로 나눈다 (the latter only choosable when N%K==0)

# 알고리즘: 주어진 N에 대하여 최대한 많이 나누기를 수행
# 설명: N의 값을 줄일 때 2 이상의 수로 나누는 작업이 1을 빼는 작업보다 수를 훨씬 많이 줄일 수 있음
# 정당성 분석: K가 2 이상이기만 하면 나누기를 통해 step을 기하급수적으로 줄일 수 있음
#           또한 N은 항상 1에 도달하게 됨
# time complexity: O(N)

def until_one(N, K, counter):
    if N == 1:
        return counter
    return until_one(N // K, K, counter + 1) if N % K == 0 else until_one(N-1, K, counter+1)

# 1을 하나씩 빼지 않고, 1을 몇 번 빼야할지 계산해서 빼기 때문에 반복 횟수 급감 (N이 클 때)
# time complexity: O(log N)
def until_one_v2(N, K):
    counter = 0
    while True:
        # subtract 1 from N until N % K == 때
        target = (N // K) * K   # the cloest number of N divisible by K
        counter += (N - target) # subtract 1 from N until it reaches to target
        N = target 
        if N < K:
            break
        counter += 1
        N //= K

    # if N is bigger than 1, to change it to N
    counter += (N - 1)
    return counter


# PROBLEM 3. 곱하기 혹은 더하기
# 0부터 9까지의 숫자들로 이루어진 문자열 S에
# 왼쪽에서부터 모든 숫자 사이에 곱하기 혹은 더하기 연산자를 넣어 만들어질 수 있는 가장 큰 수
# (모든 연산은 왼쪽에서부터 이루어짐, 1<= S의 길이 <= 20)

# "두 수 중에서 하나라도 0 혹은 1인 경우를 제외하고는"
# '+' 보다 '*'가 더 값을 크게 만듬
# a 만족 -> b or c: 전형적인 그리디 알고리즘

def multiply_or_add(s):
    # s = list(map(int, list(s)))
    ans = int(s[0])
    for i in range(1, len(s)):
        num = int(s[i])
        if ans >= 2 and num >=2:
            ans *= num
        else:
            ans += num
    return ans

''' (*** 전체적으로 리뷰 필요, 이해 잘 X ***) '''
# PROBLEM 4. 모험가 길드
# 마을에 모험가 N명, N명의 모험가 대상으로 '공포도' 측정
# 공포도가 X인 모험가는 반드시 X명 이상으로 구성한 모험가 그룹 참여
# 최대 몇 개의 모험가 그룹을 만들 수 있는지, 여행을 떠날 수 있는 그룹 수의 최댓값
# 모든 모험가를 특정한 그룹에 넣을 필요는 X (몇 명의 모험가는 마을에 남아있어도 O)
# adventure_guild(5, [2,3,1,2,2]) -> 2

# 알고리즘: 오름차순 정렬 이후에 공포도가 가장 낮은 모험가부터 하나씩 확인, 현재 그룹 멤버의 수보다 현재 공포도보다 크거나 같으면 그룹 설정
# 분석: 오름차순으로 정렬되어 있기 때문에 항상 최소한의 그룹 멤버만을 통해서 그룹이 결성됨, 최소한의 그룹 멤버들만을 통해 그룹이 결성되니 그룹 갯수는 최댓값
def adventure_guild(n, fear_list):
    fear_list.sort()
    group_num = 0
    group_mem_count = 0
    for fear in fear_list:
        group_mem_count += 1
        if fear <= group_mem_count:
            group_num += 1
            group_mem_count = 0
    return group_num



if __name__ == '__main__':

    print("- - - - - - - - - - - - - - -")

    # POBLEM 1. 거스름 돈 with 최소의 동전 갯수
    print(f"PROBLEM 1. minimum # of coins for change 1260 is {minimum_change(1260)}") # 6

    print("- - - - - - - - - - - - - - -")

    # PROBLEM 2. 1이 될 때까지의 step들의 최소 횟수
    print(f"PROBLEM 2. (N:17, K:4) - minimum # of steps until N to be 1 is {until_one(17, 4, 0)}") # 3
    print(f"PROBLEM 2. (N:17, K:4) - minimum # of steps until N to be 1 is {until_one_v2(17, 4)}") # 3

    print("- - - - - - - - - - - - - - -")

    # PROBLEM 3. 곱하기 혹은 더하기
    print(f"PROBLEM 3. S=\"02984\" - maximum possiblely made value is {multiply_or_add('02984')}") # 576
    print(f"PROBLEM 3. S=\"567\" - maximum possiblely made value is {multiply_or_add('567')}")     # 210

    print("- - - - - - - - - - - - - - -")

    # PROBLEM 4. 모험가 길드
    print(f"PROBLEM 4. (n: 5, fear_list: [2, 3, 1, 2, 2]) - maximum group that can go on a trip is {adventure_guild(5, [2, 3, 1, 2, 2])}") # 2