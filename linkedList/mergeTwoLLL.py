# https://leetcode.com/problems/merge-two-sorted-lists/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Solution 1
# O(n) time complexity; O(len(list1)+len(list2)) space complexity
def mergeTwoLists(list1, list2):
    newList = ListNode()
    head = newList
    while list1 and list2:
        if list1.val < list2.val:
            head.next = list1
            list1 = list1.next
        else:
            head.next = list2
            list2 = list2.next

        head = head.next
    if list1:
        head.next = list1
    elif list2:
        head.next = list2

    return newList.next
