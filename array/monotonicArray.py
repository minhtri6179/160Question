# https://www.algoexpert.io/questions/monotonic-array
# Solution 1
class Solution:
    def isMonotonic(self, nums) -> bool:
        if len(nums) <= 1:
            return True
        isGreater = False
        for i in range(len(nums)-1):
            if nums[i+1] > nums[i]:
                isGreater = True
                break
        if isGreater:
            for i in range(len(nums)-1):
                if nums[i] > nums[i+1]:
                    return False
            return True
        else:
            for i in range(len(nums)-1):
                if nums[i] < nums[i+1]:
                    return False
            return True


# Solution 2
def isMonotonic(nums):
    trendingDown = True
    trendingUp = True
    for i in range(len(nums)-1):
        if nums[i] < nums[i+1]:
            trendingDown = False
        if nums[i] > nums[i+1]:
            trendingUp = False

    return trendingDown or trendingUp
