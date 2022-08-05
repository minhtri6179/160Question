# https://leetcode.com/problems/two-sum/

# Solution 1
def twoSum(self, nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

# Solution 2


def twoSum(self, nums, target):
    table = {}
    for i, num in enumerate(nums):
        remain = target - num
        if remain in table:
            return [table[remain], i]
        else:
            table[num] = i
