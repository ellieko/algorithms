'''
895. Maximum Frequency Stack
https://leetcode.com/problems/maximum-frequency-stack/

'''

class FreqStack:

    # stack of stacks
    # time complexity for push and pop: O(1)
    # space complexity: O(n) where n is the number of elements in FreqStack
    def __init__(self):
        # map for the count of each variable
        
        self.freq = {}                  # {value: count}
        
        # stack of stacks (index: frequency)
        self.stacks = [[]]              # stacks[0] = []
                                        # stacks[1] = [elements of first occurrences]
                                        # stacks[2] = [elements of second occurrences]
        

    def push(self, val: int) -> None:
        self.freq[val] = self.freq.get(val, 0) + 1
        
        # for new frequency
        if len(self.stacks) <= self.freq[val]:
            self.stacks.append([val])
            
        # for our exisiting frequency
        else:
            self.stacks[self.freq[val]].append(val)

        
    def pop(self) -> int:
        v = self.stacks[-1].pop()
        if self.stacks[-1] == []:
            self.stacks.pop()
        self.freq[v] -= 1
        return v
        
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()