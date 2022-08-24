# Smallest Difference
# Solution1 (N^2)
def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    smallest = abs(arrayOne[0]-arrayTwo[0])
    cache = []
    for num1 in arrayOne:
        for num2 in arrayTwo:
            if abs(num1-num2) < smallest:
                smallest = abs(num1-num2)
                cache = [num1, num2]

    return cache
# Solution2 (nlog(n) + mlog(m)) (sort)


def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    arrayOne.sort()
    arrayTwo.sort()
    i, j = 0, 0
    result = []
    smallest = abs(arrayOne[0]-arrayTwo[0])
    while i < len(arrayOne) and j < len(arrayTwo):
        num1, num2 = arrayOne[i], arrayTwo[j]
        if num1 < num2:
            i += 1
            cur = num1-num2
        elif num1 > num2:
            j += 1
            cur = num1-num2
        else:
            return [num1, num2]
        if abs(cur) < smallest:
            smallest = abs(cur)
            result = [num1, num2]

    return result
