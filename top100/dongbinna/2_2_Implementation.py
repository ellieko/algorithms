'''

나동빈 이코테 2021 강의 몰아보기
https://www.youtube.com/watch?v=2zjoKjt97vQ&list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC&index=3

구현 (Implementation)
풀이를 떠올린느 것은 쉽지만 소스코드로 옮기기 어려운 문제를 지칭

알고리즘은 간단한데 코드가 지나치게 길어지는 문제,
실수 연산을 다루고, 특정 소수점 자리까지 출력해야하는 문제,
문자열을 특정한 기준에 따라서 끊어 처리해야 하는 문제,
적절한 라이브러리를 찾아서 사용해야 하는 문제

- 일반적으로 알고리즘 문제에서 2차원 공간은 행렬(Matrix)의 의미로 사용됨
for i in range(5):
    for j in range(5):
        print('(', i, ',', j, ')', end= ' ') -- 여기서 end 는 newline 을 없앰
    print()

            y       y + 1     y + 2      ...  
x       ( 0 , 0 ) ( 0 , 1 ) ( 0 , 2 ) ( 0 , 3 ) ( 0 , 4 ) 
x + 1   ( 1 , 0 ) ( 1 , 1 ) ( 1 , 2 ) ( 1 , 3 ) ( 1 , 4 ) 
x + 2   ( 2 , 0 ) ( 2 , 1 ) ( 2 , 2 ) ( 2 , 3 ) ( 2 , 4 ) 
...     ( 3 , 0 ) ( 3 , 1 ) ( 3 , 2 ) ( 3 , 3 ) ( 3 , 4 ) 
        ( 4 , 0 ) ( 4 , 1 ) ( 4 , 2 ) ( 4 , 3 ) ( 4 , 4 ) 

- 시뮬레이션 및 완전 탐색 문제에서는 2차원 공간에서의 방향 벡터가 자주 활용됨
x는 row 를 y는 column을 지칭

      동  북  서  남
dx = [0, -1,  0, 1]
dy = [1,  0, -1, 0]

# 다음 위치 아래와 같이 print 할 수 있음
for i in range(4):
    nx = x + dx[i]
    nx = y + dx[i]
    print(nx, ny) 
'''

# PROBLEM 1. 상하좌우
# 여행가 A는 NxN 크기의 정사각형 공간 위에 위치, 이 공간은 1x1 크기의 정사각형으로 나누어져 있음
# 가장 왼쪽 위 좌표는 (1, 1) - 시작 좌표, 가장 오른쪽 좌표는 (N, N)
# 상(U), 하(D), 좌(L), 우(R)로 이동할 수 있으며
# 움직임이 적힌 계획서를 따라 이동하되, 공간을 벗어나는 움직임은 무시, 도착점 출력
# udlr_arrive_at(5, [R, R, R, U, D, D]) -> 3 4

def udlr_arrive_at(n, map):
    #     R        U        L       D
    dx = {'R': 0, 'U': -1, 'L': 0, 'D': 1}
    dy = {'R': 1, 'U': 0, 'L': -1, 'D': 0}
    x, y = 1, 1
    for i in map:
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 1 and nx <= n and ny >= 1 and ny <= n:
            x, y = nx, ny
    return(x, y)


# PROBLEM 2. 시각
# 정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서
# 3이 하나라도 포함되는 모든 경우의 수 출력

# python: 1초에 2000만번의 연산, 하루는 24*60*60 = 86,400초
# 알고리즘: Brute Forcing (완전 탐색)
def count_three_til(n):
    count = 0
    for i in range(n + 1):
        for j in range(60):
            for k in range(60):
                if '3' in str(i) + str(j) + str(k):
                    count += 1
    return count


# PROBLEM 3. 왕실의 나이트
# 왕실 정원  = 8 x 8 좌표 평면 (행 column: 1-8, 열 row: a-h), 특정 한 칸에 나이트
# 나이트는 이동 시 L자 형태로만 이동 가능, 정원 밖 X
# 나이트 이동 방법: 1) 수평으로 두 칸 이동 뒤, 수직으로 한 칸
#               2) 수직으로 두 칸 이동 뒤, 수평으로 한 칸
# 나이트 위치가 주어졌을 때 나이트가 이동 가능한 경우의 수
# knight_move('a1') -> 2
def knight_move(position):
    # 8 possible movenments
    # R2U1, R2D1, L2U1, L2D1
    # R1U2, R1D2, L1U2, L1D2
    dx = [-1, 1, -1, 1, -2, 2, -2, 2]
    dy = [2, 2, -2, -2, 1, 1, -1, -1]
    # moves = [(-1, 2), (1, 2), (-1,-2), (1, -2), (-2, 1), (2, 1), (-2, -1), (2, -1)]
    x, y, count = int(ord(position[0])) - int(ord('a')) + 1, int(position[1]), 0
    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 1 or nx > 8 or ny < 1 or ny > 8:
            continue
        count += 1
    return count
    

# PROBLEM 4. 문자열 재정렬
# 알파벳 대문자와 숫자(0-9)로만 구성된 문자열이 입력,
# 모든 알파벳을 오름차순으로 정렬하고 이어서 모든 숫자를 더한 값을 출력
# reorganize('K1KA5CB7') -> 'ABCKK13'

def reorganize(s):
    l, total = sorted(list(s)), 0
    for i in range(len(l)):
        if ord(l[i]) <= ord('9'):
            total += int(l[i])
            l[i] = ''
    l.append(str(total))
    return ''.join(l)

def reorganize_v2(s):
    result, total = [], 0
    for elem in s:
        if elem.isalpha():
            result.append(elem)
        else:
            total += int(elem)
    result.sort()
    if total != 0:
        result.append(str(total))
    return ''.join(result)

if __name__ == '__main__':

    print("- - - - - - - - - - - - - - -")

    # PROBLEM 1. 상하좌우
    print(f"PROBLEM 1. arrival point with RRRUDD is {udlr_arrive_at(5, ['R', 'R', 'R', 'U', 'D', 'D'])}") # 3 4

    print("- - - - - - - - - - - - - - -")

    # PROBLEM 2. 시각
    print(f"PROBLEM 2. number of all cases including at least one 3 from 00:00:00 to 05:59:59 is {count_three_til(5)}") # 11475

    print("- - - - - - - - - - - - - - -")

    # PROBLEM 3. 왕실의 나이트
    print(f"PROBLEM 3. number of cases kinght can move from 'a1' is {knight_move('a1')}") # 2
    
    print("- - - - - - - - - - - - - - -")

    # PROBLEM 4. 문자열 재정렬
    print(f"PROBLEM 4. reorganized string of K1KA5CB7 is {reorganize('K1KA5CB7')}") # ABCKK13
    print(f"           reorganized string of K1KA5CB7 is {reorganize_v2('K1KA5CB7')}") # ABCKK13
    print(f"           reorganized string of AJKDLSI412K4JSJ9D is {reorganize('AJKDLSI412K4JSJ9D')}") # ADDIJJJKKLSS20
    print(f"           reorganized string of AJKDLSI412K4JSJ9D is {reorganize_v2('AJKDLSI412K4JSJ9D')}") # ADDIJJJKKLSS20