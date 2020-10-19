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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        
        int carryFlag = 0;
        //ListNode l = ListNode(0);
        ListNode* l = new ListNode(0);
        ListNode* cur = l;
        ListNode* pre = l;

        while (l1 != NULL && l2 != NULL) {
            //cur->next = &ListNode(0);
            cur->next = new ListNode(0);
            cur->val = (l1->val + l2->val + carryFlag) % 10;
            carryFlag = (l1->val + l2->val + carryFlag) / 10;
            l1 = l1->next; l2 = l2->next; pre = cur; cur = cur->next;
        }

        if (l1 == NULL && l2 == NULL){
            if (carryFlag == 0) {
                pre->next = NULL;
                return l;
            }
            else {
                cur->val = 1;
                return l;
            }
        }
        else if (l1 == NULL && l2 != NULL) {
            while (l2 != NULL) {
                cur->next = new ListNode(0);
                cur->val = (l2->val + carryFlag) % 10;
                carryFlag = (l2->val + carryFlag) / 10;
                l2 = l2->next; pre = cur; cur = cur->next;
            }
            if (carryFlag == 0) {
                pre->next = NULL;
                return l;
            }
            else {
                cur->val = 1;
                return l;
            }
        }
        else {
            while (l1 != NULL) {
                cur->next = new ListNode(0);
                cur->val = (l1->val + carryFlag) % 10;
                carryFlag = (l1->val + carryFlag) / 10;
                l1 = l1->next; pre = cur; cur = cur->next;
            }
            if (carryFlag == 0) {
                pre->next = NULL;
                return l;
            }
            else {
                cur->val = 1;
                return l;
            }
        }
    }
};

/*
https://leetcode-cn.com/submissions/detail/113144744/

1568 / 1568 个通过测试用例
状态：通过
执行用时: 52 ms
内存消耗: 69.7 MB

执行用时：52 ms, 在所有 C++ 提交中击败了8.80%的用户
内存消耗：69.7 MB, 在所有 C++ 提交中击败了5.27%的用户
*/
