

def sortedSquare1(arr):
    for i in range(len(arr)):
        arr[i] = arr[i]*arr[i]
    arr.sort()
    return arr


def sortedSquare2(arr):
    result = [0 for _ in arr]
    i = 0
    j = len(arr) - 1
    for idx in range(len(arr)-1, -1, -1):
        if abs(arr[i]) < abs(arr[j]):
            result[idx] = arr[j]*arr[j]
            j -= 1
        else:
            result[idx] = arr[i]*arr[i]
            i += 1
    return result


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f'Solution 1: {sortedSquare1(arr)}')
    print(f'Solution 2: {sortedSquare2(arr2)}')
