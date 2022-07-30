using namespace std;

// This is an input struct. Do not edit.
class LinkedList
{
public:
    int value;
    LinkedList *next = nullptr;

    LinkedList(int value) { this->value = value; }
};

LinkedList *removeDuplicatesFromLinkedList(LinkedList *linkedList)
{
    // Write your code here.
    LinkedList *cur = linkedList;
    LinkedList *pre = linkedList;
    cur = cur->next;
    while (cur != nullptr)
    {
        if (cur->value == pre->value)
        {
            pre->next = cur->next;
        }
        else
        {
            pre = pre->next;
        }
        cur = cur->next;
    }
    return linkedList;
}
