
struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};
class Solution
{
public:
    ListNode *middleNode(ListNode *head)
    {
        ListNode *curI;
        ListNode *curJ;
        while (curJ->next != nullptr)
        {
            curI = curI->next;
            curJ = curJ->next->next;
            if (curJ == nullptr)
                return curI;
        }
        return curI;
    }
};