# https://leetcode.com/problems/top-k-frequent-elements/
import heapq

# Solution 1


def topKFrequent(self, nums, k: int):
    table = {}
    for num in nums:
        table[num] = table.get(num, 0) + 1

    a = [(x, y) for (x, y) in table.items()]
    a.sort(key=lambda x: x[1], reverse=True)
    result = [x[0] for x in a[:k]]
    return result
# Solution 2


def topKFrequent(self, nums, k: int):
    table = {}
    for num in nums:
        table[num] = table.get(num, 0) + 1

    a = [(y, x) for (x, y) in table.items()]
    result = []
    for _ in range(k):
        heapq._heapify_max(a)
        x = heapq._heappop_max(a)
        result.append(x[1])

    return result
# Solution 3


def topKFrequent(self, nums, k: int):
    table = {}
    for num in nums:
        table[num] = table.get(num, 0) + 1

    freq = [[] for _ in range(len(nums)+1)]
    for ke, v in table.items():
        freq[v].append(ke)

    result = []
    for i in range(len(freq)-1, 0, -1):
        for n in freq[i]:
            result.append(n)
            if len(result) == k:
                return result
