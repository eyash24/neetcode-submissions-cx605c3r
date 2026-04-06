# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def check_subtree(root, subroot):
    if root is None and subroot is None:
        return True

    elif root is None and subroot:
        return False

    elif root and subroot is None:
        return False

    elif root.val == subroot.val:
        return check_subtree(root.left, subroot.left) and check_subtree(root.right, subroot.right)
        
    else:
        return False 


class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None and subRoot is None:
            return True
        elif root is None and subRoot:
            return False
        elif root and subRoot is None:
            return True

        if root.val == subRoot.val:
            temp_subtree = subRoot
            temp_root = root
            res = check_subtree(temp_root, temp_subtree)
            if res is True:
                return True
            else:
                return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)
        else:
            return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)

        