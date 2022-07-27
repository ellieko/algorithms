'''
125. Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
and removing all non-alphanumeric characters,
it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # l = [c for word in s.lower().split() for c in word]
        string = ''.join(filter(str.isalnum, s.lower()))
        for i in range(len(string)//2):
            if string[i] != string[-i-1]:
                return False
        return True

    def isPalindrome_v2(self, s: str) -> bool:
        filtered = filter(lambda ch: ch.isalnum(), s)
        lowercased = map(lambda ch: ch.lower(), filtered)
        new_list = list(lowercased)
        reversed_list = new_list[::-1]
        return new_list == reversed_list

    # time complexity: O(n)
    # space compelxity: O(some) for redefining s... I guess
    def isPalindrome_v3(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s.lower()))
        for i in range(len(s)//2):
            if s[i] != s[-i-1]:
                return False
        return True
    
    # can define our own isalnum function
    # use ascii values
    def myisalnum(self, c) -> bool:
        return (ord('a') <= ord(c) <= ord('z') or
                ord('A') <= ord(c) <= ord('Z') or
                ord('0') <= ord(c) <= ord('9'))

    # time complexity: O(n)
    # space complexity: O(1) - two pointers algorithm
    def isPalindrome_v4(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l < r:
            while l < r and not self.myisalnum(s[l]):
                l += 1
            while r > l and not self.myisalnum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True



if __name__ == '__main__':
    print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
    print(Solution().isPalindrome_v2("A man, a plan, a canal: Panama"))
    print(Solution().isPalindrome_v3(".,"))
    print(Solution().isPalindrome_v4(".,"))     # still works because once l gets same as r, r won't change