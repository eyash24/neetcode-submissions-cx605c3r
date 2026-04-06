# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def bst(root, min_val, max_val):
    if root is None:
        return True
    
    print(f'\nroot: {root.val}, min_val: {min_val}, max_val: {max_val}')
    
    if min_val is None and max_val is None:
        print('both are None\n')
        return bst(root.left, min_val, root.val) and bst(root.right, root.val, max_val)

    elif min_val is not None and max_val is None:
        print('min_val exist but max_val is None')
        if root.val > min_val:
            return bst(root.left, min_val, root.val) and bst(root.right, root.val, max_val)
        else:
            return False

    elif min_val is None and max_val is not None:
        print('min_val is none and max_val exist')
        if root.val < max_val:
            return bst(root.left, min_val, root.val) and bst(root.right, root.val, max_val)
        else:
            return False
    else:
        print('both exist')
        if root.val > min_val and root.val < max_val:
            return bst(root.left, min_val, root.val) and bst(root.right, root.val, max_val)
        else:
            return False

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        return bst(root, None, None)
        
        

        