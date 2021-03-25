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
    ListNode* deleteDuplicates(ListNode* head) {

        ListNode* curr = head;
        while (curr != nullptr and curr->next != nullptr) {
            if (curr->val != curr->next->val) {
                curr = curr->next;
            } else {
                curr->next = curr->next->next;
            }
        }
        return head;
    }
};

/*
https://leetcode-cn.com/submissions/detail/159901423/

165 / 165 个通过测试用例
状态：通过
执行用时: 8 ms
内存消耗: 11.2 MB

执行用时：8 ms, 在所有 C++ 提交中击败了95.93%的用户
内存消耗：11.2 MB, 在所有 C++ 提交中击败了63.92%的用户
*/
