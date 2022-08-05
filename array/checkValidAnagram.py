# https://leetcode.com/problems/valid-anagram/

# Solution 1
def isAnagram(self, s: str, t: str) -> bool:
    tables = {}
    tablet = {}
    for k in s:
        if k in tables:
            tables[k] += 1
        else:
            tables[k] = 1

    for k in t:
        if k in tablet:
            tablet[k] += 1
        else:
            tablet[k] = 1
    return tables == tablet

# Solution 2


def isAnagram(self, s: str, t: str) -> bool:
    return sorted(s) == sorted(t)
