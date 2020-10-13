/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* swapPairs(struct ListNode* head){

    if (head == NULL || head->next == NULL) {
        return head;
    }

    /*
    struct ListNode* node1 = head, node2 = head->next;

    solution.c: In function ‘swapPairs’
    Line 16: Char 44: error: invalid initializer
        struct ListNode* node1 = head, node2 = head->next;
                                            ^~~~    
    */
    /*
    遇到了跟 000024_algo2.cpp 一样的问题：在同一行给两个ListNode*同时定义和初始化就报错。。。
    但是对于基本类型如int就可以： int a = 3, b=5;
    */
    struct ListNode* node1 = head;
    struct ListNode* node2 = head->next;
    node1->next = swapPairs(node2->next);
    node2->next = node1;
    return node2;

}

/*
https://leetcode-cn.com/submissions/detail/115402494/

55 / 55 个通过测试用例
状态：通过
执行用时: 4 ms
内存消耗: 5.3 MB

执行用时：4 ms, 在所有 C 提交中击败了43.14%的用户
内存消耗：5.3 MB, 在所有 C 提交中击败了88.99%的用户
*/
