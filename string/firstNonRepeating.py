# Algoexpert
def firstNonRepeatingCharacter(string):
    # Write your code here.
    table = {}
    for i, ch in enumerate(string):
        if ch in table:
            table[ch] = -1
        else:
            table[ch] = i
    print(table)
    for k in table:
        if table[k] != -1:
            return table[k]

    return -1
