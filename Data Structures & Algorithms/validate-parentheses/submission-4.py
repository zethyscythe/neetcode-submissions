class Solution:
    def isValid(self, s: str) -> bool:
        # 1. Early exit optimization for odd lengths
        if len(s) % 2 != 0:
            return False
            
        # 2. Hash map for O(1) bracket matching
        bracket_map = {")": "(", "}": "{", "]": "["}
        stack = []
        
        for char in s:
            if char in bracket_map:
                # 3. Combined stack-empty and pop verification
                if not stack or stack.pop() != bracket_map[char]:
                    return False
            else:
                stack.append(char)
                
        return not stack
    