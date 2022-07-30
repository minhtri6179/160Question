# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    # Write your code here.
    cur = head
    pre = head
    counterCur = 1
    while (counterCur <= k):
        cur = cur.next
        counterCur += 1

    if cur is None:
        head.value = head.next.value
        head.next = head.next.next
        return
    while (cur.next is not None):
        cur = cur.next
        pre = pre.next

    pre.next = pre.next.next


# Solution 2
def removeKthNodeFromEnd(head, k):
    # Write your code here.
    cur = head
    cur2 = head
    pre2 = head
    lenList = 0
    while cur is not None:
        lenList += 1
        cur = cur.next
    pos = lenList - k
    countPos = 0
    while cur2 is not None:
        if countPos == pos:
            # delete
            pre2.next = cur2.next
        pre2 = cur2
        cur2 = cur2.next
        countPos += 1
