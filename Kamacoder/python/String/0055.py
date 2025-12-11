"""
Link: https://kamacoder.com/problempage.php?pid=1065

Solution1: Use built-in functions and slicing.
    Time Complexity: O(n).
    Space Complexity: O(n). (Auxiliary space for the result list)

Solution2: Reverse the whole string, then reverse two substrings separated by k.
    Time Complexity: O(n).
    Space Complexity: O(n). (Auxiliary space for the result list)
"""

class Solution:
    def rightRotate(self, s: str, k: int) -> str:
        length = len(s)
        
        if k > length:
            return ''
        if k == length:
            return s
        
        s_list = list(s)
        s_list = s_list[-k:] + s_list[:-k]
        return ''.join(s_list)

class Solution2:
    def rightRotate(self, s: str, k: int) -> str:
        from typing import List

        def reverseSubstring(s: List[str]) -> List[str]:
            left, right = 0, len(s) - 1
            
            while left < right:
                s[left], s[right] = s[right], s[left]
                
                left += 1
                right -= 1

            return s

        length = len(s)
        
        if k > length:
            return ''
        if k == length:
            return s
        
        s_list = list(s)
        s_list = reverseSubstring(s_list)
        s_list = reverseSubstring(s_list[:k]) + reverseSubstring(s_list[k:])
        
        return ''.join(s_list)

if __name__ == '__main__':
    import sys
    
    data = sys.stdin.read().strip().splitlines()
    k, s = int(data[0]), data[1]
    
    print(Solution().rightRotate(s, k))