# https://leetcode.com/problems/valid-palindrome/
# Solution 1
def isPalindrome(self, s: str) -> bool:
    s = s.lower()
    preprocessing = []
    for ch in s:
        if 48 <= ord(ch) <= 57 or 97 <= ord(ch) <= 122:
            preprocessing.append(ch)

    # Now, check it!!
    i, j = 0, len(preprocessing)-1
    while i < j:
        if preprocessing[i] != preprocessing[j]:
            return False
        j -= 1
        i += 1
    return True
# Solution 2


def isPalindrome(s: str) -> bool:
    i, j = 0, len(s) - 1
    while i < j:
        while i < j and not isAlphaNum(s[i]):
            i += 1
        while i < j and not isAlphaNum(s[j]):
            j -= 1
        if s[i].lower() != s[j].lower():
            return False
        i, j = i + 1, j - 1
    return True

# Could write own alpha-numeric function


def isAlphaNum(c):
    return (
        ord("A") <= ord(c) <= ord("Z")
        or ord("a") <= ord(c) <= ord("z")
        or ord("0") <= ord(c) <= ord("9"))
