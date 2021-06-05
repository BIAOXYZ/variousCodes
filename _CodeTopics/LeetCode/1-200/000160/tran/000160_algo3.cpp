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
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        
        unordered_set<ListNode*> setA;
        while (headA != nullptr) {
            setA.insert(headA);
            headA = headA->next;
        }
        while (headB != nullptr) {
            // 这里当然可以写成： auto it = setA.find(headB);
            std::unordered_set<ListNode*>::iterator it = setA.find(headB);
            if (it != setA.end()) {
                return headB;
            }
            headB = headB->next;
        }
        return nullptr;
    }
};

/*
https://leetcode-cn.com/submissions/detail/184220873/

39 / 39 个通过测试用例
状态：通过
执行用时: 64 ms
内存消耗: 16.8 MB

执行用时：64 ms, 在所有 C++ 提交中击败了27.04%的用户
内存消耗：16.8 MB, 在所有 C++ 提交中击败了10.76%的用户
*/
