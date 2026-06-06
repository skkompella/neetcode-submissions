# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    li = deque()
    cnt = 0
    def recurse(self, root):
        if len(self.li) == 0:
            return
        if all(root.val >= i for i in self.li):
            self.cnt += 1
        if root.left != None:
            self.li.append((root.left).val)
            self.recurse(root.left)
            self.li.pop()
        if root.right != None:
            self.li.append((root.right).val)
            self.recurse(root.right)
            self.li.pop()
        
    def goodNodes(self, root: TreeNode) -> int:
        self.li = deque()
        self.cnt = 0
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1
        self.li.append(root.val)
        self.recurse(root)
        # self.cnt += 1
        return self.cnt
