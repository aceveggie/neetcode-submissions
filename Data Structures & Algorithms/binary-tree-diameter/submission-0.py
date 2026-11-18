# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, root):
        if root is None:
            return 0
        lh,rh =0,0
        lh = self.helper(root.left)
        rh = self.helper(root.right)
        self.maxd = max(self.maxd, lh+rh)
        return 1 + max(lh, rh)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxd = 0
        self.helper(root)
        return self.maxd