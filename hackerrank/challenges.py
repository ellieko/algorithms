# [Dynamic Array]

# takeaway 1) define array of n empty arrays: [[]]*2
# [2]*2 = [2,2]
# [[2]]*2 = [[2], [2]] --> [[]]*2
# [[2]*2] = [[2,2]]

# takeaway 2) define variable with *, setting them same memory address
# l = [[2]]*2
# l[0].apapend(10) --> l = [[2, 10], [2, 10]]
# l = [[2],[2]]
# l[0].append(10) --> l = [[2, 10], [2]]

# conclusion !!!!
# l = [[] for i in range(n)]

def dynamicArray(n, queries):
    arr = [[] for i in range(n)]
    lastAnswer = 0
    for row in queries:
        idx = (row[1]^lastAnswer)%n
        if row[0] == 1:
            arr[idx].append(row[2])
        else:
            lastAnswer = arr[idx][row[2]%len(arr[idx])]
            print(lastAnswer)



# [Array Manipulation]
# add the values of k(3rd position of the query)
# between indices a(1st position of the query) and b(2nd position of the query) inclusive
# and find the max value

# e.g. n = 10
#      queries = [[1,5,3], [4,8,7], [6,9,1]]
#      a b k      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#      1 5 3      [3, 3, 3, 3, 3, 0, 0, 0, 0, 0]
#      4 8 7      [3, 3, 3,10,10, 7, 7, 7, 0, 0]
#      6 9 1      [3, 3, 3,10,10, 8, 8, 8, 1, 0]
# ---> the largest value is "10"

# passed only 8/15 test cases (runtime error for other 7 test cases)
# due to the time complexity O(n*m)

def arrayManipulation(n, queries):
    d = {i:0 for i in range(1, n+1)}
    m = 0
    for a,b,k in queries:
        for i in range(a, b+1):
            d[i] += k
            if m < d[i]:
                m = d[i]
    return m

# e.g. n = 10
#      queries = [[1,5,3], [4,8,7], [6,9,1]]
#      a b k      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#      1 5 3      [3, 3, 3, 3, 3, 0, 0, 0, 0, 0]  ---  [ 3  0  0  0  -3  0  0  0  0  0]
#      4 8 7      [3, 3, 3,10,10, 7, 7, 7, 0, 0]  ---  [ 3  0  0  7  -3  0  0 -7  0  0]
#      6 9 1      [3, 3, 3,10,10, 8, 8, 8, 1, 0]  ---  [ 3  0  0  7  -3  1  0 -7 -1  0] 

def arrayManipulation(n, queries):
    q = 0
    def help(q):
        q == len(queries)


if __name__ == '__main__':

    dynamicArray(2,[[1,0,5],
                    [1,1,7],
                    [1,0,3],
                    [2,1,0],
                    [2,1,1]])       # should print 7, 3

    