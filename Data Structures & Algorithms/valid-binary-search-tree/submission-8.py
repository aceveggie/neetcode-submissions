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

    def helper(self, root):
        if root is None:
            return
        self.helper(root.left)
        if len(self.array)>0 and self.array[-1] >= root.val:
            self.bst = False
            return
        self.array.append(root.val)
        self.helper(root.right)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        self.helper(root)
        return self.bst