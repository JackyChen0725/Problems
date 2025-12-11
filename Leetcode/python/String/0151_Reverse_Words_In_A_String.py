"""
Link: https://leetcode.com/problems/reverse-words-in-a-string/

Solution1: Use built-in functions. Split the string by spaces, reverse the list of words, and join them with a single space.
    Time Complexity: O(n).
    Space Complexity: O(n). (Auxiliary space for the temporary list)

Solution2: Use two pointers to first remove extra spaces, then reverse the entire string, and finally reverse each word individually.
    Time Complexity: O(n).
    Space Complexity: O(n). (Auxiliary space for the temporary list)
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.split()
        s_list = s_list[::-1]
    
        return ' '.join(s_list)

class Solution2:
    def reverseWords(self, s: str) -> str:
        def removeExtraSpaces(s_list: list) -> list:
            s_list = list(s)
            length = len(s)
            
            slow = 0
            fast = 0
            while fast < length:
                if s_list[fast] != ' ':
                    if slow > 0:
                        s_list[slow] = ' '
                        slow += 1
                    while fast < length and s_list[fast] != ' ':
                        s_list[slow] = s_list[fast]
                        print(s_list[slow])
                        slow += 1
                        fast += 1
                else:
                    fast += 1
            return s_list[:slow]

        def reverseEachWord(s_list: list) -> list:
            length = len(s_list)
            
            start = 0
            end = 0
            while end < length:
                if s_list[end] == ' ':
                    s_list[start:end] = s_list[start:end][::-1]
                    start = end + 1
                end += 1
            s_list[start:end] = s_list[start:end][::-1]

            return s_list

        s_list = list(s)
        # print(s_list)
        s_list = removeExtraSpaces(s_list)
        # print(s_list)
        s_list = s_list[::-1]
        # print(s_list)
        s_list = reverseEachWord(s_list)
        # print(s_list)
        
        return ''.join(s_list)

sol = Solution()
print(sol.reverseWords("the sky is blue"))