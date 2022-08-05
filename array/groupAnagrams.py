# https://leetcode.com/problems/group-anagrams/
# Solution 1
from collections import defaultdict


def groupAnagrams(self, strs):
    table = defaultdict(list)
    for s in strs:
        counter = [0]*26
        for k in s:
            counter[ord(k)-ord('a')] += 1

        table[tuple(counter)].append(s)

    return table.values()


def groupAnagrams(self, strs):
    table = {}
    for s in strs:
        if str(sorted(s)) in table:
            table[str(sorted(s))] += [s]
        else:
            table[str(sorted(s))] = [s]
    return table.values()
