'''
22. Generate Parentheses
https://leetcode.com/problems/generate-parentheses/

Given n pairs of parentheses,
write a function to generate all combinations of well-formed parentheses.

e.g.
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

e.g.
Input: n = 1
Output: ["()"]

'''


class Solution:

    # Bruteforce - find all possible parenthesis and then checking if it is valid
    # Time Complexity - O(2^(2n)*n)
    # For each of 2^(2n) sequences, we need to create and validate the sequence,
    # which takes O(n) work.
    def generateParenthesis(self, n):

        def generateAll(index, sofar):
            if index == n*2:
                s = "".join(sofar)
                if self.isValidParen(s):
                    combinations.append(s)
                return
            else:
                generateAll(index+1, sofar + ['('])
                generateAll(index+1, sofar + [')'])

        combinations = [] 
        generateAll(0, [])
        return combinations
    
    def isValidParen(self, s):
        balance = 0
        for chr in s:
            if chr == '(':
                balance += 1
            else:
                balance -= 1
                if balance < 0:
                    return False
        return balance == 0


    # Backtracking - add parens only when we know it will remain a valid sequence
    # By keeping track of the number of opening and closing brackets we have placed so far
    # time complexity: ... 
    # space complexity: ...
    def generateParenthesis_v2(self, n):
        res = []
        
        def backtrack(curr, openCount, closedCount):
            if openCount == n and closedCount == n:
                res.append(curr)
                return
            
            if openCount < n:
                backtrack(curr + '(', openCount + 1, closedCount)
            if closedCount < openCount:
                backtrack(curr + ')', openCount, closedCount + 1)
        
        backtrack("", 0, 0)
        return res


if __name__ == '__main__':

    print(Solution().isValidParen("()()()"))
    print(Solution().isValidParen("((()))"))
    print(Solution().isValidParen("(())()"))
    print(Solution().isValidParen("(())((")) 

    print(Solution().generateParenthesis(1))    # ["()"]
    print(Solution().generateParenthesis_v2(1))    # ["()"]
    print(Solution().generateParenthesis(3))    # ["((()))","(()())","(())()","()(())","()()()"]
    print(Solution().generateParenthesis_v2(3))    # ["((()))","(()())","(())()","()(())","()()()"]