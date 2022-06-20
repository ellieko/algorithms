'''
118. Pascal's Triangle

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
    1
   1,1
  1,2,1
 1,3,3,1
1,4,6,4,1

'''

class Solution:
    def generate(self, numRows):
        ans = []
        for i in range(numRows):     
            temp = [None for j in range(i+1)]  
            temp[0], temp[-1] = 1, 1
            for j in range(1, i):
                temp[j] = ans[i-1][j-1] + ans[i-1][j]
            ans.append(temp)
        return ans

if __name__ == '__main__':
    print(Solution().generate(5))