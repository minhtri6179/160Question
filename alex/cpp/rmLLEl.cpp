
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
    ListNode *removeElements(ListNode *head, int val)
    {
        ListNode *pre = head;
        ListNode *cur = head;

        while (cur != nullptr)
        {
            if (cur->val == val)
            {
                if (pre == cur)
                {
                    pre = pre->next;
                    head = head->next;
                }
                else
                    pre->next = cur->next;
            }
            else
                pre = cur;

            cur = cur->next;
        }
        return head;
    }
};