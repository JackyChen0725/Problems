"""
Link: https://leetcode.com/problems/repeated-substring-pattern/

Solution1: Double String Method. The original string will exist in the doubled string (excluding the first and last characters) if it is repeated by the minimum repeating unit.
    Time Complexity: O(n), the time complexity of str.find() is O(m + n), where m = 2*n here, and O(3*n) = O(n).
    Space Complexity: O(n).

Solution2: KMP Algorithm. The substring that excludes the longest prefix-suffix is the minimum repeating unit.
    Time Complexity: O(n). the time complexity of building the "next" array is O(n), and the final check is O(1).
    Space Complexity: O(n).
"""

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s) <= 1:
            return False
        
        repeated_s = s[1:] + s[:-1]
        if repeated_s.find(s) != -1:
            return True
        return False

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        from typing import List
        
        def getNext(next: List[str], s: str) -> None:
            j = 0
            next[0] = 0
            for i in range(1, len(s)):
                while j > 0 and s[i] != s[j]:
                    j = next[j - 1]
                
                if s[i] == s[j]:
                    j += 1
                    
                next[i] = j
            return

        n = len(s)
        next = [0] * n
        getNext(next, s)
        
        if next[n - 1] != 0 and n % (n - next[n - 1]) == 0:
            return True
        return False

print(Solution().repeatedSubstringPattern('a'))
print(Solution().repeatedSubstringPattern('ab'))
print(Solution().repeatedSubstringPattern('abab'))
print(Solution().repeatedSubstringPattern('ababab'))
print(Solution().repeatedSubstringPattern('abababc'))
