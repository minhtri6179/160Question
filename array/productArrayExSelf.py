# https://leetcode.com/problems/product-of-array-except-self/
# Solution 1 O(N) space
def productExceptSelf(self, nums):
    prefix = [1] * len(nums)
    postfix = [1] * len(nums)

    cur = 1
    for i, num in enumerate(nums):
        cur *= num
        prefix[i] *= cur

    cur = 1
    for i in range(len(nums)-1, -1, -1):
        cur *= nums[i]
        postfix[i] *= cur

    result = [1] * len(nums)
    for i in range(len(nums)):
        a = prefix[i-1] if i > 0 else 1
        b = postfix[i+1] if (i+1) < len(nums) else 1
        result[i] = a*b

    return result

# Solution 2 (with extra space O(1))


def productExceptSelf(self, nums):
    result = [1] * len(nums)
    # [2, 3, 4, 5]
    # [(1), 2, 2*3, 2*2*4]
    pre = 1
    for i, num in enumerate(nums):
        result[i] *= pre
        pre *= num

    # [3*4*5, 4*5, 5, (1)]
    pos = 1
    for i in range(len(nums)-1, -1, -1):
        result[i] *= pos
        pos *= nums[i]

    return result
