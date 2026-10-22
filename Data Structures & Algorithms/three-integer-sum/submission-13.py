class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #-1,0,1
        #-1,1,2
        #-1,-1,-4

        #0,1,2
        #0,2,-1
        #0,-1,-4
        nums.sort()
        print(nums)
        #[-4,-1,-1,0,1,2]
        result=[]
        
        for i,num in enumerate(nums):
            if(num>0):
                break
            if (i>0 and num==nums[i-1]):
                continue

            l=i+1    
            r=len(nums)-1
            while l<r:

                three_sum = num+ nums[l]+nums[r]
                #print(f"num: {num} nums[l]: {nums[l]} nums[r]: {nums[r]}")
                if three_sum <0:
                    l+=1 
                    continue

                elif three_sum >0:
                    r-=1
                    continue      

                result.append([num,nums[l],nums[r]])    
                #print(result)
                l+=1
                r-=1

                while (l<r and nums[l]==nums[l-1]):
                    l+=1
                while (l<r and nums[r]==nums[r+1]):
                    r-=1                    
                # -1,0,0,1
                # num=-1, num_left=0 num_right=1
                # num=-1, num_left=0, num_right=1


            

        return result

          





    

        