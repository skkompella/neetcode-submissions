# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    is_bst = True
    def recurse(self, root, leftbound, rightbound):
        if self.is_bst == False:
            return
        if root == None:
            return
        if root.val <= leftbound or root.val >= rightbound:
            self.is_bst = False
        self.recurse(root.left, leftbound, root.val)
        self.recurse(root.right, root.val, rightbound)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.is_bst = True
        if root == None:
            return True
        if root.left == None and root.right == None:
            return True
        self.recurse(root.left, -1001, root.val)
        self.recurse(root.right, root.val, 1001)
        return self.is_bst