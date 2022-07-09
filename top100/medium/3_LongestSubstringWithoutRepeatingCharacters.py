'''
3. Longest Substring without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/solution/

Given a string s, find the length of the longest substring without repeating characters.

e.g.
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

s consists of English letters, digits, symbols and spaces.

'''


class Solution:

    # time complexity: O(n^2)
    # space complexity: O(n)
    def lengthOfLongestSubstring_v2(self, s: str) -> int:
        res = 0         # our answer (maximum length)
        seen = {}       # if char was seen during ith iterationn

        # fix start (where substring begins)
        for i,c1 in enumerate(s):
            seen[c1] = i
            length = 1
            # go further until meet already visited character
            for c2 in s[i+1:]:
                if c2 in seen and seen[c2] == i:
                    break
                seen[c2] = i
                length += 1
            # update our answer, maximum length
            res = max(res, length)
        return res

    # slide window tech
    # time complexity: O(N)
    # space complexity: O(N)
    def lengthOfLongestSubstring_v3(self, s: str) -> int:
        l = max_len = 0
        chars = set()
        for r,elem in enumerate(s):

            # shrink window until it doesn't have repeating character
            while elem in chars:
                elem.remove(s[l])
                l += 1

            chars.add(elem)
            max_len = max(r - l + 1, max_len)

        return max_len

    # s consists of English letters, digits, symbols and spaces.
    # make a list of None, a length of 128
    # value of ord of lower, upper English characters, digits, symbols and spaces
    # if the value was new, we put there index of the found position in s
    def lengthOfLongestSubstring_v4(self, s: str) -> int:
        return      
        # chars = [None] * 128
        # left = right = 0
        # while right < len(s):
        #     r = s[right]
        #     idx = chars[ord(r)]
        #     if idx != None and left

    def lengthOfLongestSubstring_v5(self, s: str) -> int:
        dicts = {}
        maxlength = start = 0
        for i,value in enumerate(s):
            if value in dicts:
                sums = dicts[value] + 1
                if sums > start:
                    start = sums
            num = i - start + 1
            if num > maxlength:
                maxlength = num
            dicts[value] = i
        return maxlength


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring('abcadbc'))
    print(Solution().lengthOfLongestSubstring_v2('abcadbc'))

    print(Solution().lengthOfLongestSubstring('abcabca'))
    print(Solution().lengthOfLongestSubstring_v2('abcabca'))

    print(Solution().lengthOfLongestSubstring('abcbbca'))
    print(Solution().lengthOfLongestSubstring_v2('abcbbca'))