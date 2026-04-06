# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self,root):
        # return format: val till path , max_val
        if root is None:
            return None
        
        if root.left is None and root.right is None:
            if self.res is not None:
                self.res = max(self.res, root.val)
            else:
                self.res = root.val
            return root.val

        r_val = self.pathSum(root.right)
        l_val = self.pathSum(root.left)

        if not r_val and not l_val:
            max_path = root.val
            propagate = max_path
        elif not r_val and l_val:
            max_path = max(l_val+root.val, root.val)
            propagate = max_path
        elif r_val and not l_val:
            max_path = max(r_val+root.val, root.val)
            propagate = max_path
        else:
            max_path = max(r_val+l_val+root.val, r_val+root.val, l_val+root.val, root.val)
            propagate = max(r_val+root.val, root.val, l_val+root.val)

        self.res = max(self.res, max_path)
        return propagate


    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = None
        _ = self.pathSum(root)
        return self.res

    
        