'''
191. Number of 1 Bits

Write a function that takes an unsigned integer and returns the number of '1' bits
it has (also known as the Hamming weight).
'''


class Solution:
    # input n = 0b00000000000000000000000000001011
    # -> decimal 11
    def hammingWeight(self, n: int) -> int:
        print(bin(n))
        return len([1 for b in bin(n) if b == '1'])

    def hammingWeight_v2(self, n: int) -> int:
        ans = 0
        while n:
            ans += n % 2
            n >>= 1         # shift to right by one bit
        return ans

        # shifting to right                         shifting to left
        # 11 >> 1 --> 5 (001011 -> 000101)          11 << 1 --> 22 (001011 -> 010110)   
        # 5 >> 1  --> 2 (000101 -> 000010)          22 << 1 --> 44 (010110 -> 101100)
        # 2 >> 1  --> 1 (000010 -> 000001)          44 << 1 --> 88 (101100 -> 1011000)
        # gives half or half with one less          gives twice

if __name__ == '__main__':
    print(Solution().hammingWeight(0b00000000000000000000000000001011)) #1+2+8 = 11
    print(Solution().hammingWeight_v2(0b00000000000000000000000000001011))
