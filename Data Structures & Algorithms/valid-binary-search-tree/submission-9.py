# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.bst = True
        self.prev_val = None

    def helper(self, root):
        if root is None or self.bst is False:
            return
        self.helper(root.left)
        if self.prev_val is None:
            self.prev_val = root.val
        elif self.prev_val < root.val:
            self.prev_val = root.val
        else:
            self.bst = False
            return
        self.helper(root.right)

    def isValidBST(self, root: TreeNode | None) -> bool:
        if root is None:
            return True
        self.helper(root)
        return self.bst