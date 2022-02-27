'''
[Binary Search] 이진 탐색
정렬되어 있는 리스트에서 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 방법
시작점, 끝점, 중간점을 이용하여 탐색 범위를 설정함

(<-> 순차 탐색: 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 확인하는 방법)

time complexity: logN (밑: 2)
단계마다 탐색 범위를 2로 나누는 것과 동일하므로 연산 횟수는 logN에 비례 (밑: 2)
'''

def binary_search(l, num):
    start, end = 0, len(l)-1
    while start <= end:
        mid = (start+end)//2
        if l[mid] == num:
            return mid
        elif l[mid] < num:
            start = mid + 1
        else:
            end = mid - 1
    return -1

def binary_search_recursive(l, num, start, end):
    if start > end:
        return -1
    mid = (start+end)//2
    if l[mid] == num:
        return mid
    elif l[mid] < num:
        return binary_search_recursive(l, num, mid+1, end)
    else:
        return binary_search_recursive(l, num, start, mid-1)



# 이진 탐색 활용 문제: Parametric Search 
# 최적화 문제를 결정 문제(예 혹은 아니오)로 바꾸어 해결하는 기법
# (최적화 문제란? 어떤 함수의 값을 가능한 만큼 낮추거나 혹은 최대한 높이거나 하는 문제)
# e.g. 특정한 조건을 만족하는 가장 알맞은 값을 빠르게 찾는 최적화 문제
# 일반적으로 코딩 테스트에서의 파라메트릭 서치 문제는 이진 탐색을 이용하여 해결할 수 있음
 
# 연습 문제 1) 떡볶이 떡 만들기
# 높이가 19, 14, 10, 17cm인 떡이 나란히 있고 절단기 높이 = 15cm,
# 자른 뒤 떡의 높이는 15, 14, 10, 15cm, 이 때 손님은 6cm만큼의 떡을 가져감
# 손님이 요청한 총 길이가 M일 때,
# 적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값은?
# 절단기의 높이는 0부터 10억(10^9)까지의 정수 중 하나 --> 큰 탐색 범위 --> 이진 탐색

# input                                 output
# 4 6 (떡의 개수 N과 요청한 떡의 길이 M)       15       
# 19 15 10 17   (떡의 개별 높이)

# 문제 해결 아이디어: 시작점 = 0, 끝점 = 19, 중간점 = 9 (이게 절단기의 높이 자체)
# 절단기의 높이가 반드시 주어진 리스트 내에 있다는 확신이 없으므로 주어진 떡의 길이만을 절단기의 높이로 고려할 수 없음
# 절단기의 높이는 0부터 주어진 떡의 최댓값까지 가능
#   - 절단기의 높이가 0일 때: 요청한 떡의 길이가 주어진 떡들의 총합일 때
#   - 절단기의 높이가 주어진 떡들의 최댓값일 때: 요청한 떡의 길이가 0일 때
def maximum_height(l, m):
    start, end, height = 0, max(l), 0
    while start <= end:
        h = (start+end)//2
        amount = sum([x-h for x in l if x > h])
        # 양이 부족한 경우, h를 줄여서 양을 늘려야함
        if amount < m:
            end = h - 1
        # 양이 충분한 경우, height를 업데이트하고 더 큰 h 탐색
        # 조건에 만족하는 이상 h가 큰 값에서 작은 값이 될리는 없음
        # 조건이 만족하면 우리는 h를 증가시키니까 height는 가능한 제일 큰 절단기 높이가 되어있을 것
        else:
             height = h
             start = h + 1
    return height  


# 연습 문제 2) 정렬된 배열에서 특정 원소의 개수 구하기
# 수열은 오름차순으로 정렬되어 주어지고, 시간 복잡도는 logN 이어야만 함

# python의 이진 탐색 라이브러리
from bisect import bisect_left, bisect_right
# bisect_left(a, x):    정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스를 반환
# bisect_right(a, x):   정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 인덱스를 반환
# e.g. a = [1,2,4,4,8]
#      bisect_left(a,4)    -> 2
#      bisect_right(a,4)   -> 4

# 값이 특정 범위에 속하는 데이터 개수 구하기 - 리스트가 정렬되어 있을 때, 값이 [left_value, right_value]인 데이터의 개수
# e.g. a = [1,2,3,3,3,3,4,4,8,9]
#      count_by_range(a,4,4)  -> 2
#      count_by_range(a,-1,3) -> 6
def count_by_range(a, left_value, right_value):
    return bisect_right(a, right_value) - bisect_left(a, left_value)


if __name__ == '__main__':

    # binary search
    print(binary_search([0,2,4,6,8,10,18], 0))                      # 0
    print(binary_search([0,2,4,6,8,10,18], 18))                     # 6
    print(binary_search([0,2,4,6,8,10,18], 4))                      # 2
    print(binary_search([0,2,4,6,8,10,18], 12))                     # -1

    # binary search (recursive)
    print(binary_search_recursive([0,2,4,6,8,10,18], 0, 0, 6))      # 0
    print(binary_search_recursive([0,2,4,6,8,10,18], 18, 0, 6))     # 6
    print(binary_search_recursive([0,2,4,6,8,10,18], 4, 0, 6))      # 2
    print(binary_search_recursive([0,2,4,6,8,10,18], 12, 0, 6))     # -1

    # count by range
    print(count_by_range([1,2,3,3,3,3,4,4,8,9], 4, 4))              # 2
    print(count_by_range([1,2,3,3,3,3,4,4,8,9], -1, 3))             # 6


    # practice problems
    # 연습 문제 1) 떡볶이 떡 만들기 
    print(maximum_height([19,15,10,17], 6))                         # 15