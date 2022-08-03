# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Solution 1
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head, n: int):
        first, second = head, head
        for _ in range(n):
            second = second.next
        if second is None:
            return head.next
        while second.next:
            first = first.next
            second = second.next
        first.next = first.next.next

        return head
