/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) {

        struct ListNode* dummyHead = new ListNode(0);
        dummyHead->next = head;
        struct ListNode* prev = dummyHead;

        while (prev->next) {
            if (prev->next->val != val) {
                prev = prev->next;
            } else {
                prev->next = prev->next->next;
            }
        }
        return dummyHead->next;
    }
};

/*
https://leetcode-cn.com/submissions/detail/184194128/

66 / 66 个通过测试用例
状态：通过
执行用时: 28 ms
内存消耗: 14.6 MB

执行用时：28 ms, 在所有 C++ 提交中击败了68.56%的用户
内存消耗：14.6 MB, 在所有 C++ 提交中击败了56.59%的用户
*/
