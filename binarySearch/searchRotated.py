# https://leetcode.com/problems/search-in-rotated-sorted-array/
# Solution 1
def search(self, nums, target: int) -> int:
    l, r = 0, len(nums)-1
    while l <= r:
        mid = (l+r)//2
        if nums[mid] == target:
            return mid

        # Left search
        if nums[l] <= nums[mid]:
            if nums[mid] < target or nums[l] > target:
                l = mid+1
            else:
                r = mid-1

        # Right search
        else:
            if nums[mid] > target or nums[r] < target:
                r = mid-1
            else:
                l = mid+1
    return -1
