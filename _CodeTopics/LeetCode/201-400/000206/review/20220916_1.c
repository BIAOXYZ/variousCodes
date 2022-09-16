/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* reverseList(struct ListNode* head){

    if (head == NULL || head->next == NULL) {
        return head;
    }
    struct ListNode* res = reverseList(head->next);
    head->next->next = head;
    head->next = NULL;
    return res;
}

/*
https://leetcode.cn/submissions/detail/363607530/

执行用时：
4 ms
, 在所有 C 提交中击败了
81.99%
的用户
内存消耗：
6.6 MB
, 在所有 C 提交中击败了
5.06%
的用户
通过测试用例：
28 / 28
*/
