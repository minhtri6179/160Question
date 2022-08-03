# https://leetcode.com/problems/add-two-numbers

# Solution 1
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):

        remain = 0
        sumOfTwoLinkedList = ListNode(0)
        curSOTLL = sumOfTwoLinkedList
        while l1 or l2:
            if l1 and l2:
                num = l1.val + l2.val
                l1 = l1.next
                l2 = l2.next
            elif l1:
                num = l1.val
                l1 = l1.next
            else:
                num = l2.val
                l2 = l2.next
            unit = (num % 10) + remain
            if unit // 10:
                remain = 1
                unit = unit % 10
            else:
                if num // 10:
                    remain = 1
                else:
                    remain = 0
            newNode = ListNode(unit)
            curSOTLL.next = newNode
            curSOTLL = newNode
        if remain == 1:
            newNode = ListNode(1)
            curSOTLL.next = newNode
            curSOTLL = newNode
        return sumOfTwoLinkedList.next


# Solution 2
class Solution:
    def addTwoNumbers(self, l1, l2):
        newList = ListNode(0)
        cur = newList
        cache = 0

        while l1 or l2 or cache != 0:
            l1val = l1.val if l1 else 0
            l2val = l2.val if l2 else 0
            num = l1val + l2val + cache
            cache = num // 10
            num = num % 10
            cur.next = ListNode(num)
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return newList.next
