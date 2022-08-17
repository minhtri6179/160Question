# https://leetcode.com/problems/valid-palindrome-ii/
# Solution 1 :((((   O(N^2) time exceeded
class Solution:
    def validPalindrome(self, s: str) -> bool:
        # Firstly, create sub string
        for pos, ch in enumerate(s):
            a = s[:pos] + s[(pos+1):]
            if self.checkPali(a):
                return True
        return False

    def checkPali(self, s):
        i, j = 0, len(s)-1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
