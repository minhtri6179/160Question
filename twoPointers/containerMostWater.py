# https://leetcode.com/problems/container-with-most-water/

# Solution 1 Brute force (time limit exceeded:( )
def maxArea(self, height) -> int:
    maxArea = 0
    for i, num in enumerate(height):
        for j in range(i+1, len(height)):
            tempArea = min(height[i], height[j])*(j-i)
            if tempArea > maxArea:
                maxArea = tempArea
    return maxArea


# Solution 2 (two pointer)
def maxArea(self, height) -> int:
    maxArea = 0
    i, j = 0, len(height)-1
    while i < j:
        curArea = min(height[i], height[j])*(j-i)
        if curArea > maxArea:
            maxArea = curArea
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    return maxArea
