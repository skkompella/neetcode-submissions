# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    li = []
    def levelOrderRecurse(self, root, height):
        if root == None:
            return
        if len(self.li) == height:
            self.li.append([root.val])
        else:
            self.li[height].append(root.val)
        self.levelOrderRecurse(root.left, height+1)
        self.levelOrderRecurse(root.right, height+1)

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.li = []
        self.levelOrderRecurse(root, 0)
        return self.li
        