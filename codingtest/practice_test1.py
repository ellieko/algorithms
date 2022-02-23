'''
PROBLEM 1)

Implement a String like class with methods as below, 
with space complexity of 0(1) for all the methods

Class Str {
public Str(char[] arr) // constructor

public char charAt(int idx);

public Str substring(int startIdx, int length); // should use constant space
}

'''

class Str:
    def __init__(self, arr):
        self.arr = arr
    def charAt(self, idx):
        return self.arr[idx]
    def substring(self, start_idx, length):
        return self.arr[start_idx: start_idx + length]
        # you can catch when its length is exceeded


'''

PROBLEM 2)
Given a BSTNode object, return the next in order node.

'''

# Binary Search Tree
class BST: 
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None  

    def add_child(self, data):
        if data == self.data:
            return
        elif data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BST(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BST(data)

    def print_tree(self):
        if self:
            print(self.data, end = ' ')
            if self.left:
                return self.left.print_tree()
            if self.right:
                return self.right.print_tree()
            print()


def build_tree(elements):
    root = BST(elements[0])
    for e in elements:
        root.add_child(e)
    return root
    

if __name__ == '__main__':
    str = Str("this")
    print(str.substring(1,5))

    bst = build_tree([5,4,8,3,32,1])
    bst.print_tree()