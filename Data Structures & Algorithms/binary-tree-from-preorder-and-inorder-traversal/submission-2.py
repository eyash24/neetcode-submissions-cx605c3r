# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) > 0:
            if len(inorder) == 1:
                return TreeNode(inorder[0])

            print(f'C1\npreorder:{preorder}\ninorder:{inorder}')
            root = preorder[0]
            print('root: ', root)
            inorder_index = inorder.index(root)
            inorder_left_part = inorder[:inorder_index]
            if inorder_index + 1 < len(inorder):
                inorder_right_part = inorder[inorder_index+1:]
            else:
                inorder_right_part = []
            
            preorder = preorder[1:]
            
            i = 0
            preorder_left = []
            while i < len(inorder_left_part) and inorder_left_part[i] in preorder:
                preorder_left.append(preorder[i])
                i+=1
            
            if i+1 < len(preorder):
                preorder_right = preorder[i:]
            else:
                preorder_right = []

            node = TreeNode(root)
            print('\nLeft')
            print(f'preorder_left:{preorder_left}\ninorder_left: {inorder_left_part}')
            node.left = self.buildTree(preorder_left, inorder_left_part)

            print('\nRight')
            print(f'preorder_right:{preorder_right}\ninorder_right: {inorder_right_part}')
            node.right = self.buildTree(preorder_right, inorder_right_part)
            return node
        
        else:
            print('c2, None')
            return None

        


