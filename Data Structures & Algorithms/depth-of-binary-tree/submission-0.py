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
        if root.left is None and root.right is None:
            return 1
        lh = 0
        rh = 0
        if root.left:
            lh = self.helper(root.left)
        if root.right:
            rh = self.helper(root.right)
        curheight = 1 + max(lh,rh)
        return curheight
        
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.helper(root)