# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def invert(root):
    if root is None:
        return None

    elif root.left is None and root.right is None:
        return root
    else:
        root.left, root.right = invert(root.right), invert(root.left)
        return root

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        root = invert(root)
        return root

        
