'''
You are given a large integer represented as an integer array digits,
where each digits[i] is the ith digit of the integer.
The digits are ordered from most significant to least significant in left-to-right order.
The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
'''


class Solution:

    # indexing using negative signs
    def plusOne(self, digits):
        i = -1
        while i >= -len(digits):
            if digits[i] == 9:
                digits[i] = 0
                i -= 1
            else:
                digits[i] += 1
                break
        if i < -len(digits):
            digits.insert(0, 1)
        return digits

    # indexing using positive signs
    def plusOne_v2(self, digits):
        i = len(digits) - 1
        while i >= 0:
            if digits[i] == 9:
                digits[i] = 0
                i -= 1
            else:
                digits[i] += 1
                break
        if i == -1:
            digits.insert(0, 1)
        return digits

    # shorter version (while -> for) 
    def plusOne_v3(self, digits):
        for i in range(len(digits)-1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        return [1] + digits         # digits.insert(0, 1) and return digits is faster


if __name__ =='__main__':
    print(Solution().plusOne([1,0,9]))      # [1,1,0]
    print(Solution().plusOne([9]))          # [1,0]
    print(Solution().plusOne([1,9,9]))      # [2,0,0]
    print(Solution().plusOne([9,9,9]))      # [1,0,0,0]

    print("- - - - - - - - - - - - - - - - -")

    print(Solution().plusOne_v2([1,0,9]))      # [1,1,0]
    print(Solution().plusOne_v2([9]))          # [1,0]
    print(Solution().plusOne_v2([1,9,9]))      # [2,0,0]
    print(Solution().plusOne_v2([9,9,9]))      # [1,0,0,0]

    print("- - - - - - - - - - - - - - - - -")

    print(Solution().plusOne_v3([1,0,9]))      # [1,1,0]
    print(Solution().plusOne_v3([9]))          # [1,0]
    print(Solution().plusOne_v3([1,9,9]))      # [2,0,0]
    print(Solution().plusOne_v3([9,9,9]))      # [1,0,0,0]