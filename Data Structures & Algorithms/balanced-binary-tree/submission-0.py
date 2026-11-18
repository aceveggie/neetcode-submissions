# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, root):
        if self.balanced == False:
            return 0
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        lh,rh = 0,0
        if root.left:
            lh = self.helper(root.left)
        if root.right:
            rh = self.helper(root.right)
        if abs(lh-rh) > 1:
            self.balanced=False
            return 0
        return 1 + max(lh,rh)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        if root is None:
            return self.balanced
        
        self.helper(root)
        return self.balanced