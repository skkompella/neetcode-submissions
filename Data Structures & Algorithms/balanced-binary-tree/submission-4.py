# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def bal(self, root):
        # if root == None:
        #     return 0, 0
        # bal = 0
        # jon = self.bal(root.left, height)
        # ron = self.bal(root.right, height)
        # if (root.left == None and root.right != None) or (root.right == None and root.left != None):
        #     bal += 1
        # if (root.left != None or root.right != None):
        #     height += 1
        # if jon[0] == -1 or ron[0] == -1:
        #     return -1
        # bal += abs(jon[0] - ron[0])
        # print(bal)
        # if bal > 1:
        #     return -1
        # if abs(jon[0] - ron[0]) > 1:
        #     return -1
        # return bal, height

        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1
        jon = self.bal(root.left)
        ron = self.bal(root.right)
        height = max(jon, ron)
        if (root.left != None or root.right != None):
            height += 1
        # print(height, abs(ron - jon))
        print(jon, ron)
        if ron == -1 or jon == -1:
            return -1
        if abs(ron - jon) > 1:
            return -1
        return height

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if self.bal(root) == -1:
            return False
        return True