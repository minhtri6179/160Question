# https://leetcode.com/problems/contains-duplicate/

# Solution 1 (time limit exceeded :(( )
def containsDuplicate(self, nums) -> bool:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False

# Solution 2 (hash table)


def containsDuplicate(self, nums) -> bool:
    table = {}
    for num in nums:
        if num in table:
            return True
        else:
            table[num] = True
    return False

# Solution 3 (hash set)


def containsDuplicate(self, nums) -> bool:
    hashSet = set()
    for num in nums:
        if num in hashSet:
            return True
        else:
            hashSet.add(num)
    return False
