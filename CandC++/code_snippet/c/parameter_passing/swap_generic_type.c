#include <stdio.h>
# include <stdlib.h>
#  include <string.h>

int swap_generic_type (void *x, void *y, int size) {
    void *tmp;
    if ((tmp = malloc(size)) == NULL) {
        return -1;
    }
    
    memcpy(tmp, x, size);
    memcpy (x, y, size);
    memcpy  (y, tmp, size);
    free(tmp);
    return 0;
}

typedef struct ListNode{
    int val;
    struct ListNode *next;
}LNODE;

struct ListNode* creat_node(int val) {
    struct ListNode* node = NULL;
    node = (struct ListNode*)malloc(sizeof(LNODE));
    if (NULL == node){
        printf("malloc failed!\n");
    }
    memset(node,0,sizeof(LNODE));
    node->val = val;
    node->next = NULL;
    return node;
}

int main()
{
    int a = 1, b = 2;
    printf("Before swap_generic_type for int: a is %d, b is %d\n", a, b);
    swap_generic_type(&a, &b, sizeof(int));
    printf("After swap_generic_type for int: a is %d, b is %d\n", a, b);

    char x = 'x', y = 'y';
    printf("Before swap_generic_type for char: x is %c, y is %c\n", x, y);
    swap_generic_type(&x, &y, sizeof(char));
    printf("After swap_generic_type for char: x is %c, y is %c\n", x, y);
    
    struct ListNode* node1 = creat_node(1);
    struct ListNode* node2 = creat_node(2);
    struct ListNode* node3 = creat_node(3);
    struct ListNode* node4 = creat_node(4);
    node3->next = node1;
    node4->next = node2;
    printf("Before swap_generic_type for struct: node3->val is %d, node3->next is %p\n", node3->val, node3->next);
    printf("Before swap_generic_type for struct: node4->val is %d, node4->next is %p\n", node4->val, node4->next);
    swap_generic_type(&node3, &node4, sizeof(struct ListNode));
    printf("After swap_generic_type for struct: node3->val is %d, node3->next is %p\n", node3->val, node3->next);
    printf("After swap_generic_type for struct: node4->val is %d, node4->next is %p\n", node4->val, node4->next);
    
    return 0;
}

/******************************************************************************
Before swap_generic_type for int: a is 1, b is 2                                                                                                 
After swap_generic_type for int: a is 2, b is 1                                                                                                  
Before swap_generic_type for char: x is x, y is y                                                                                                
After swap_generic_type for char: x is y, y is x                                                                                                 
Before swap_generic_type for struct: node3->val is 3, node3->next is 0x165a010                                                                   
Before swap_generic_type for struct: node4->val is 4, node4->next is 0x165a030                                                                   
After swap_generic_type for struct: node3->val is 4, node3->next is 0x165a030                                                                    
After swap_generic_type for struct: node4->val is 3, node4->next is 0x165a010
*******************************************************************************/
