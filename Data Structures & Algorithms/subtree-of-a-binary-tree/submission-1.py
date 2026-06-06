# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isTreeSame(self, p, q):
        if p == None and q == None:
            return True
        if p == None or q == None:
            return False
        if self.isTreeSame(p.left, q.left) == False:
            return False
        if self.isTreeSame(p.right, q.right) == False:
            return False
        if p.val != q.val:
            return False
        return True
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root == None and subRoot == None:
            return True
        if root == None:
            return False
        if subRoot == None:
            return True
        jon = subRoot.val
        if root.val == jon:
            if self.isTreeSame(root, subRoot):
                return True
        return self.isSubtree(root.left, subRoot) | self.isSubtree(root.right, subRoot)