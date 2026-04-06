from collections import defaultdict, deque


class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adjacency = {c: set() for w in words for c in w}
        incoming_edges = {c: 0 for w in words for c in w}
        
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            min_len = min(len(w1), len(w2))
            
            diff = False
            for j in range(min_len):
                if w1[j]!= w2[j]:
                    if w2[j] not in adjacency[w1[j]]:
                        adjacency[w1[j]].add(w2[j])
                        incoming_edges[w2[j]] += 1
                    diff = True
                    break
            
            if not diff and len(w1) > len(w2):
                return ''
        
        print(adjacency)
        
        queue = deque()
        for k in incoming_edges:
            if incoming_edges[k] == 0:
                queue.append(k)

        arrangement = ""

        while queue:
            node = queue.popleft()
            arrangement += str(node)
            print(node)

            for no in adjacency[node]:
                incoming_edges[no] -= 1
                if incoming_edges[no] == 0:
                    queue.append(no)

        if len(arrangement) != len(incoming_edges):
            return ""

        return arrangement