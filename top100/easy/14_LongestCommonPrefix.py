# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

class Solution:
    def longestCommonPrefix(self, strs) -> str:
        # set prefix first word of the given string list
        prefix = strs[0]
        for i in range(1, len(strs)):
            temp = ""
            for j in range(len(strs[i])):
                if j < len(prefix) and prefix[j] == strs[i][j]:
                    temp += prefix[j]
                else:
                    break
            prefix = temp
        return prefix
