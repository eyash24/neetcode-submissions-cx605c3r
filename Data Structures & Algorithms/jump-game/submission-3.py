class Solution:
    def canJump(self, nums: List[int]) -> bool:
        stack = [0]
        target = len(nums)-1
        # print('target: ', target)

        while stack:
            index = stack.pop(0)
            if index == target:
                return True

            jump = nums[index]
            # print('index: ', index, 'jump: ', jump, "next index: ", index+jump)
            if jump > 0:
                for i in range(1,jump+1):
                    stack.append(index+i)            
        
        return False            

        
        