# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def distance(root, diameter):
    if root is None:
        return 0, diameter
    elif root.left is None and root.right is None:
        return 1, diameter
    else:
        right_length, right_diameter = distance(root.right, diameter)
        left_length, left_diameter = distance(root.left, diameter)
        print(f'right_length:{right_length}, left_length:{left_length}')
        curr_dia = right_length + left_length
        print(curr_dia)
        
        return max(right_length, left_length)+1, max([curr_dia, right_diameter, left_diameter])
        

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        _, res = distance(root, diameter)
        return res
        

        