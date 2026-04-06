# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        self.stack= []
        self.level(root, 0)
        res = []
        depth = len(self.stack)
        print(self.stack)
        
        for i in range(depth):
            row = self.stack[i]
            row = row[::-1]
            for j in row:
                if j is not None:
                    res.append(j)
                    break
        
        return res


    def level(self, root, level):
        if len(self.stack) < level+1:
            if root is None:
                self.stack.append([None])
            else:
                self.stack.append([root.val])
        else:
            if root is None:
                self.stack[level].append(None)
            else:
                self.stack[level].append(root.val)

        if root is not None:
            self.level(root.left, level+1)
            self.level(root.right, level+1)
        
    




            
        