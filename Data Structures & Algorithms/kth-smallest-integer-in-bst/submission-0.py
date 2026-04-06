# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root):
        print(self.index, self.nodes)
        if root is None:
            return 
        
        if root.left is None and root.right is None:
            self.index += 1
            self.nodes.append(root.val)
            if self.index == k:
                self.res = self.nodes[k-1]

        elif root.left is not None:
            self.dfs(root.left)
            self.index += 1
            self.nodes.append(root.val)
            if self.index == k:
                self.res = self.nodes[k-1]
            self.dfs(root.right)

        elif root.left is None:
            self.index += 1
            self.nodes.append(root.val)
            if self.index == k:
                self.res = self.nodes[k-1]
            self.dfs(root.right)
            
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.index = 0
        self.nodes = []
        self.res = None
        self.dfs(root)
        return self.res

            