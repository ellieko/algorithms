'''
PROBLEM) Fraudulent Activity Notifications
https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting

'''

# counting sort review
def count_sort(arr):
    index = [0] * (max(arr)+1)
    for elem in arr:
        index[elem] += 1
    return [idx for idx, count in enumerate(index) for i in range(count) ]
    # return sum([[item]*count for item, count in enumerate(index)],[])

# tried multiple source codes but all of them fails to pass a few test cases due to the limited time
# tried using queue data structure and bisect module , ...
def activityNotifications(expenditure, d):
    from collections import deque
    if len(expenditure) <= d:
        return 0
    count, temp = 0, deque(expenditure[:d])
    for i in range(d, len(expenditure)):
        t = [0]*(max(temp)+1)
        for elem in temp:
            t[elem] += 1
        t = [idx for idx, count in enumerate(t) for i in range(count)]
        cp = t[d//2-1] + t[d//2] if d//2 == 0 else 2*t[d//2]
        if expenditure[i] >= cp:
            count +=1
        temp.popleft()
        temp.append(expenditure[i])
    return count

# from stackoverflow (link below), passes all test cases
# https://stackoverflow.com/questions/58257308/timeout-error-in-fraudulent-activity-notification-hackerrank/63227912#63227912?newreg=03d908cbdd6c4128b3d956ac8940797c

# since possible max value is 200,
# we use counting algorithm
# we update only window of length d
# find a median from that window from counting algorithm
# so it doesn't have to sort/remove every time
# since n can be enormously big, we use comparatively smaller expenditure value
def findMedian_stackoverflow(counter, d):
    count = 0
    median = 0
    if d%2 != 0:
        for i in range(len(counter)):
            count += counter[i]
            if count > d//2:
                median = i
                break
    else:
        first = 0
        second = 0
        for i, _ in enumerate(counter):
            count += counter[i]  
            if first == 0 and count >= d//2:
                first = i        
            if second == 0 and count >= d//2 + 1:
                second = i
                break  
        median = (first+second) / 2 
    return median

def activityNotifications_stackoverflow(expenditure, d):
    count = 0
    counter = [0]*201
    for exp in range(d):
        counter[expenditure[exp]] += 1
    for i in range(d, len(expenditure)):
        new = expenditure[i]
        old = expenditure[i-d]
        median = findMedian_stackoverflow(counter, d)
        if new >= 2*median:
            count += 1  
        counter[old] -= 1
        counter[new] += 1
    return count



'''
PROBLEM) Merge Sort: Counting Inversions
'''

# reimplementation: quick sort
# average: O(nlogn), worst: O(n^2)
def quick_sort_v1(arr, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        if left <= end and arr[left] <= arr[pivot]:
            left += 1
        if 0 < right and arr[pivot] < arr[right]:
            right -= 1
        if left > right:
            arr[pivot], arr[right] = arr[right], arr[pivot]
        else:
            arr[left], arr[right] = arr[right], arr[left]
    quick_sort_v1(arr, start, right-1)
    quick_sort_v1(arr, right+1, end)

def quick_sort_v2(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    tail = arr[1:]
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort_v2(left_side) + [pivot] + quick_sort_v2(right_side)

# reimplementation: merge sort - like quick sort, divide and conquer
# θ(nlogn) in all 3 cases (worst, average and best)
def merge_sort(arr):
    if len(arr) <= 1: 
        return 
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    merge_sort(left)
    merge_sort(right)
    return merge_two_sorted_lists(arr, left, right)

def merge_two_sorted_lists(arr, left, right):
    l_len, r_len = len(left), len(right)
    i = j = k = 0
    while i < l_len and j < r_len:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < l_len:
        arr[k] = left[i]
        i += 1
        k += 1

    while j < r_len:
        arr[k] = right[j]
        j += 1
        k += 1


# initial trial - fails to pass 9/15 test cases due to timeout
def countInversions(arr):
    count = 0
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                count += 1
                arr[j], arr[j-1] = arr[j-1], arr[j]
    return count

# second trial - wrong answers lol
def countInversions_v2(arr):
    count = 0 
    def merge_two_sorted_lists_2(arr, left, right):
        nonlocal count
        l_len, r_len = len(left), len(right)
        i = j = k = 0
        while i < l_len and j < r_len:
            temp = arr[k]
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            if temp != arr[k]:
                count += 1
            k += 1
        while i < l_len:
            temp = arr[k]
            arr[k] = left[i]
            i += 1
            k += 1
        while j < r_len:
            temp = arr[k]
            arr[k] = right[j]
            j += 1
            k += 1
            
    def merge(arr):
        if len(arr) <= 1:
            return
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        merge(left)
        merge(right)
        return merge_two_sorted_lists_2(arr, left, right)
    merge(arr)
    
    return count

if __name__ == '__main__':
    print(count_sort([7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]))      
    print(activityNotifications([2,3,4,2,3,6,8,4,5], 5))    # 2

    # to understand stackoverflow code

    # suppose d = 3, our window is [3,1,5], median is 3
    # then our counter should be [0,1,0,1,0,1,0,0, ...]
    print(findMedian_stackoverflow([0,1,0,1,0,1,0,0],3))

    # suppose d = 4, our window is [3,1,5,7], median is (3+5)/2 = 4.0
    # then our counter should be [0,1,0,1,0,1,0,1,0,0, ...]
    print(findMedian_stackoverflow([0,1,0,1,0,1,0,1,0,0],4))

    print("- - - - - - - - - - - - - - -")

    # quick sort
    arr = [5,7,9,0,3,1,6,2,4,8]
    quick_sort_v1(arr, 0, 9)
    print(arr)

    print(quick_sort_v2([5,7,9,0,3,1,6,2,4,8]))

    print("- - - - - - - - - - - - - - -")

    # merge sort
    l = [10, 3, 15, 7, 8, 23, 98, 29]
    merge_sort(l)
    print(l)

    # second trial
    print(countInversions([2,1,3,1,2]))     # 4
    print(countInversions_v2([2,1,3,1,2]))  # 4 but get 9 or 5