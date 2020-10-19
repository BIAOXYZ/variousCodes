/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* partition(struct ListNode* head, int x){
    //if (NULL == head){
    //    return -1;
    //}

    struct ListNode* small = (struct ListNode *)malloc(sizeof(struct ListNode));
    struct ListNode* large = (struct ListNode *)malloc(sizeof(struct ListNode));
    struct ListNode* curr_small = small;
    struct ListNode* curr_large = large;

    while (head != NULL){
        if (head->val < x){
            curr_small->next = head;
            curr_small = curr_small->next;
        }
        else{
            curr_large->next = head;
            curr_large = curr_large->next;
        }
        head = head->next;
    }

    curr_large->next = NULL;
    curr_small->next = large->next;
    return small->next;
}
"""
https://leetcode-cn.com/submissions/detail/54908515/

166 / 166 个通过测试用例
状态：通过
执行用时: 4 ms
内存消耗: 5.5 MB
"""
