'''

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
    def letterCombinations(self, digits):
        if len(digits) == 0:
            return []
        letters = { "2" : "abc", "3" : "def", "4" : "ghi", "5" : "jkl", "6" : "mno", "7" : "pqrs", "8" : "tuv", "9" : "wxyz" }
    
        def backtrack(index, path):
            if len(path) == len(digits):
                combinations.append("".join(path))
                return
            possible_letters = letters[digits[index]]
            for letter in possible_letters:
                path.append(letter)
                backtrack(index+1, path)
                path.pop()

        combinations = []
        backtrack(0, [])
        return combinations


if __name__ == '__main__':
    print(Solution().letterCombinations("23"))
