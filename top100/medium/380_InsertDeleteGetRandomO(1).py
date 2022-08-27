'''
380. Insert Delete GetRandom O(1)
https://leetcode.com/problems/insert-delete-getrandom-o1/

'''

import random

# hashmap and numlist (because we need list to ramdomly pick and provide one element)
# hashmap for indice of out inserted elements
# insert can be done by appending value to the list
# about remove??
# removing last element is only possible with O(1)
# so we prefer removing the last element
# -> we find the index from our value to remove from hashmap
# exchange value to remove and last value from the list
# so that the value to remove can be at the end of the list

class RandomizedSet:

    def __init__(self):
        self.numIndexMap = {}
        self.numList = []

    def insert(self, val: int) -> bool:
        res = val not in self.numIndexMap
        if res:
            self.numIndexMap[val] = len(self.numList)
            self.numList.append(val)
        return res

    def remove(self, val: int) -> bool:
        res = val in self.numIndexMap
        if res:
            idx = self.numIndexMap[val]
            lastVal = self.numList[-1]
            self.numList[idx] = lastVal
            self.numIndexMap[lastVal] = idx
            self.numList.pop()
            
            del self.numIndexMap[val]
        return res
        

    def getRandom(self) -> int:
        return random.choice(self.numList)
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()