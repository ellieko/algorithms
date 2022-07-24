'''
240. Search a 2D Matrix II

'''

class Solution:
    # brute force
    # time complexity: O(NM)
    # space complexity: O(1)
    def searchMatrix_v1(self, matrix, target: int) -> bool:
        for row in matrix:
            if target in row:
                return True
        return False

    # binary search
    # time complexity: O(NlogN)
    # space complexity: O(1)
    def searchMatrix_v2(self, matrix, target: int) -> bool:
        def binary_search(start, vertical):
            lo, hi = 0, len(matrix)-1 if vertical else len(matrix[0])-1
            while lo <= hi:
                mid = (lo+hi)//2
                if vertical:
                    if matrix[mid][start] == target:
                        return True
                    elif matrix[mid][start] < target:
                        lo = mid + 1
                    else:
                        hi = mid - 1
                else:
                    if matrix[start][mid] == target:
                        return True
                    elif matrix[start][mid] < target:
                        lo = mid + 1
                    else:
                        hi = mid - 1
            return False
                    
        if not matrix:
            return False
        for i in range(min(len(matrix), len(matrix[0]))):
            vertical_found = binary_search(i, True)
            horizontal_found = binary_search(i, False)
            if vertical_found or horizontal_found:
                return True
        return False

    # Search Space Reduction
    # time complexity: O(N+M)
    # space complexity: O(1)
    def searchMatrix_v3(self, matrix, target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        
        row, col = len(matrix)-1, 0
        
        while row >= 0 and col < len(matrix[0]):
            print(f"matrix value at {row},{col} is {matrix[row][col]}")
        
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                row -= 1
            else:
                col += 1
        
        return False
                
        
                
    
            
                
        
                
            
                
        