"""
Link: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

Solution1: Brute Force. Iterate through the haystack and check for the needle at each position.
    Time Complexity: O(n * m), where n is the length of haystack and m is the length of needle.
    Space Complexity: O(1).

Solution2: KMP Algorithm. Preprocess the needle to create a "next" array that indicates the longest prefix which is also a suffix.
    Time Complexity: O(n + m), where n is the length of haystack and m is the length of needle.
    Space Complexity: O(m).
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0

        n = len(haystack)
        m = len(needle)
        
        for i in range(n - m + 1):
            k = i
            j = 0
            while j < m and haystack[k] == needle[j]:
                k += 1
                j += 1

            if j == m:
                return i
        return -1

class Solution2:
    def strStr(self, haystack: str, needle: str) -> int:
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
        
        if needle == "":
            return 0
        
        n = len(haystack)
        m = len(needle)

        next = [0] * m
        getNext(next, needle)

        j = 0
        for i in range(n):
            while j > 0 and haystack[i] != needle[j]:
                j = next[j - 1]

            if haystack[i] == needle[j]:
                j += 1
            
            if j == m:
                return i - m + 1
        return -1

print(Solution().strStr("sadbutsad", "sad"))
print(Solution().strStr("sabutsad", "sad"))
print(Solution().strStr("sadbutsa", "sad"))
print(Solution().strStr("leetcode", "leeto"))
print(Solution().strStr("leetcode", ""))


