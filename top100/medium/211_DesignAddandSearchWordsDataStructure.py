'''
211. Design Add and Search Words Data Structure
https://leetcode.com/problems/design-add-and-search-words-data-structure/

Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary(): Initializes the object.
void addWord(word): Adds word to the data structure, it can be matched later.
bool search(word): Returns true if there is any string in the data structure
                   that matches word or false otherwise.
                   Word may contain dots '.' where dots can be matched with any letter.

'''

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    # time complexity: O(m) where m is the key length
    # space complexity: O(m)
    def addWord(self, word: str) -> None:
        parent = self.root
        for c in word:
            if c not in parent.children:
                parent.children[c] = TrieNode()
            parent = parent.children[c]
        parent.endOfWord = True

    # use dfs (recursion) for word having '.' cases
    # time complexity: O(m) for the "well-defined" words without dots, where M is the key length and N is a number of keys
    # and O(N*26^M) for the "undefined" words,
    # which corresponds to the worst-case situation of searching an undefined word ....(. M times)
    # which is one character longer than all inserted keys

    # space complexity: O(1) for the search of "well-defined" words w/o dots,
    # and up to O(m) for the "undefined" words, to keep the recursion stack
    def search(self, word: str) -> bool:
        
        def dfs(root, j):
            parent = root
            for i in range(j, len(word)):
                c = word[i]
                if c == '.':
                    for child in parent.children.values():
                        if dfs(child, i+1):
                            return True
                    return False
                else:
                    if c not in parent.children:
                        return False
                    parent = parent.children[c]
            return parent.endOfWord

        return dfs(self.root, 0)