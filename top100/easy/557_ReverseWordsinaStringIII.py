'''
557. Reverse Words in a String III

Given a string s, reverse the order of characters in each word
within a sentence while still preserving whitespace and initial word order.

e.g.
Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

'''

class Solution:
    def reverseWords_v1(self, s: str) -> str:
        temp = s.split()
        for i in range(len(temp)):
            word = [c for c in temp[i]]
            for j in range(len(word)//2):
                word[j], word[-j-1] = word[-j-1], word[j]
            temp[i] = "".join(word)
        return " ".join(temp)

    def reverseWords_v2(self, s: str) -> str:
        return " ".join([i[::-1] for i in s.split()])

if __name__ == '__main__':
    print(Solution().reverseWords_v1("Let's take LeetCode contest"))
    print(Solution().reverseWords_v2("Let's take LeetCode contest"))