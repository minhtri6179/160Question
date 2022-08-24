# https://leetcode.com/problems/move-zeroes/
# Solution 1 (n^2) time limit exceeded
class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if nums[i] == 0:
                for j in range(len(nums)-1, i, -1):
                    if nums[j] != 0:
                        nums[i], nums[j] = nums[j], nums[i]


# Solution 2
class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, 0
        while r < len(nums):
            if nums[r] == 0:
                r += 1
            else:
                nums[l], nums[r] = nums[r], nums[l]
                l, r = l+1, r+1
