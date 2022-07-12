'''
49. Group Anagrams

'''

class Solution:
    def groupAnagrams(self, strs):
        # anagram --> sort하면 같다 but sorting takes time
        # 모든 word를 sort 시키고, 그 값을 dict에 넣을 수도 있는데
        # 그러면 time complexity가 O(N*MlogM)

        # strs[i] consists of lowercase English letters (a-z -> 26)
        # because we know there will be only 26 differenct characters at maximum

        # time complexity: O(N*M) where N is a length of strs and M is an average length of each word
        # space complexity: 
        from collections import defaultdict
        res = defaultdict(list)
        
        for word in strs:
            count = [0] * 26
            
            for c in word:
                count[ord(c) - ord('a')] += 1
                
            # count 자체를 key로 하기 때문에, key가 겁나 큼
            res[tuple(count)].append(word)      # because we cannot use list as key (python)
            
        return res.values()

if __name__ == '__main__':
    print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))