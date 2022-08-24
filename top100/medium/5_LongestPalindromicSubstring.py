'''
5. Longest Palindromic Substring
https://leetcode.com/problems/longest-palindromic-substring/

Given a string s, return the longest palindromic substring in s.

'''

class Solution:
    
    # time complexity: O(n^2)
    # because expanding a palindrome around its center could take O(n) time

    # space complexity: O(1)
    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        
        # center of our substring
        for i in range(len(s)):
            
            # odd number of substring
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > end - start + 1:
                    start, end = l, r
                l -= 1
                r += 1
            
            # even number of substring
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > end - start + 1:
                    start, end = l, r
                l -= 1
                r += 1
                
        return s[start:end+1]

    # Brute Force with O(n^3) -- Time Limit Exceeded
    def longestPalindrome_v1(self, s):
        ans = s[0]
        hash = {}

        for i in range(len(s)-1):
            hash[(i, i+1)] = True if s[i] == s[i+1] else False

        for i in range(len(s)-2):
            hash[(i, i+2)] = True if s[i] == s[i+2] else False
        
        for i in range(len(s)-1):
            for j in range(i+1,len(s)):
                if (i,j) not in hash:
                    self.isPalindrome(s, (i,j), hash)
                if hash[(i,j)] and len(ans) < (j-i+1):
                    ans = s[i:j+1]
        return ans

    def isPalindrome(self, s, tuple, hash):
        (i, j) = tuple
        if (i+1, j-1) not in hash:
            self.isPalindrome(s, (i+1, j-1), hash)
        hash[(i, j)] = True if hash[(i+1, j-1)] and s[i] == s[j] else False


    # A palindrome is a word, number, phrase, or other sequence of characters
    # which reads the same backward as forward
    # Improve the solution above (Approach 4. Expand Around Center)
    # time complexity: O(n^2)
    # space complexity: O(1)
    def longestPalindrome_v2(self, s):
        n = len(s)
        res, res_length = "", 0

        for i in range(n):
            # odd length palindrome
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                if r-l+1 > res_length:
                    res_length = r-l+1
                    res = s[l:r+1]
                l -= 1
                r += 1

            # even length palindrome
            l, r = i, i+1
            while l >= 0 and r < n and s[l] == s[r]:
                if r-l+1 > res_length:
                    res_length = r-l+1
                    res = s[l:r+1]
                l -= 1
                r += 1

        return res


if __name__ == '__main__':

    print(Solution().longestPalindrome_v4('a'))
    print(Solution().longestPalindrome_v4('aacabdkacaa'))
    print(Solution().longestPalindrome_v4("flsuqzhtcahnyickkgtfnlyzwjuiwqiexthpzvcweqzeqpmqwkydhsfipcdrsjkefehhesubkirhalgnevjugfohwnlhbjfewiunlgmomxkafuuokesvfmcnvseixkkzekuinmcbmttzgsqeqbrtlwyqgiquyylaswlgfflrezaxtjobltcnpjsaslyviviosxorjsfncqirsjpkgajkfpoxxmvsyynbbovieoothpjgncfwcvpkvjcmrcuoronrfjcppbisqbzkgpnycqljpjlgeciaqrnqyxzedzkqpqsszovkgtcgxqgkflpmrikksaupukdvkzbltvefitdegnlmzeirotrfeaueqpzppnsjpspgomyezrlxsqlfcjrkglyvzvqakhtvfmeootbtbwfhqucbnuwznigoyatvkocqmbtqghybwrhmyvvuchjpvjckiryvjfxabezchynfxnpqaeampvaapgmvoylyutymdhvhqfmrlmzkhuhupizqiujpwzarnszrexpvgdmtoxvjygjpmiadzdcxtggwamkbwrkeplesupagievwsaaletcuxtpsxmbmeztcylsjxvhzrqizdmgjfyftpzpgxateopwvynljzffszkzzqgofdlwyknqfruhdkvmvrrjpijcjomnrjjubfccaypkpfokohvkqndptciqqiscvmpozlyyrwobeuazsawtimnawquogrohcrnmexiwvjxgwhmtpykqlcfacuadyhaotmmxevqwarppknoxthsmrrknu"))
