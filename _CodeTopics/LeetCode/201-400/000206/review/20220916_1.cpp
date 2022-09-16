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
    ListNode* reverseList(ListNode* head) {

        if (!head || !head->next) {
            return head;
        }
        ListNode* res = reverseList(head->next);
        head->next->next = head;
        head->next = nullptr;
        return res;
    }
};

/*
https://leetcode.cn/submissions/detail/363590847/

执行用时：
4 ms
, 在所有 C++ 提交中击败了
95.89%
的用户
内存消耗：
8.3 MB
, 在所有 C++ 提交中击败了
9.69%
的用户
通过测试用例：
28 / 28
*/
