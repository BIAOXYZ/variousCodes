/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* partition(ListNode* head, int x) {
        
        ListNode* dummyHeadSmall = new ListNode(0);
        ListNode* dummyHeadLarge = new ListNode(0);
        ListNode* small = dummyHeadSmall;
        ListNode* large = dummyHeadLarge;
        ListNode* curr = head;

        while (curr != NULL) {
            ListNode* nxt = curr->next;
            if (curr->val < x) {
                small->next = curr;
                small = small->next;
            } else {
                large->next = curr;
                large = large->next;
            }
            curr->next = nullptr;
            curr = nxt;
        }

        small->next = dummyHeadLarge->next;
        return dummyHeadSmall->next;

    }
};

/*
https://leetcode-cn.com/submissions/detail/135504883/

166 / 166 个通过测试用例
状态：通过
执行用时: 8 ms
内存消耗: 7.1 MB

执行用时：8 ms, 在所有 C++ 提交中击败了59.25%的用户
内存消耗：7.1 MB, 在所有 C++ 提交中击败了56.64%的用户
*/
