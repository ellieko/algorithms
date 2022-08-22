'''
819. Most Common Word

Given a string paragraph and a string array of the banned words banned,
return the most frequent word that is not banned.
It is guaranteed there is at least one word that is not banned, and that the answer is unique.

The words in paragraph are case-insensitive and the answer should be returned in lowercase.

'''

from collections import Counter, defaultdict
import operator
import re
from typing import List

class Solution:
    # my approach
    # time complexity: O(n+m)
    # space complexity: O(n+m)
    def mostCommonWord_v1(self, paragraph: str, banned: List[str]) -> str:
        # paragraph.lower().split(" ") but for one weird test case changed as the line below
        paragraphs = re.split(' |; |, |\,', paragraph.lower())
        count = {}
        for word in paragraphs:
            w = ''.join(filter(str.isalpha, word))
            count[w] = 1 + count.get(w, 0)
            
        ban = {word.lower() for word in banned}
        
        word, freq = None, 0
        for k, v in count.items():
            if v > freq and k not in ban:
                word, freq = k, v
        return word

    # time complexity: O(n+m)
    # where n is the number of characters in the input string
    # and m is the number of characters in the banned list
    # space complexity: O(n+m) for the hash map and set
    def mostCommonWord_v2(self, paragraph: str, banned: List[str]) -> str:
        normalized_str = ''.join([c.lower() if c.isalpha() else ' ' for c in paragraph])
        words = normalized_str.split()
        word_count = defaultdict(int)
        banned_words = set(banned)
        for word in words:                                      
            if word not in banned_words:
                word_count[word] += 1
        return max(word_count.items(), key=operator.itemgetter(1))[0]                       

        
