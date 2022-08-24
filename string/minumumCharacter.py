# Input: ['this', 'that', 'did', 'dead', 'them!', 'a']
# Output: ['t', 't', 'h', 'i', 's', 'a', 'd', 'd', 'e', 'e', 'm', '!']
# Output:
# Solution 1
def minimumCharactersForWords(words):
    # Write your code here
    min_table = {}
    for word in words:
        cur_table = {}
        for ch in word:
            cur_table[ch] = cur_table.get(ch, 0)+1
        for k in cur_table:
            if cur_table[k] > min_table.get(k, 0):
                min_table[k] = cur_table[k]

    result = []
    for k in min_table:
        for _ in range(min_table[k]):
            result.append(k)
    return result
