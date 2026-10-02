class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # 1=2*4*6
        # 2=1*4*6
        # 4=1*2*6
        # 6=1*2*4

        left=[1] * len(nums)
        left_num=1
        right_num=1
        right=[1] * len(nums)
        for i in range(len(nums)-1):
            left_num*=nums[i]
            left[i+1]=left[i] * nums[i]
            #print(left[i+1])
            #print(left_num)
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
            right[j-1]=right[j]*nums[j]
            #print(f" idx= {j-1} val= {right[j-1]} ")
            #print(nums[j])
        #print(right[3])    
        #print(left[0])
        return [x * y for x, y in zip(left, right)]
