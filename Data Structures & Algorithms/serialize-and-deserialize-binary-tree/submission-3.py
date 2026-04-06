# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:

    def bfs(self, root, pos):
        l_p, r_p = 2*pos+1, 2*pos+2

        if len(self.ll) < r_p +2:
            self.ll += [100001]*(r_p-len(self.ll)+1)
        
        if root is None:
            self.ll[pos] = 100001

        elif root and root.left is None and root.right is None:
            self.ll[pos] = root.val
            self.ll[l_p] = 100001
            self.ll[r_p] = 100001

        else:
            self.ll[pos] = root.val
            self.bfs(root.left, l_p)
            self.bfs(root.right, r_p)
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.ll = list()

        self.bfs(root, 0)
        return str(self.ll)[1:-1]
        
    def buildTree(self, index):
        if index > len(self.tree_ll):
            return None
        
        elif self.tree_ll[index] == 100001:
            # None
            return None

        else:
            l_pos, r_pos = 2*index+1, 2*index+2

            node = TreeNode(self.tree_ll[index])
            node.left = self.buildTree(l_pos)
            node.right = self.buildTree(r_pos)

            return node


    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        print(data)
        self.tree_ll = list(map(int, data.split(',')))
        print(len(self.tree_ll))
        print('tree ll: ',self.tree_ll)
        
        return self.buildTree(0)




