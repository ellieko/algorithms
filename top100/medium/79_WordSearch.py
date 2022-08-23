'''
79. Word Search
https://leetcode.com/problems/word-search/

'''

# We argue that a more accurate term to summarize the solution would be backtracking,
# which is a methodology where we mark the current path of exploration,
# if the path does not lead to a solution, we then revert the change (i.e. backtracking)
# and try another path.

class Solution:
    # time complexity: O(N*dfs) = O(N*4^L)
    # where N is the number of cells in the board and L is the length of the word to be matched

    # backtrack: call stack is the length of word, time complexity is 4^L (or 3^L)
    # For the backtracking function, initially we could have at most 4 directions to explore,
    # but further the choices are reduced into 3 (since we won't go back to where we come from)
    # As a result, the execution trace after the first step could be visualized as a 3-ary tree,
    # each of the branches represent a potential exploration in the corresponding direction.
    # Therefore, in the worst case, the total number of invocation
    # would be the number of nodes in a full 3-nary tree, which is about 3^L

    # space complexity: O(the length of the word)
    # The main consumption of the memory lies in the recursion call of the backtracking function
    # The maximum length of the call stack would be the length of the word

    def exist(self, board, word: str) -> bool:
        width = len(board[0])   # COLUMNS
        height = len(board)     # ROWS

        # if word exists starting from (i, j)
        def backtrack(i, j, idx):

            # if we are done matching word
            if idx == len(word):
                return True

            # not a valid index
            if i < 0 or i >= height or j < 0 or j >= width:
                return False

            # if it is not matching character
            #    or we already visited this character
            if board[i][j] != word[idx]:
                return False

            # to know that we've already visited the cell (i, j)
            # so that it can't be matched again
            board[i][j] = '#'

            for r, c in [(0,1), (1,0), (0,-1), (-1,0)]:
                ret = backtrack(i+r,j+c, idx+1)
                if ret: break
            
            # if there was not successful matching
            # need to revert the change
            board[i][j] = word[idx]

            return ret

        # look for starting point
        for i in range(height):
            for j in range(width):
                if backtrack(i, j, 0):
                    return True
        return False




