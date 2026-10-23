class Solution:
    def climbStairs(self, n: int) -> int:

        if n<=2:
            return n
        prev=1
        curr=2

        for i in range(3,n+1):
            total=prev+curr
            prev=curr
            curr=total
            
        return total



        