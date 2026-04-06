import heapq


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        graph = []
        nodes = dict()
        set_track = [-1]*len(points)
        cost = 0
        set_num = 0

        for i, node in enumerate(points):
            nodes[str(node)] = i

        for src in points:
            for dst in points:
                d = abs(src[0] - dst[0]) + abs(src[1] - dst[1])
                heapq.heappush(graph,(d, src, dst))
        
        print(nodes)
        
        while graph:
            d, src, dst = heapq.heappop(graph)
            if src == dst:
                continue
            
            print(set_track)
            set_src = set_track[nodes[str(src)]]
            set_dst = set_track[nodes[str(dst)]]
            print('\nEdge length: ', d)
            print(f'Node: {src}, set: {set_src}')
            print(f'Node: {dst}, set: {set_dst}')
            
            if set_src == -1 and set_dst == -1:
                print('adding edge')
                cost += d
                set_track[nodes[str(src)]] = set_num
                set_track[nodes[str(dst)]] = set_num
                set_num += 1
            
            elif set_src == -1 and set_dst > -1:
                print('adding edge')
                cost += d
                set_track[nodes[str(src)]] = set_dst
            
            elif set_src > -1 and set_dst == -1:
                print('adding edge')
                cost += d
                set_track[nodes[str(dst)]] = set_src
            
            elif set_src > -1 and set_dst > -1 and set_src != set_dst:
                print('adding edge')
                cost += d
                src_count = set_track.count(set_src)
                dst_count = set_track.count(set_dst)

                if src_count > dst_count:
                    print('before: ', set_track)
                    for i in range(len(points)):
                        if set_track[i] == set_dst:
                            set_track[i] = set_src
                    print('after:', set_track)

                else:
                    print('before:', set_track)
                    for i in range(len(points)):
                        if set_track[i] == set_src:
                            set_track[i] = set_dst
                    print('after: ', set_track)

        return cost

  

