'''
Problem 1) Reductor Array
For two integer arraayss, the comparator value is the total number of elements in the first array
such that there exists no integer in the second array with an absolute difference less than or equal to d.
Find the comparator value

LEETCODE 1385. Find the Distance Value Between Two Arrays (Easy)
'''

# submitted code
# 3/15 tests failed to pass because time limit exceeds
# issue - time commplexity: O(N^2)
# how to break two loops... while loop judiciously?
def comparatorValue(a, b, d):
    count = 0
    for i in a:
        l = [abs(i-num) for num in b if abs(i-num) > d]
        if len(l) == len(b):
            count += 1
    return(count)

# using for loop + break - still O(N^2)
def comparatorValue_v1(a, b, d):
    count = 0
    for i in a:
        counted = True
        for j in b:
            if abs(i-j) <= d:
                counted = False
                break
        if counted:
            count +=1
    return count

# using while loop + break - stil O(N^2)
def comparatorValue_v2(a, b, d):
    count = 0
    for num in a:
        j = 0
        while j <= len(b)-1:
            if abs(num-b[j]) <= d:
                break
            j += 1
        if j == len(b):
            count += 1

    return count

# using min and max...?
def comparatorValue_v3(a, b, d):
    count = 0
    a_min, a_max = min(a), max(a)       # O(N)
    b_min, b_max = min(b), max(b)       
    return count

                
'''
    groups = {}
    counts_sorted = ((e,i) for i,e in enumerate(counts))
    counts_sorted = sorted(counts_sorted, reverse=True, key=lambda x:x[0])
    for count in counts_sorted:

        size, idx = count

        if size not in groups: #group doesn't exist
            groups[size] = [idx]
        elif len(groups[size]) < size: #exist and have space
            groups[size].append(idx)

        if len(groups[size]) == size:
            for i in groups[size]: 
                print(i, end=' ')
            print('\r')
            del groups[size]

'''


'''
Problem 2) The Social Network 
A social network has n active users, numbered from 0 to n-1.
Users selectively friend one another to create groups of friends within the network.

- Two users x and y are direct friends if they friend each other on the network.
- Two users x and z are indirect friends if there is some y common to both x and z
- Two users x and y belong to the same group if they are friends directly or indirectly.
- The numbers of people in each group is given as an array of n integers,
  counts where counts[i] denotes the total number of users in the group that the user belongs to.
- All of the users in a particular group must have minimal id numbers.

Print the information of each valid group in a new line as space separated integers in ASC order.
And groups themselves are ordered by smallest member ID in ASC order
'''

# submitted code
# only 4/15 tests passed
# (because I intended to pass the tese cases only, not fully keep in mind the whole program)
# "groups themselves are ordered by smallest member ID in ASC order" !!!!!!!
def socialGraphs(counts):
    d, s = {}, []
    for idx,num in enumerate(counts):
        d[num] = d[num] + [idx] if num in d else [idx]
    for key in d:
        for i in range(len(d[key])//key):
            s.append(d[key][i*key:i*key+key])
    s.sort()
    for p in s:
        print(*p)


        
if __name__ == '__main__':

    print(comparatorValue_v1([7,5,9],[13,1,4], 3))              # 1 ([5,6,3],[8,4,1],[4,7,5]) = "[4,7,5]"
    print(comparatorValue_v1([7,5,9],[10, 10, 10, 10],2))       # 2
    print(comparatorValue_v1([7,5,9],[10],2))                   # 2
    print(comparatorValue_v1([7],[10],2))                       # 1
    print(comparatorValue_v1([7,1,0],[10],2))                   # 3

    print(comparatorValue_v1([1,4,2,3],[-4,-3,6,10,20,30],3))   # 2

    print("- - - - - - - - - - - - - - -")


    print(socialGraphs([3,3,3,3,3,1,3]))                                           # 0 1 2
    print(socialGraphs([1,1,1]))                                     # 0           # 3 4 6
                                                                     # 1           # 5
                                                                     # 2
    print(socialGraphs([2,2,2,2]))                      # 0 1
                                                        # 2 3

    print(socialGraphs([2,3,3,3,3,3,1,3,1,1,1,2,2,2]))  # 0 11
                                                        # 1 2 3
                                                        # 4 5 7
                                                        # 6
                                                        # 8
                                                        # 9
                                                        # 10
                                                        # 12 13