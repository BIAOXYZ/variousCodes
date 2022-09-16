/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* reverseList(struct ListNode* head){

    if (!head || !head->next) {
        return head;
    }
    struct ListNode* pre = head;
    struct ListNode* cur = head->next;
    pre->next = NULL;

    while (cur) {
        struct ListNode* nxt = cur->next;
        cur->next = pre;
        pre = cur;
        cur = nxt;
    }
    return pre;
}

/*
https://leetcode.cn/submissions/detail/363605023/

执行用时：
4 ms
, 在所有 C 提交中击败了
81.99%
的用户
内存消耗：
6.4 MB
, 在所有 C 提交中击败了
12.46%
的用户
通过测试用例：
28 / 28
*/
