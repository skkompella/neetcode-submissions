# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode], depth = 0) -> int:
        if root == None:
            return depth
        # if root.left == None and root.right == None:
        #     return depth + 1
        depth += 1
        return max(self.maxDepth(root.left, depth), self.maxDepth(root.right, depth))