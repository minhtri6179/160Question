# https://leetcode.com/problems/linked-list-cycle/

# Solution 1
# O(n) time complexity; O(1) space complexity
def hasCycle(head) -> bool:
    first, second = head, head
    while second and second.next:
        first = first.next
        second = second.next.next
        if second == first:
            return True
    return False


# Solution 2
# O(n) time complexity; O(n) space complexity
def hasCycle(head) -> bool:
    l = set()
    cur = head

    while cur:
        if cur in l:
            return True
        else:
            l.add(cur)
        cur = cur.next
    return False
