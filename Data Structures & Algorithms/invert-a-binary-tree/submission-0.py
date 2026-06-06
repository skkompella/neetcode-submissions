# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None or root.left == None and root.right == None:
            return root
        tmp = root.left
        tmp1 = root.right
        root.left = self.invertTree(tmp1)
        root.right = self.invertTree(tmp)
        return root
        