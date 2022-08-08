# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Solution 1 (time limit exceeded)
def maxProfit(self, prices) -> int:
    maxPf = 0
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            cur = prices[j] - prices[i]
            if cur > maxPf:
                maxPf = cur

    return maxPf

# Solution 2


def maxProfit(self, prices):
    maxPf = 0
    i, j = 0, 1
    while j < len(prices):
        if prices[j] > prices[i]:
            curPf = prices[j]-prices[i]
            maxPf = max(curPf, maxPf)
        else:
            i = j
        j += 1
    return maxPf
