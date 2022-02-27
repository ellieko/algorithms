'''
PROBLEM) SHERLOCK AND ANAGRAMS
Two strings are anagrams of each other if the letters of one string can be rearranged to form the other string.
Given a string, find the number of pairs of substrings of the string that are anagrams of each other.

'''
# all substrings of string s
# all_subs = [s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1)]
# all_subs = [s[i:j] for i, j in combinations(range(len(s)+1), 2)]

# all substrings of s of which length is K
# l = [subs for subs in all_subs if len(subs) == K]

from itertools import combinations

def sherlockAndAnagrams(s):
    # all substrings
    count = 0
    all_subs = [s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1)]
    for i in range(1, len(s)):
        # list of substrings of which length is i (1...len(s)-1)
        bylength = [subs for subs in all_subs if len(subs) == i]
        for idx, s in enumerate(bylength):
            bylength[idx] = {c:s.count(c) for c in s}
        for a,b in combinations(bylength, 2):
            if a == b:
                count +=1
    return count 

if __name__ == '__main__':
    print(sherlockAndAnagrams('kkkk'))        # 10
    print(sherlockAndAnagrams('mom'))         # 2
    print(sherlockAndAnagrams('abba'))        # 4
    print(sherlockAndAnagrams('abcd'))        # 0
    print(sherlockAndAnagrams('ifailuhkqq'))  # 3
    