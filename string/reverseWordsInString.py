# Input: string = " this   is the best example"
# Output: "example best the is   this "
# Solution 1
def reverseWordsInString(s):
    words = []
    start = 0
    for i, ch in s:
        if ch == ' ':
            words.append(s[start:i])
            start = i
        else:
            if s[start] == ' ':
                words.append(' ')
                start = i
    words.append(s[start:])
    return ''.join(words[::-1])
