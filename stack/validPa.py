# https://leetcode.com/problems/valid-parentheses/
# Solution 1
def isValid(self, s: str) -> bool:
    a = []
    left = ['(', '[', '{']
    right = [')', ']', '}']
    pre = None

    for ch in s:
        if ch in left:
            a.append(ch)
        else:
            if len(a) == 0:
                return False
            if left.index(pre) == right.index(ch):
                a.pop()
                ch = a[-1] if len(a) != 0 else None
            else:
                return False
        pre = ch
    return (len(a) == 0)

# Solution 2


def isValid(self, s: str) -> bool:
    stack = []
    openClose = {'(': ')', '[': ']', '{': '}'}

    for ch in s:
        if ch in openClose.values():
            if stack and openClose[stack[-1]] == ch:
                stack.pop()
            else:
                return False
        else:
            stack.append(ch)

    if len(stack) == 0:
        return True
    return False
