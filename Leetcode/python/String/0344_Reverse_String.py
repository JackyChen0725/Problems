"""
Link: https://leetcode.com/problems/reverse-string/

Solution1: Use two pointers to swap characters from both ends of the list until they meet in the middle.
    Time Complexity: O(n).
    Space Complexity: O(1).

Solution2: Similar to Solution1 but uses a for loop to reduce conditional checking time.
    Time Complexity: O(n).
    Space Complexity: O(1).
"""

from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        
        while left < right:
            s[left], s[right] = s[right], s[left]
            
            left += 1
            right -= 1

        return

class Solution2:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        n = len(s)
        
        for i in range(n // 2):
            s[i], s[n - 1 - i] = s[n - 1 - i], s[i]
        
        return

# print(Solution().reverseString(["h","e","l","l","o"]))
print(Solution().reverseString(["h","e","l","o"]))
