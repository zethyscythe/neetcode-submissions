class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l=0
        r=len(heights)-1
        max_area=0
        while l<r:
            
            area=(r-l) * min(heights[l],heights[r])
            #print(f"l={l} r= {r} heights_l={heights[l]} heights_r={heights[r]} area={area}")

            max_area=max(max_area,area)    
            if heights[l] > heights[r]:
                r-=1
            else:
                l+=1    
        return max_area