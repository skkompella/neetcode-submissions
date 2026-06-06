# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lca(self, root, less, great):
        if less.val == root.val:
            return root
        if great.val == root.val:
            return root
        if less.val < root.val and great.val > root.val:
            return root
        if less.val < root.val and great.val < root.val:
            return self.lca(root.left, less, great)
        if less.val > root.val and great.val > root.val:
            return self.lca(root.right, less, great)

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root == None:
            return None
        if root.left == None and root.right == None:
            return root
        LCA = root
        less = p
        great = q
        if p.val > q.val:
            less = q
            great = p
        if less.val == great.val:
            return less
        
        return self.lca(root, less, great)
