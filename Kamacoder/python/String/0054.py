"""
Link: https://kamacoder.com/problempage.php?pid=1064

Solution1: Direct Replacement.
    Time Complexity: O(n).
    Space Complexity: O(n). (Auxiliary space for the temporary list)

Solution2: Two Pointers from the End.
    Time Complexity: O(n).
    Space Complexity: O(n). (Auxiliary space for the result list)
"""

class Solution:
    def substitute_numbers(self, s: str) -> str:
        res = list(s)
        
        for i in range(len(res)):
            if res[i].isdigit():
                res[i] = 'number'
        
        return ''.join(res)

class Solution2:
    def substitute_numbers(self, s: str) -> str:
        cnt = sum(1 for c in s if c.isdigit())
        oldLength = len(s)
        newLength = oldLength + cnt * 5
        
        res = [''] * newLength
        oldIndex = oldLength - 1
        newIdx = newLength - 1
        
        while oldIndex >= 0:
            if s[oldIndex].isdigit():
                res[newIdx] = 'r'
                res[newIdx - 1] = 'e'
                res[newIdx - 2] = 'b'
                res[newIdx - 3] = 'm'
                res[newIdx - 4] = 'u'
                res[newIdx - 5] = 'n'
                
                newIdx -= 6
            else:
                res[newIdx] = s[oldIndex]
                
                newIdx -= 1
            oldIndex -= 1
        
        return ''.join(res)

if __name__ == '__main__':
    sol = Solution()

    while True:
        try:
            s = input()
            res = sol.substitute_numbers(s)
            print(res)
        except EOFError:
            break