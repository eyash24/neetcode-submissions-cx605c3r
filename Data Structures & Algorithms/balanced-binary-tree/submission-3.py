# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def height(root):
    if root is None:
        print('c1', None)
        return 0, True
    elif root.left is None and root.right is None:
        print('c2', root.val)
        return 1, True
    else:
        rh, res_r = height(root.right)
        lh, res_l = height(root.left)
        if res_r is False or res_l is False or abs(rh-lh) > 1:
            return max(rh, lh)+1, False
        else:
            return max(rh, lh)+1, True


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        r_h, r_res = height(root.right)
        print()
        l_h, l_res = height(root.left)
        print()
        print(r_h, l_h)
        if abs(r_h-l_h) < 2 and r_res and l_res:
            return True
        else:
            return False
        