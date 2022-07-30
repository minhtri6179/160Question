# https://leetcode.com/problems/reverse-linked-list/


# Solution 1
# O(n) time complexity; O(1) space complexity
def reverseList(head):
    pre = None
    cur = head
    while cur:
        nxt = cur.next
        cur.next = pre
        pre = cur
        cur = nxt
    return pre


# Solution 2
# O(n) time complexity;
# O(n) space complexity to store node each traversal
def reverseList(head):
    cur = head
    pre = None
    track_off = []
