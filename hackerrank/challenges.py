# dynamic array

# takeaway 1) define array of n empty arrays: [[]]*2
# [2]*2 = [2,2]
# [[2]]*2 = [[2], [2]] --> [[]]*2
# [[2]*2] = [[2,2]]

# takeaway 2)
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

if __name__ == '__main__':
    dynamicArray(2,[[1,0,5],
                    [1,1,7],
                    [1,0,3],
                    [2,1,0],
                    [2,1,1]])       # should print 7, 3