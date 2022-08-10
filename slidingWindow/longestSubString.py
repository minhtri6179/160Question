# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Solution 1
def lengthOfLongestSubstring(self, s: str) -> int:
    if len(s) == 0:
        return 0
    maxCount = 1
    for i, ch in enumerate(s):
        curSet = set(ch)
        for j in range(i+1, len(s)):
            if s[j] in curSet:
                maxCount = max((j-i), maxCount)
                break
            curSet.add(s[j])
            maxCount = max(len(curSet), maxCount)
    return maxCount

# Solution 2 (sliding window)


def lengthOfLongestSubstring(self, s: str) -> int:
    hashSet = set()
    i, j = 0, 0
    maxCount = 0
    while j < len(s):
        while s[j] in hashSet:
            hashSet.remove(s[i])
            i += 1
        hashSet.add(s[j])
        maxCount = max(maxCount, (j-i+1))
        j += 1
    return maxCount

# Solution 3 (hash map)


def lengthOfLongestSubstring(self, s: str) -> int:
    hashMap = {}
    i = 0
    maxLength = 0
    for j in range(len(s)):
        if s[j] in hashMap and hashMap[s[j]] >= i:
            i = hashMap[s[j]] + 1
        hashMap[s[j]] = j
        maxLength = max(maxLength, j-i + 1)
    return maxLength
