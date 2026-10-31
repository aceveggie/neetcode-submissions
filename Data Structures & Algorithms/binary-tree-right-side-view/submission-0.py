# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        if root is None:
            return output
        q = [[root]]
        while len(q) > 0:
            cur_level = q.pop()
            o_list = []
            n_list = []
            for each_node in cur_level:
                o_list.append(each_node.val)
                if each_node.left:
                    n_list.append(each_node.left)
                if each_node.right:
                    n_list.append(each_node.right)
            if n_list:
                q.append(n_list)
            output.append(o_list[-1])
        return output
