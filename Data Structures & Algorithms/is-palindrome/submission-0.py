class Solution:
    def isPalindrome(self, s: str) -> bool:

        i=0
        j=len(s)-1

        while i<len(s) and j>-1:

            left=s[i]
            right=s[j]
            if not s[i].isalnum():
                i+=1
                continue
            elif not s[j].isalnum():
                j-=1
                continue

            if s[i].lower()!=s[j].lower():
                return False
            i+=1
            j-=1    
        return True        



        

        