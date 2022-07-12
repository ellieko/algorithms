'''
79. Word Search
https://leetcode.com/problems/word-search/

'''

class Solution:
    # time complexity: O(N*3^L) where N is the number of cell, L is the length of the word to be matched
    # 3 because we cannot go back to where we come from, so only 3 choices to go

    # space complexity: O(L) where L is the length of the word to be matched 
    # the main consumpition of the memory lies in the recursion call of the backtracking function
    # the maximum length of the call stack would be the length of the word
    # therefore, the space complexity of the algorithm is O(L)

    def exist(self, board, word: str) -> bool:
        
        self.width = len(board[0])   # COLUMNS
        self.height = len(board)     # ROWS
        self.board = board

        # look for starting point
        for i in range(self.height):
            for j in range(self.width):
                # visited = [[0]*width]*height
                # --> with this defintion of visited, if you visited[0][0] = 1, every 0th element in each row changed to 1
                if self.backtrack(i, j, word):
                    return True
        return False

    # if word exists starting from (i, j)
    def backtrack(self, i, j, word):

        # if we are done matching word
        if len(word) < 1:
            return True

        # not a valid index
        if i < 0 or i >= self.height or j < 0 or j >= self.width:
            return False

        # if it is not matching character
        #    or we already visited this character
        if (self.board[i][j] != word[0]):
            return False

        # to know that we've visited the cell (i,j)
        # so that it can't be matched again
        self.board[i][j] = '#'

        for r, c in [(0,1), (1,0), (0,-1), (-1,0)]:
            if self.backtrack(i+r,j+c, word[1:]):
                return True
        
        # if there was not successful matching
        # need to revert the change
        self.board[i][j] = word[0]

        # Tried all directions, and did not find any match
        return False

        
    


if __name__ == '__main__':
    print(Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))      # True

    print(Solution().exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCESEEEFS"))  # True
    # visited updated... has to keep the previous visited if there's no way to get the word from the position
    # have to go back...
    # didn't know how to revert the change!!!! (BACKTRACKING)