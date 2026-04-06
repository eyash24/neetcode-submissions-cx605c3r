class Solution:
    def __init__(self):
        self.d = dict()
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        index = 0
        for i in range(2, 10):
            self.d[i] = list(alpha[index:index+3])
            index += 3

            if i == 9:
                self.d[9] = self.d.get(9) + ['z']
            elif i == 7:
                self.d[7] = self.d.get(7) + ['s']
                index+=1 

    def letterComboHelper(self, digits, index, prev_list):
        if digits =='':
            self.result = []
            return
        
        alpha = self.d.get(int(digits[index]))
        print('alpha:', alpha)
        print('prev_list:', prev_list)
        print('index: ', index)
        new_list = []

        if prev_list:
            print('creating combo')
            for i in alpha:
                for j in prev_list:
                    print(i+j)
                    new_list.append(j+i)
        else:
            new_list = alpha
        
        print('new_list: ', new_list)
        
        index += 1
        if index == len(digits):
            self.result.extend(new_list.copy())
        else:
            self.letterComboHelper(digits, index, new_list)
    
    

    def letterCombinations(self, digits: str) -> List[str]:
        self.result = []
        self.letterComboHelper(digits, 0, [])
        return self.result

        