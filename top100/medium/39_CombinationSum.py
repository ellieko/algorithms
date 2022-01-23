'''

Given an array of distinct integers candidates and a target integer target,
return a list of all unique combinations of candidates where the chosen numbers sum to target.
You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times.
Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target
is less than 150 combinations for the given input.

e.g.
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]

'''

# 'break' is used to end loops while 'return' is used to end a function (and return a value)
# 'continue' is used to proceed to next iteration w/o completing the current one

from itertools import combinations


class Solution:
    # return type is List[List[int]]
    # stuck at getting only unique combinations ...
    # 'track' (dictionary which keeps tracking of counts of used candidate) is being shared ...
    def combinationSum(self, candidates, target):
        # the backtracking algorithm is unfolded as a Depth-First-Search tree traversal
        def backtrack(l, sum, track):
            if sum == target and track not in count_track:
                combinations.append(l)
                count_track.append(dict(track))
                # print(f"combinations: {combinations}")
                # print(f"count_track: {count_track}")
                return
            for num in candidates:
                if sum + num > target:
                    continue # shouldn't be break/return, should be continue
                             # because 'candidates' are not sorted
                track[num] = track[num] + 1
                backtrack(l + [num], sum + num, track)
                track[num] = track[num] - 1

        # should not assign variables with '=' for the reason
        # they start with the same value, []
        # combinations = count_track = [] --> NO !!!!
        # the above assignment leads to l(combination) and track
        # to be added both combinations and count_track
        combinations, count_track = [], []
        backtrack([], 0, {n:0 for n in candidates})
        return combinations

    # updated solution with LeetCode
    # having dictionary to track the number of candidates being used
    # --> choose next number in order (to make combinations only have unique ones)

    # An important detail on choosing the next number for the combination is
    # that we select the candidates in order, where the total candidates are treated as a list.
    # Once a candidate is added into the current combination,
    # we will not look back to all the previous candidates in the next explorations.

    # much faster

    # N: the number of candidates, T: the target value, M: the minimal value among the candidates
    # Time Complexity: O(N^(T/M+1))
    def combinationSum_v2(self, candidates, target):
        def backtrack(remain, comb, start):
            if remain == 0:
                combinations.append(comb)
                return
            elif remain < 0:
                return
            else:
                for i in range(start, len(candidates)):
                    backtrack(remain - candidates[i], comb + [candidates[i]], i)

        combinations = []
        backtrack(target, [], 0)
        return combinations

if __name__ == '__main__':
    print(Solution().combinationSum_v2([2,3,6,7], 7))
    print(Solution().combinationSum_v2([2,7,6,3,5,1],9))
