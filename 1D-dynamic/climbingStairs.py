# https://leetcode.com/problems/climbing-stairs/

# Solution 1 BruteForce
def climbStairs(self, n: int) -> int:
    """
    Time complexity: O(2^n)
    Space complexity: O(n)
    """
    return self.bruteForce(0, n)


def bruteForce(self, start, end):
    if start > end:
        return 0

    if start == end:
        return 1
    return self.bruteForce(start + 1, end) + self.bruteForce(start + 2, end)


# Solution 2
def climbStairs(self, n: int) -> int:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    cache = {}
    return self.bruteForce(0, n, cache)


def bruteForceMemozation(self, start, end, cache):
    if start > end:
        return 0

    if start == end:
        return 1
    if start in cache:
        return cache[start]
    cache[start] = self.bruteForceMemozation(
        start + 1, end, cache) + self.bruteForceMemozation(start + 2, end, cache)

    return cache[start]

# Solution 3 (1D - dynamic programming)


def climbStairs(self, n: int) -> int:
    i = 1
    j = 1
    for k in range(1, n):
        temp = j
        j = i + j
        i = temp
    return j
