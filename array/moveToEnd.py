# Algoexpert
def moveElementToEnd(array, toMove):
    # Write your code here.
    l, r = 0, len(array)-1
    while l < r:
        if array[l] == toMove:
            while array[r] == toMove and l < r:
                r -= 1
            array[l], array[r] = array[r], array[l]
        l += 1
    return array
