# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def check_tree(root, p, q):
    if root is None:
        return (False, False, None)
    # elif root.left is None and root.right is None:
    #     print(root.val)
    #     return (False, False, None)
    else:
        print(root.val)
        if root.val == p:

            print('found p')
            # check for q
            res_l = check_tree(root.left, p, q)
            res_r = check_tree(root.right, p, q)
            print(res_l, res_r, sep="\n", end="\n\n")

            if res_l[1] or res_r[1]:
                return (True, True, root)
            else:
                return (True, False, None)

        elif root.val == q:
            print('found q')
            # check for p
            res_l = check_tree(root.left, p, q)
            res_r = check_tree(root.right, p, q)
            print(res_l, res_r, sep="\n", end="\n\n")

            if res_l[0] or res_r[0]:
                return (True, True, root)
            else:
                return (False, True, None)

        else:
            res_l = check_tree(root.left, p, q)
            res_r = check_tree(root.right, p, q)
            print(res_l, res_r, sep="\n", end="\n\n")
            
            if res_l[2] is not None or res_r[2] is not None:
                if res_l[2]:
                    return res_l
                else:
                    return res_r

            elif (res_l[0] and res_r[1]) or (res_l[1] and res_r[0]):
                return (True, True, root)
            
            elif res_l[0] or res_r[0]:
                return (True, False, None)

            elif res_l[1] or res_r[1]:
                return (False, True, None)

            else:
                return (False, False, None)     


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        res = check_tree(root, p.val, q.val)
        print(res)
        return res[-1]
        