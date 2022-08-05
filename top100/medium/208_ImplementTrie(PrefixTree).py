'''
208. Implement Trie (Prefix Tree)
https://leetcode.com/problems/implement-trie-prefix-tree/

A trie (pronounced as "try") or prefix tree is a tree data structure
used to efficiently store and retrieve keys in a dataset of strings.
There are various applications of this data structure, such as autocomplete and spellchecker.

'''

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

    # children['a'] = TreeNode()
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    # time complexity: O(m) where m is the key length
    # space complexity: O(m)
    # In the worst case newly inserted key doesn't share a prefix with the the keys already inserted in the trie.
    # We have to add mm new nodes, which takes us O(m) space
    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True
    
    # time complexity: O(m) where m is the key length
    # space complexity: O(1)
    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        
        return cur.endOfWord
    
    # time complexity: O(m) where m is the key length
    # space complexity: O(1)
    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True
            
            
        

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

# my first approach using set
# class Trie:

#     def __init__(self):
#         self.trie = set()
        
#     def insert(self, word: str) -> None:
#         self.trie.add(word)

#     def search(self, word: str) -> bool:
#         if word in self.trie:
#             return True
#         return False  

#     def startsWith(self, prefix: str) -> bool:
#         for word in self.trie:
#             if len(word) >= len(prefix) and prefix == word[:len(prefix)]:
#                 return True
#         return False

# my second approach using Tree but not neat for a few reasons
# it uses two extra spaces to keep strings
# need to retrieve node using its value

# class TreeNode:
#     def __init__(self, c):
#         self.val = c
#         self.children = set()       # set of TreeNodes
#         self.child_values = set()   # set of characters 
        
#     def getChildNode(self, c):      # -> TreeNode
#         for word in self.children:
#             if word.val == c:
#                 return word
        
# class Trie:
#     def __init__(self):
#         self.root = TreeNode(-1)
        
#     def insert(self, word: str) -> None:
#         parent = self.root
        
#         for i in range(len(word)):
#             # print(f"{i}th parent's child_values: {parent.child_values}")
#             if word[i] in parent.child_values:
#                 parent = parent.getChildNode(word[i])
#             else:
#                 parent.child_values.add(word[i])
#                 new = TreeNode(word[i])
#                 parent.children.add(new)
#                 parent = new
                
#         parent.child_values.add(None) # end of the word
            
#     def search(self, word: str) -> bool:
#         parent = self.root
#         for i in range(len(word)):
#             if word[i] not in parent.child_values:
#                 return False
#             parent = parent.getChildNode(word[i])
            
#         return None in parent.child_values
    

#     def startsWith(self, prefix: str) -> bool:
#         parent = self.root
#         for i in range(len(prefix)):
#             if prefix[i] not in parent.child_values:
#                 return False
#             parent = parent.getChildNode(prefix[i])
#         return True