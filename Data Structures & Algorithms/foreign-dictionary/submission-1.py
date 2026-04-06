from collections import OrderedDict, deque
from typing import List

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adjacency_dict = {c: set() for w in words for c in w}
        incoming_edges = {c: 0 for w in words for c in w}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            min_len = min(len(w1), len(w2))

            found = False
            for j in range(min_len):
                if w1[j] != w2[j]:
                    if w2[j] not in adjacency_dict[w1[j]]:
                        adjacency_dict[w1[j]].add(w2[j])
                        incoming_edges[w2[j]] += 1
                    found = True
                    break

            if not found and len(w1) > len(w2):
                return ""
        
        print(adjacency_dict)

        queue = deque()
        for c in incoming_edges:
            if incoming_edges[c] == 0:
                queue.append(c)

        arrangement = ""

        while queue:
            node = queue.popleft()
            arrangement += node

            for nei in adjacency_dict[node]:
                incoming_edges[nei] -= 1
                if incoming_edges[nei] == 0:
                    queue.append(nei)

        if len(arrangement) != len(incoming_edges):
            return ""

        return arrangement