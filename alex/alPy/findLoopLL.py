# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(n) for time complexity and O(n) for speed
def findLoop(head):
    # Write your code here
    table = {}
    cur = head
    while cur:
        if cur.next in table:
            return cur.next
        else:
            table[cur] = cur
        cur = cur.next
