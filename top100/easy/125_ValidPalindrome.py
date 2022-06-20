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

if __name__ == '__main__':
    print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
    print(Solution().isPalindrome_v2("A man, a plan, a canal: Panama"))