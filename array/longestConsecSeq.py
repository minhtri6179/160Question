# https://leetcode.com/problems/longest-consecutive-sequence/

# Solution 1 O(Nlog(N))
def longestConsecutive(nums):
    nums.sort()
    count = 0
    print(nums)
    for i, num in enumerate(nums):
        if i+1 < len(nums) and nums[i+1] == num:
            count -= 1
        count += 1
        if i+1 < len(nums) and nums[i+1] - num > 1:
            break
    return count

# Solution 2


def longestConsecutive(self, nums):
    a = set()
    for num in nums:
        a.add(num)
    longest = 0
    for num in a:
        if (num-1) not in a:
            count = 1
            while (num+count) in a:
                count += 1
            if count > longest:
                longest = count

    return longest
