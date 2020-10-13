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
    ListNode* swapPairs(ListNode* head) {

        if (head == nullptr || head->next == nullptr) {
            return head;
        }

        /*
        ListNode* node1 = head, node2 = head->next;

        Line 19: Char 33: error: no viable conversion from 'ListNode *' to 'ListNode'
        ListNode* node1 = head, node2 = head->next;
                              ^       ~~~~~~~~~~
        */
        /*
        没明白上面那句为啥会报错，我如果用类似的定义加初始化的方式对int型变量就没问题，比如：
        int a = 3, b=5;
        所以最后直接写成两行了。。。
        */
        ListNode* node1 = head;
        ListNode* node2 = head->next;
        node1->next = swapPairs(node2->next);
        node2->next = node1;
        return node2;

    }
};

/*
https://leetcode-cn.com/submissions/detail/115398200/

55 / 55 个通过测试用例
状态：通过
执行用时: 4 ms
内存消耗: 7.4 MB

执行用时：4 ms, 在所有 C++ 提交中击败了66.38%的用户
内存消耗：7.4 MB, 在所有 C++ 提交中击败了5.30%的用户
*/
