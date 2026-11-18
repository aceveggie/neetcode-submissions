# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.bst = True
        self.array = []
        self.a_len = 0

    def helper(self, root):
        if root is None:
            return
        self.helper(root.left)
        self.array.append(root.val)
        self.helper(root.right)

    def isincreasing(self):
        c_0 = self.array[0]
        i = 1
        while i < self.a_len and self.bst is True:
            if self.array[i] <= c_0:
                self.bst = False
            else:
                c_0 = self.array[i]
            i += 1
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        self.helper(root)
        self.a_len = len(self.array)
        if self.a_len > 1:
            self.isincreasing() 
        return self.bst