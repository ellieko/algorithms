'''
17. Letter Combinations of a Phone Number
https://leetcode.com/problems/letter-combinations-of-a-phone-number/

Given a string containing digits from 2-9 inclusive,
return all possible letter combinations that the number could represent.
Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.

e.g.
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

'''

# Backtracking Problem
# because 0 <= digits.length <= 4
# Time Complexity: O(4^N * N) where N is the length of digits.
# Note that 4 in this expression is referring to the maximum value length in the hash map,
# and not to the length of the input.

class Solution:

    # recursion (backtrack)
    # time complexity: O(4^n) where n is the length of digits
    # space complexity: O(n) not counting space used for the output,
    #                   the extra space we use relative to input size is the space occupied by the recursion call stack
    def letterCombinations_v1(self, digits):
        res = []
        digitToChar = { "2" : "abc", "3" : "def", "4" : "ghi", "5" : "jkl",
                        "6" : "mno", "7" : "pqrs", "8" : "tuv", "9" : "wxyz" }
    
        def backtrack(idx, curStr):
            if idx == len(digits):
                res.append(curStr)
                return
            for c in digitToChar[digits[idx]]:
                backtrack(idx+1, curStr+c)

        if digits:
            backtrack(0, "")
        return res

    # bfs
    # time complexity: O(4^n) where n is the length of digits
    # space complexity: O(4^n)
    def letterCombinations_v2(self, digits):
        from collections import deque
        res = []
        digitToChar = { "2" : "abc", "3" : "def", "4" : "ghi", "5" : "jkl",
                        "6" : "mno", "7" : "pqrs", "8" : "tuv", "9" : "wxyz" }
        q = deque([""])
        while digits and q:
            s = q.popleft()
            if len(s) == len(digits):
                res.append(s)
            else:
                for c in digitToChar[digits[len(s)]]:
                    q.append(s + c)
        return res




if __name__ == '__main__':
    print(Solution().letterCombinations("23"))
