# https://leetcode.com/problems/minimum-absolute-difference/
# Solution 1 O(nlog(n) + n^2 + n^2) :D
class Solution:
    def minimumAbsDifference(self, arr):
        result = []
        arr.sort()
        smallest = abs(arr[0]-arr[1])
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if abs(arr[i]-arr[j]) < smallest:
                    smallest = abs(arr[i]-arr[j])

        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if abs(arr[i]-arr[j]) == smallest:
                    result.append([arr[i], arr[j]])

        return result

# Solution 2  O(nlog(n) + n + n)


class Solution:
    def minimumAbsDifference(self, arr):
        result = []
        arr.sort()
        smallest = arr[1]-arr[0]
        for i in range(len(arr)-1):
            if arr[i+1]-arr[i] < smallest:
                smallest = arr[i+1]-arr[i]

        for i in range(len(arr)-1):
            if arr[i+1]-arr[i] == smallest:
                result.append([arr[i], arr[i+1]])

        return result
