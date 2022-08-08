# https://leetcode.com/problems/3sum/
# Solution 1 brute force (time limit exceeded) :((
def threeSum(self, nums):
    x = [[]]
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                t = [nums[i], nums[j], nums[k]]
                x.append(t)
    result = []
    for comb in x[1:]:
        if sum(comb) == 0:
            comb.sort()
            if comb not in result:
                result.append(comb)
    return result


# Solution 2
def threeSum(self, nums):
    result = []
    for i, num in enumerate(nums):
        table = {}
        idx = i+1
        target = -num
        for j, num1 in enumerate(nums[idx:]):
            remain = target - num1
            if remain in table:
                cur = [num, table[remain], remain]
                cur.sort()
                if cur not in result:
                    result.append(cur)
            else:
                table[num1] = remain

    return result


# Solution 3
def threeSum(self, nums):
    result = []
    nums.sort()

    for i, num in enumerate(nums):
        if i > 0 and num == nums[i-1]:
            continue
        l, r = i + 1, len(nums)-1
        while l < r:
            threeSum = num + nums[l] + nums[r]
            if threeSum < 0:
                l += 1
            elif threeSum > 0:
                r -= 1
            else:
                result.append([num, nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l-1] and l < r:
                    l += 1

    return result
