"""
Link: https://leetcode.com/problems/reverse-string-ii/

Solution1: Use two pointers to reverse every 2k characters in the string. Be aware of the cases where the remaining characters are less than k or between k and 2k.
    Time Complexity: O(n).
    Space Complexity: O(n). (Auxiliary space for the temporary list)

Solution2: Similar to Solution1 but use a helper function and list slicing method.
    Time Complexity: O(n).
    Space Complexity: O(n). (Auxiliary space for the temporary list)
"""

from typing import List

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res = list(s)
        n = len(s)
        
        for start in range(0, n, k * 2):
            left = start
            right = start + k - 1 if start + k <= n else n - 1
            
            while left < right:
                res[left], res[right] = res[right], res[left]
                
                left += 1
                right -= 1
        
        return ''.join(res)

class Solution2:
    def reverseStr(self, s: str, k: int) -> str:
        def reverseSubstring(s: List[str]) -> List[str]:
            left, right = 0, len(s) - 1
            
            while left < right:
                s[left], s[right] = s[right], s[left]
                
                left += 1
                right -= 1

            return s
    
        res = list(s)
        n = len(s)
        
        for start in range(0, n, k * 2):
            left = start
            right = start + k if start + k <= n else n

            res[left : right] = reverseSubstring(res[left : right])

        return ''.join(res)

print(Solution().reverseStr("abcdefg", 2))
print(Solution().reverseStr("abcdefgh", 3))
