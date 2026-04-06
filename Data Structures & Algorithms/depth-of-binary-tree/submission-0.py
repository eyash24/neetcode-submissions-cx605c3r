# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def depth(root):
    if root is None:
        return 0
    elif root.left is None and root.right is None:
        return 1
    else:
        return max(1+depth(root.left), 1+depth(root.right))

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return depth(root)


        