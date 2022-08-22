'''
165. Compare Version Numbers
https://leetcode.com/problems/compare-version-numbers/

'''

class Solution:
    # 1) Split + Parse (Two Pass: one for list creation and the other for comparison)
    # time complexity: O(n+m+max(n,m)) -> O(n+m)
    # space complexity: O(n+m)
    def compareVersion_v1(self, version1: str, version2: str) -> int:
        l1 = version1.split(".")
        l2 = version2.split(".")
        for i in range(max(len(l1), len(l2))):
            v1 = int(l1[i]) if i < len(l1) else 0
            v2 = int(l2[i]) if i < len(l2) else 0
            if v1 == v2:
                continue
            return -1 if v1 < v2 else 1
        return 0


    # 2) Two Pointers (One Pass)
    # time complexity: O(max(n, m))
    # space complexity: O(1)
    def compareVersion_v2(self, version1: str, version2: str) -> int:
        p1 = p2 = 0
        n, m = len(version1), len(version2)
        while p1 < n or p2 < m:
            v1 = v2 = 0

            # read the revision number from version1
            while p1 < n and version1[p1] != '.':
                v1 = v1*10 + int(version1[p1])
                p1 += 1

            # read the revision number from version2
            while p2 < m and version2[p2] != '.':
                v2 = v2*10 + int(version2[p2])
                p2 += 1

            if v1 < v2: return -1
            if v1 > v2: return 1

            p1 += 1
            p2 += 1

        return 0

        
            