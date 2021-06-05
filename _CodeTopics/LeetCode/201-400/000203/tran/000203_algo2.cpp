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

        if (head == nullptr) {
            return nullptr;
        } else if (head->val != val) {
            head->next = this->removeElements(head->next, val);
        } else {
            // 加不加 this 都行。
            return removeElements(head->next, val);
        }
        return head;
    }
};

/*
https://leetcode-cn.com/submissions/detail/184195463/

66 / 66 个通过测试用例
状态：通过
执行用时: 16 ms
内存消耗: 15.1 MB

执行用时：16 ms, 在所有 C++ 提交中击败了99.70%的用户
内存消耗：15.1 MB, 在所有 C++ 提交中击败了5.03%的用户
*/
