'''
48. Rotate Image
https://leetcode.com/problems/rotate-image/

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.

'''

from typing import List


class Solution:
    # time complexity: O(n^2)
    # space complexity: O(1)
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix) - 1
        while l < r:
            top, bottom = l, r
            for i in range(r - l):

                # save topLeft value
                topLeft = matrix[top][l+i]

                # move bottomLeft value to topLeft
                matrix[top][l+i] = matrix[bottom-i][l]

                # move bottomRight value to bottomLeft
                matrix[bottom-i][l] = matrix[bottom][r-i]

                # move topRight value to bottomRight
                matrix[bottom][r-i] = matrix[top+i][r]

                # move topLeft value to topRight
                matrix[top+i][r] = topLeft
            
            l += 1
            r -= 1 