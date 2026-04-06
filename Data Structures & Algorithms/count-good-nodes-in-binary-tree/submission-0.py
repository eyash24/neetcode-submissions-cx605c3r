# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        self.traverse_tree(root, None)

        return self.count

    def traverse_tree(self, root, max_val):
        if root is None:
            return 
        if max_val:
            if root.val >= max_val:
                max_val = root.val
                self.count += 1

                self.traverse_tree(root.right, max_val)
                self.traverse_tree(root.left, max_val)
            else:
                self.traverse_tree(root.right, max_val)
                self.traverse_tree(root.left, max_val)
        else:
            self.count += 1
            max_val = root.val
            self.traverse_tree(root.right, max_val)
            self.traverse_tree(root.left, max_val)
                