# https://leetcode.com/problems/rotate-list/

# Solution 1
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head, k):
        newList = ListNode(0)
        newHead = newList
        first, second = head, head
        countK = 1
        num = 0
        cur = head
        while cur:
            cur = cur.next
            num += 1
        if head is None:
            return head
        k = k % num
        while countK <= k:
            second = second.next
            countK += 1
        if second is None:
            return head
        while second.next:
            second = second.next
            first = first.next
        newHead.next = first.next
        first.next = None
        while newHead.next:
            newHead = newHead.next
        newHead.next = head
        return newList.next


# Solution 2
class Solution:
    def rotateRight(self, head, k: int):
        if head is None:
            return head
        # finding length of linked list
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        k = k % length

        if k == 0:
            return head
        # Change linking between node
        cur = head
        for i in range(length-k-1):
            cur = cur.next
        newHead = cur.next
        cur.next = None
        tail.next = head
        return newHead
