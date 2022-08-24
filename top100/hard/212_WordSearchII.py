'''
212. Word Search II
https://leetcode.com/problems/word-search-ii/

'''

from typing import List


class Solution:
    # bruteforce solution gives us TLE
    # need to use prefix tree data structure + optimization (if word found, incrementally remove the matched leaf node)
    
    # time complexity: O(m*4*3&(l-1))
    # where m is the number of cells and l is the maximum length of words
    # space complexity: O(n)
    # where n is the total number of letters in the dictionary
    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        # initialize our prefix tree
        trie = {}
        for word in words:
            node = trie
            for letter in word:
                node = node.setdefault(letter, {})
            node['$'] = word

        m, n = len(board), len(board[0])
        res = []
        
        def backtrack(i, j, parent):
            letter = board[i][j]
            currNode = parent[letter]
            
            word_match = currNode.pop('$', False)
            if word_match:
                res.append(word_match)
            
            board[i][j] = '#'
            for r, c in (0,1), (0,-1), (1,0), (-1,0):
                nr, nc = i+r, j+c
                if nr < 0 or nc < 0 or nr >= m or nc >= n:
                    continue 
                if board[nr][nc] not in currNode:
                    continue
                backtrack(nr, nc, currNode)
            board[i][j] = letter
            
            # optimization: incrementally remove the matched leaf node in trie
            if not currNode:
                parent.pop(letter)
                
        for i in range(m):
            for j in range(n):
                # look for words starting with board[i][j]
                if board[i][j] in trie:
                    backtrack(i, j, trie)
        return res
                    
