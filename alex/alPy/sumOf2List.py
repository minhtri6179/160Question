# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# Solution 1. create 2 number then add them
def sumOfLinkedLists(linkedListOne, linkedListTwo):
    # Write your code here.
    newList = LinkedList(0)
    curNode = newList
    num1 = 0
    num2 = 0
    head1 = linkedListOne
    head2 = linkedListTwo
    i = 0
    while head1 or head2:
        if head1:
            num1 = num1 + head1.value*pow(10, i)
            head1 = head1.next
        if head2:
            num2 = num2 + head2.value*pow(10, i)
            head2 = head2.next
        i += 1
    result = num1 + num2
    if result == 0:
        return newList
    while (result > 0):
        num = result % 10
        result = result // 10
        newNode = LinkedList(num)
        curNode.next = newNode
        curNode = newNode
    return newList.next


# Solution 2.
# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    # Write your code here.
    remain = 0
    sumOfTwoLinkedList = LinkedList(None)
    curSOTLL = sumOfTwoLinkedList

    while linkedListOne or linkedListTwo:
        if linkedListOne and linkedListTwo:
            num = linkedListOne.value + linkedListTwo.value
            linkedListOne = linkedListOne.next
            linkedListTwo = linkedListTwo.next
        elif linkedListOne:
            num = linkedListOne.value
            linkedListOne = linkedListOne.next
        else:
            num = linkedListTwo.value
            linkedListTwo = linkedListTwo.next

        unit = (num % 10) + remain
        if num // 10:
            remain = 1
        else:
            remain = 0
        newNode = LinkedList(unit)
        curSOTLL.next = newNode
        curSOTLL = newNode
    if remain == 1:
        newNode = LinkedList(1)
        curSOTLL.next = newNode
        curSOTLL = newNode
    return sumOfTwoLinkedList.next
