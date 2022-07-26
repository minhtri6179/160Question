
# Brute force
from itertools import count


def val1(arr, seq):
    idxArr = 0
    countEqual = 0
    for seqNum in seq:
        for i in range(idxArr, len(arr)):
            if seqNum == arr[i]:
                countEqual += 1
                idxArr = i+1
                break
    return countEqual == len(seq)


def val2(arr, seq):
    arrI = 0
    seqI = 0
    while arrI < len(arr) and seqI < len(seq):
        if arr[arrI] == seq[seqI]:
            seqI += 1
        arrI += 1
    return seqI == len(seq)


if __name__ == '__main__':
    arr = [5, 1, 22, 25, 6, -1, 8, 10]
    seq = [5, 1, 22, 22, 25, 6, -1, 8, 10]
    print(f'Solution 1: {val1(arr, seq)}')
    print(f'Solution 2: {val2(arr, seq)}')
