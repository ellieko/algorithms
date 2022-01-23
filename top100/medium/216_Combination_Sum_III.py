'''

Find all valid combinations of k numbers that sum up to n
such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations.
The list must not contain the same combination twice,
and the combinations may be returned in any order.

e.g.
Input: k = 3, n = 7
Output: [[1,2,4]]

e.g
Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]

'''

# backtracking is a general algorithm for finding
# all (or some) solutions to some computational problems.
# The idea is that it incrementally builds candidates to the solutions,
# and abandons a candidate ("backtrack") as soon as
# it determines that this candidate cannot lead to a final solution.

class Solution:
    def combinationSum3(self, k, n):
        def backtrack(remain, l, next_start):
            if remain == 0 and len(l) == k:
                # need to make a copy of current combination, list(l)
                # cuz the list object are essentially passed as reference in Python and Java
                # otherwise the combination would be reverted in other branch of backtracking.
                combinations.append(list(l)) 
                return
            elif remain < 0 or len(l) == k:
                return
            for num in range(next_start, 10):
                l.append(num)
                backtrack(remain - num, l, num + 1)
                l.pop()

        combinations = []
        backtrack(n, [], 1)
        return combinations

if __name__ == '__main__':
    print(Solution().combinationSum3(3,9))