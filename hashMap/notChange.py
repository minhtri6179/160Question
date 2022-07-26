
# Brute force
def combine(arr):
    if len(arr) == 0:
        return [[]]
    firstE = arr[0]
    rest = arr[1:]
    remainArr = combine(rest)

    combs = []
    for num in remainArr:
        combs += [num, num+[firstE]]
    return combs


def notChange1(arr):
    combs = combine(arr)
    result = [sum(comb) for comb in combs]
    result.sort()
    k = 0
    for num in list(set(result)):
        if k != num:
            return k
        k += 1
    return k
# Hash map


# Magic
def notChange2(arr):
    arr.sort()
    cur = 0
    for num in arr:
        if cur+1 < num:
            return cur+1
        cur += num
    return cur+1


if __name__ == '__main__':
    coins = [5, 7, 1, 1, 2, 3, 22]

    print(f'Solution 1: {notChange1(coins)}')
    print(f'Solution 2: {notChange2(coins)}')
