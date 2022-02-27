from re import A


def hourglassSum(arr):
    # (1,1) (1,2) (1,3) (1,4)
    # (2,1) (2,2) (2,3) (2,4)
    # (3,1) (3,2) (3,3) (3,4)
    # (4,1) (4,2) (4,3) (4,4)
    ans = None
    for i in range(1,5):
        for j in range(1,5):
            total = arr[i][j] + arr[i-1][j] + arr[i+1][j]
            total = total + arr[i-1][j-1] + arr[i-1][j+1]
            total = total + arr[i+1][j-1] + arr[i+1][j+1]
            if ans == None or ans < total:
                ans = total
    return ans

# the reason I got it wrong
# int 0: False -> when you use initially defined to None variable(var) that can be possibly 0 later
#                 you can not use conditional "not var" for the case not defined yet
#                 because if its value is zero, it gets misleaded (defined but recognize non-defined)


'''
PROBLEM) NEW YEAR CHAOS

It is New Year's Day and people are in line for the Wonderland rollercoaster ride.
Each person wears a sticker indicating their initial position in the queue from 1 to n.
Any person can bribe the person directly in front of them to swap positions,
but they still wear their original sticker. One person can bribe at most two others.

"Determine the minimum number of bribes that took place to get to a given queue order."
Print the number of bribes, or, if anyone has bribed more than two people, print Too chaotic.

e.g) q = [1,2,3,5,4,6,7,8] -> 1
     q = [4,1,2,3] -> Too chaotic.

input: int q[n]: the positions of the people after all bribes
return: No value is returned, print the minimum number of bribes necessary or Too chaotic

'''

# 1 2 5 3 7 8 6 4 - 1
# 1 2 3 5 7 8 6 4 - 2
# 1 2 3 5 6 7 8 4 
# insertion sort
def minimumBribes(q):
    num = 0
    for idx, pos in enumerate(q):
        if pos - idx - 1 >= 3:
            print('Too chaotic')
            return
    for i in range(1, len(q)):
        for j in range(i, 0, -1):
            if q[j] < q[j-1]:
                q[j], q[j-1] = q[j-1], q[j]
                num += 1
            else:
                break
    print(num)

def minimumBribes_v2(q):
    num = 0
    queue = [pos - 1 for pos in q]
    for idx, pos in enumerate(queue):
        if pos - idx > 2:
            print('Too chaotic')
            return
        for j in range(idx, 0, -1):
            if queue[j] < queue[j-1]:
                queue[j], queue[j-1] = queue[j-1], queue[j]
                num += 1
            else:
                break
    print(num)



'''
PROBLEM) MINIMUM SWAPS 2
Find the minimum number of swaps required to sort the array in ascending order.
'''
def minimumSwaps(arr):
    count = 0
    i = 0
    while i < len(arr):
        if arr[i] == i+1:
            i += 1
        else:
            temp = arr[i]
            arr[i] = arr[temp-1]
            arr[temp-1] = temp
            count += 1
    return count


    

if __name__ == '__main__':

    print("- - - - - - - - - - - - - - -")

    # POBLEM. hourglassSum
    arr = [[-1, 1, -1, 0, 0, 0],
           [0, -1, 0, 0, 0, 0],
           [-1, -1, -1, 0, 0, 0],
           [0, -9, 2, -4, -4, 0],
           [-7, 0, 0, -2, 0, 0],
           [0, 0, -1, -2, -4, 0]]
    print(hourglassSum(arr))

    print("- - - - - - - - - - - - - - -")

    # POBLEM. minimumBribes
    minimumBribes([2,1,5,3,4])    # 3
    minimumBribes([5,1,2,3,7,8,6,4])  # Too chaotic 
    minimumBribes([1,2,5,3,7,8,6,4])  # 7

    minimumBribes_v2([2,1,5,3,4])    # 3
    minimumBribes_v2([5,1,2,3,7,8,6,4])  # Too chaotic 
    minimumBribes_v2([1,2,5,3,7,8,6,4])  # 7

    print("- - - - - - - - - - - - - - -") 

    print(minimumSwaps([7,1,3,2,4,5,6]))    # 5
    print(minimumSwaps([2,3,4,1,5]))        # 3
    print(minimumSwaps([1,3,5,2,4,6,7]))    # 3
    print(minimumSwaps([4,3,1,2]))          # 3