# https://leetcode.com/problems/reorder-list/

# Solution 1
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head):
        """
        Do not return anything, modify head in-place instead.
        """
        # Firstly, split 2 linkedlist to 2 sub linklist
        first, second = head, head
        while second and second.next:
            first = first.next
            second = second.next.next

        # Reverse 2th list
        cur = first.next
        pre = first.next = None
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        # Pre is head of reverse 2th ll

        # Merge 2 ll to gain result
        first, second = head, pre
        while second:
            t1, t2 = first.next, second.next
            first.next = second
            second.next = t1
            first, second = t1, t2
