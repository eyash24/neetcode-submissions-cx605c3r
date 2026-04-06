class Solution:
    
    def climbStairs(self, n: int) -> int:
        way = 0
        mem = [-1]*46
        mem[0] = 0
        mem[1] = 1
        mem[2] = 2
        
        for i in range(3, n+1):
            ways = 0
            if i - 1 >= 0:
                req = i-1
                if mem[req] > -1:
                    ways += mem[req]
            
            if i - 2>=0:
                req = i-2
                if mem[req] > -1:
                    ways += mem[req]
            
            mem[i] = ways
    
        # print(mem)
        return mem[n]