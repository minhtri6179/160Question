# https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# Algoexpert
# Solution
def deleteDuplicates(self, head):
    pre, cur = head, head
    while cur:
        if cur.val == pre.val:
            pre.next = cur.next
        else:
            pre = cur
        cur = cur.next
    return head
