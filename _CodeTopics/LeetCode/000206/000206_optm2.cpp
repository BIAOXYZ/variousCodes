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
    ListNode* reverseList(ListNode* head) {

        ListNode* pre = NULL;
        ListNode* curr = head;
        ListNode* next = NULL;

        while (curr != NULL) {
            next = curr->next;
            curr->next = pre;
            pre = curr;
            curr = next;
        }
        return pre;
    }
};

"""
https://leetcode-cn.com/submissions/detail/105023232/

27 / 27 个通过测试用例
状态：通过
执行用时: 12 ms
内存消耗: 8.5 MB
"""
"""
执行用时：12 ms, 在所有 C++ 提交中击败了71.81%的用户
内存消耗：8.5 MB, 在所有 C++ 提交中击败了48.17%的用户
"""
