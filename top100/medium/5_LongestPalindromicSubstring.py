'''

Given a string s, return the longest palindromic substring in s.

'''

class Solution:

    # Brute Force with O(n^3) -- Time Limit Exceeded
    def longestPalindrome(self, s):
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

    # reference to review
    # https://zkf85.github.io/2019/03/26/leetcode-005-longest-palindrome#solution

    # Improve the solution above (Approach 4. Expand Around Center - O(n^2))
    def longestPalindrome_v4(self, s):
        start = end = 0
        for i in range(len(s)):
            c1 = self.expendAroundCenter(s, i, i)
            c2 = self.expendAroundCenter(s, i, i+1)
            longer = max(c1, c2)
            if end - start < longer:
                start = i - (longer - 1) // 2
                end = i + longer // 2
        return s[start:end+1]

    def expendAroundCenter(self, s, left, right):
        l, r, length = left, right, len(s)
        while (0 <= l and r < length and s[l] == s[r]):
            l -= 1
            r += 1
        return r - l - 1


if __name__ == '__main__':

    print(Solution().longestPalindrome_v4('a'))
    print(Solution().longestPalindrome_v4('aacabdkacaa'))
    print(Solution().longestPalindrome_v4("flsuqzhtcahnyickkgtfnlyzwjuiwqiexthpzvcweqzeqpmqwkydhsfipcdrsjkefehhesubkirhalgnevjugfohwnlhbjfewiunlgmomxkafuuokesvfmcnvseixkkzekuinmcbmttzgsqeqbrtlwyqgiquyylaswlgfflrezaxtjobltcnpjsaslyviviosxorjsfncqirsjpkgajkfpoxxmvsyynbbovieoothpjgncfwcvpkvjcmrcuoronrfjcppbisqbzkgpnycqljpjlgeciaqrnqyxzedzkqpqsszovkgtcgxqgkflpmrikksaupukdvkzbltvefitdegnlmzeirotrfeaueqpzppnsjpspgomyezrlxsqlfcjrkglyvzvqakhtvfmeootbtbwfhqucbnuwznigoyatvkocqmbtqghybwrhmyvvuchjpvjckiryvjfxabezchynfxnpqaeampvaapgmvoylyutymdhvhqfmrlmzkhuhupizqiujpwzarnszrexpvgdmtoxvjygjpmiadzdcxtggwamkbwrkeplesupagievwsaaletcuxtpsxmbmeztcylsjxvhzrqizdmgjfyftpzpgxateopwvynljzffszkzzqgofdlwyknqfruhdkvmvrrjpijcjomnrjjubfccaypkpfokohvkqndptciqqiscvmpozlyyrwobeuazsawtimnawquogrohcrnmexiwvjxgwhmtpykqlcfacuadyhaotmmxevqwarppknoxthsmrrknu"))
