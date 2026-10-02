class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 1=2*4*6
        # 2=1*4*6
        # 4=1*2*6
        # 6=1*2*4
        #left=[1] * len(nums)
        #right=[1] * len(nums)
        result=[1] * len(nums)
        left_num=1
        right_num=1
        for i in range(len(nums)-1):
            left_num*=nums[i]
            result[i+1]=left_num
            #nums[i+1]*=nums[i]
            #0 1
            #1 1
            #2 1*2
            #3 1*2*4
        for j in range(len(nums)-1,0,-1):
            #0 6*4*2
            #1 6*4
            #2 6
            #3 1
            right_num*=nums[j]
            result[j-1]*=right_num
            
        return result
