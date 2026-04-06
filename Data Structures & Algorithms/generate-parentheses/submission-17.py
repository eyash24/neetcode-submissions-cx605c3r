class Solution:
    def genParHelper(self, s='', left=0, right=0):
        print(s)
        if len(s) == 2*self.n:
            print(s)
            self.res.append(s)
            return
        
        if left < self.n:
            self.genParHelper(s+'(', left+1, right)

        if right < left:
            self.genParHelper(s+')', left, right+1)
        


    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        self.n = n
        self.genParHelper()
        return self.res
        