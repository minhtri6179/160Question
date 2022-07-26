
# Brute force
def twoSum1(arr, target):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                return [arr[i], arr[j]]

    return -1

# Hash map


def twoSum2(arr, target):
    table = {}
    for num in arr:
        remain = target - num
        if remain in table:
            return [num, remain]
        else:
            table[num] = remain

    return -1


if __name__ == '__main__':
    arr = [3, 5, -4, 8, 11, 1, -1, 6]
    targetSum = 10
    print(f'Solution 1: {twoSum1(arr, targetSum)}')
    print(f'Solution 2: {twoSum2(arr, targetSum)}')
