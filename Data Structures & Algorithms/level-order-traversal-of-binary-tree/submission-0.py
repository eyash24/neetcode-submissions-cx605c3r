# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

        

class Solution:
    def __init__(self):
        self.stack = [[]]

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        self.level(root, 0)
        return self.stack

    def level(self, root, h):
        if root:
            if len(self.stack) < h+1:
                self.stack.append([root.val])
            else:
                rec = self.stack[h]
                rec.append(root.val)
                self.stack[h] = rec
            
            self.level(root.left, h+1)
            self.level(root.right, h+1)
        