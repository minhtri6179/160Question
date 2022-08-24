# Algoexpert
# Solution 1 O(N^3)
def longestPalindromicSubstring(string):
    # Write your code here.
    if len(string) == 1:
        return string
    longest = 0
    longestString = ""
    for i in range(len(string)):
        for j in range(i+2, len(string)+1):
            if isPalindromic(string[i:j]):
                if len(string[i:j]) > longest:
                    longest = len(string[i:j])
                    longestString = string[i:j]
    return longestString


def isPalindromic(s):
    i, j = 0, len(s)-1
    while i < j:
        if s[i] != s[j]:
            return False
        i, j = i+1, j-1
    return True

# Solution 2 O(N^2)


class Solution:
    def longestPalindrome(self, string: str) -> str:
        if len(string) <= 2:
            if len(string) == 1 or string[0] == string[1]:
                return string
            else:
                return string[0]
        longestString = ""
        for idx in range(len(string)):
            i, j = idx, idx
            a = self.longeste(string, i, j)
            b = self.longeste(string, i, j+1)
            if len(a) > len(longestString) or len(b) > len(longestString):
                if len(a) > len(b):
                    longestString = a
                else:
                    longestString = b
        return longestString

    def longeste(self, string, i, j):
        longest = 0
        longestString = ""
        while i >= 0 and j < len(string):
            if string[i] != string[j]:
                break
            if len(string[i:j+1]) > longest:
                longest = len(string[i:j+1])
                longestString = string[i:j+1]
            i, j = i-1, j+1
        return longestString

# Solution 3 (similar solution 2)


class Solution:
    def longestPalindrome(self, s: str) -> str:
        longestString = ""
        longestLen = 0
        for i in range(len(s)):
            # Odd substring
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if len(s[l: r+1]) > longestLen:
                    longestString = s[l:r+1]
                    longestLen = len(s[l: r+1])
                l, r = l-1, r+1

            # Even substring
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if len(s[l: r+1]) > longestLen:
                    longestString = s[l:r+1]
                    longestLen = len(s[l: r+1])
                l, r = l-1, r+1

        return longestString
