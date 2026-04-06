"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        
        queue = [node]
        node_dict = dict()
        visited = []

        while queue:
            root = queue.pop(0)
            val, neighbors = root.val, root.neighbors
            visited.append(val)
            if val not in node_dict:
                new_node = Node(val=val)
                node_dict[val] = new_node
            else:
                new_node = node_dict[val]
            
            for n in neighbors:
                print(n.val)
                if n.val not in visited:
                    queue.append(n)
                
                if n.val not in node_dict:
                    node_dict[n.val] = Node(val=n.val)
                
                if node_dict[n.val] not in new_node.neighbors:
                    new_node.neighbors.append(node_dict[n.val])
            
            print('queue: ', queue)
        
        print(node_dict)
        for k,nod in node_dict.items():
            print(k,nod, nod.neighbors)

        return node_dict[1]
            

                




        