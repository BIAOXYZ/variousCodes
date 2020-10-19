/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode* reverseList(struct ListNode* head){

        struct ListNode* pre = NULL;
        struct ListNode* curr = head;

        while (curr != NULL) {
            struct ListNode* next = curr->next;
            curr->next = pre;
            pre = curr;
            curr = next;
        }
        return pre;
}

"""
https://leetcode-cn.com/submissions/detail/105021785/

27 / 27 个通过测试用例
状态：通过
执行用时: 4 ms
内存消耗: 6.1 MB
"""
"""
执行用时：4 ms, 在所有 C 提交中击败了85.75%的用户
内存消耗：6.1 MB, 在所有 C 提交中击败了16.03%的用户
"""
