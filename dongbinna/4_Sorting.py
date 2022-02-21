'''
[Selection Sort]
처리되지 않은 데이터 중에서 가장 작은 데이터를 선택해
맨 앞에 있는 데이터와 바꾸는 것을 반복

time complexity: O(N^2)
아이디어가 매우 간단, 구현이 쉬움

'''
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


'''
[Insertion Sort]
처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입
선택 정렬에 비해 구현 난이도가 높은 편이지만, 일반적으로 더 효율적

time complexity: O(N^2)
in best scenario, where almost all itmes are already sorted, O(N)
데이터가 거의 정렬되어 있을 때는 가장 빠름

'''
def insertion_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j] 
            else:
                break
    return arr


'''
[Quick Sort]
기준 데이터를 설정하고, 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법
일반적인 상황에서 제일 많이 사용되는 정렬 알고리즘 중 하나
merge sort와 더불어 대부분의 프로그래밍 언어의 정렬 라이브러리의 근간이 되는 알고리즘
가장 기본적인 퀵 정렬은 첫 번째 데이터를 pivot으로 설정

time complexity: in average, O(NlogN)
in the worst case, where everything is already sorted and your pivot is the first data, O(N^2) 
                , that is, where partion doesn't work out efficiently
대부분의 경우에 가장 적합, 충분히 빠름
'''
def quick_sort(arr, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        # look for item that is bigger than pivot
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        # look for item that is smaller than pivot
        while right > start and arr[right] >= arr[pivot]:
            right -= 1
        if (left > right):
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:
            arr[left], arr[right] = arr[right], arr[left]
    quick_sort(arr, start, right-1)
    quick_sort(arr, right+1, end)

def quick_sort_v2(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    tail = arr[1:]
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]
    return quick_sort_v2(left_side) + [pivot] + quick_sort_v2(right_side)


'''
[Counting sort]
특정한 조건이 부합할 때만 사용할 수 있지만, 매우 빠르게 동작하는 정렬 알고리즘
(데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때 사용 가능, 0 보다 크거나 같은 정수들로만...)
데이터의 개수가 N, 데이터(양수) 중 최댓값이 K 일 때 최악의 경우에도 O(N+K)를 보장

time complexity and space complexity: O(N+K)
때에 따라서 심각한 비효율성 초래, e.g. [0, 999,999]
동일한 값을 가지는 데이터가 여러개 등장할 때 효과적, e.g. 성적
데이터의 크기가 한정되어 있는 경우에만 사용 가능하지만 매우 빠름
'''

def count_sort(arr):
    ans = []
    index = [0] * (max(arr)+1)
    for elem in arr:
        index[elem] += 1
    return sum([[item]*count for item, count in enumerate(index)],[])


'''
[정렬 알고리즘 비교]
                    average time complexity     space complexity
* Selection Sort            O(N^2)                   O(N)
* Insertion Sort            O(N^2)                   O(N) 
* Quick Sort               O(NlogN)                  O(N)
* Counting Sort             O(N+K)                  O(N+K)

'''

# 연습 문제 1) 두 배열의 원소 교체
# 두 개의 배열 A, B, 자연수 N개의 원소로 구성되어 있음
# 최대 K번의 바꿔치기 연산 가능 (A의 원소와 B의 원소 바꿔치기)
# 목표는 배열 A의 모든 원소의 합이 최대가 되도록
# e.g. A = [1,2,5,4,3] B = [5,5,6,6,5] K = 3 -> 26

def replacement_for_maximum(A,B,K):
    A.sort() # [1,2,3,4,5]
    B.sort(reverse=True) # [6,6,5,5,5]
    ans = 0
    for i in range(K):
        if A[i] < B[i]:
            A[i], B[i] = B[i], A[i]
        else:
            break
    return sum(A)


if __name__ == '__main__':
    print(selection_sort([7,5,9,0,3,1,6,2,4,8]))

    print(insertion_sort([7,5,9,0,3,1,6,2,4,8]))

    arr = [3,2,1]
    quick_sort(arr, 0, 2)
    print(arr)
    arr2 = [5,7,9,0,3,1,6,2,4,8]
    print(quick_sort_v2(arr2))

    print(count_sort([7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]))

    print("- - - - - - - - - - - - - - -")

    # 연습 문제 1) 두 배열의 원소 교체
    print(replacement_for_maximum([1,2,5,4,3],[5,5,6,6,5],3))