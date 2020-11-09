#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// 树的struct定义放这儿吧，但是这个例子没用到。
// struct TreeNode {
//     int val;
//     struct TreeNode *left;
//     struct TreeNode *right;
// };


// 这个是LeetCode原版的，结构体定义完没有带别名。
// 一个问题是，结构体别名的指针形式不知道为啥不行。先不管了。
// struct ListNode {
//     int val;
//     struct ListNode *next;
// };
struct ListNode {
    int val;
    struct ListNode *next;
}LNODE, *LNODE_PTR;

/*
后来知道为啥结构体别名的指针形式不行了，因为忘了typedef了。。。如果前面ListNode定义时加上typedef：
typedef struct ListNode {
    int val;
    struct ListNode *next;
}LNODE, *LNODE_PTR;

则下面三种都可以成功创建指向ListNode的指针：
    struct ListNode* node5 = creat_node(5);
    LNODE* node5 = creat_node(5);
    LNODE_PTR node5 = creat_node(5);
*/

struct ListNode* creat_node(int val) {
    struct ListNode* node = NULL;
    // 我甚至都没想起来malloc是stdlib.h库，memset是string.h库的。
    node = (struct ListNode*)malloc(sizeof(LNODE));
    if (NULL == node){
        printf("malloc failed!\n");
    }
    memset(node,0,sizeof(LNODE));
    node->val = val;
    node->next = NULL;
    return node;
}

void change_curr_to_next(struct ListNode* currNode) {
    currNode = currNode->next;
    return;
}

void ptr_change_curr_to_next(struct ListNode** ptr_to_currNode) {
    // 这句的括号不能省略。
    *ptr_to_currNode = (*ptr_to_currNode)->next;
    return;
}

void double_val(struct ListNode* currNode) {
    currNode->val = currNode->val * 2;
    return;
}


int main()
{
    struct ListNode* node1 = creat_node(1);
    struct ListNode* node2 = creat_node(2);
    struct ListNode* node3 = creat_node(3);
    struct ListNode* node4 = creat_node(4);
    
    node1->next = node2;
    node3->next = node4;
    
    change_curr_to_next(node1);
    printf("After change without pointer, node1 is not the next, because its value is unchanged: %d\n", node1->val);
    ptr_change_curr_to_next(&node3);
    printf("After change with pointer, node3 is the next, because its value is changed: %d\n", node3->val);
    
    struct ListNode* node5 = creat_node(5);
    
    double_val(node5);
    printf("But just change member of the struct does not need 2-level pointer: %d", node5->val);
    return 0;
}

/******************************************************************************
After change without pointer, node1 is not the next, because its value is unchanged: 1                                
After change with pointer, node3 is the next, because its value is changed: 4                                         
But just change member of the struct does not need 2-level pointer: 10 
*******************************************************************************/
