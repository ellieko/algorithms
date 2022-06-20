'''
67. Add Binary
Given two binary strings a and b, return their sum as a binary string.

'''

class Solution:

    # approach 1)
    # convert bin to int --> int(BIN, 2)
    # convert int to bin --> bin(INT) or f"{INT:b}" 
    def addBinary(self, a: str, b: str) -> str:
        # return str(bin(int(a,2)+int(b,2)))[2:] - because it gives us '0b****'
        return '{0:b}'.format(int(a,2)+int(b,2))

    # approach 2) using carry
    def addBinary_v2(self, a:str, b: str) -> str:
        n = max(len(a), len(b))
        a, b = a.zfill(n), b.zfill(n)       # zfill adds '0' to the beginning of the string until n
        carry, ans = 0, ''
        for i in range(n-1, -1, -1):
            if a[i] == '1':
                carry += 1
            if b[i] == '1':
                carry += 1
            
            # carry can be 0, 1, 2, 3 
            if carry % 2 == 1:          # if carry is 1 or 3
                ans = '1' + ans
            else:                       # if carry is 0 or 2
                ans = '0' + ans
            
            # keep carry if it was 2 or 3 (that needs to be checked on next round)
            # carry = carry // 2
            carry //= 2  

        if carry == 1:
            ans = '1' + ans

        return ans
        
if __name__ == '__main__':
    print(Solution().addBinary_v2('11','1'))
