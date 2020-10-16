/**
 * Definition for a Node.
 * struct Node {
 *     int val;
 *     struct Node *left;
 *     struct Node *right;
 *     struct Node *next;
 * };
 */

struct Node* connect(struct Node* root) {
	
    if (root == NULL) {
        return root;
    }

    struct Node* stack[5000] = {root};
    while (stack[0] != NULL) {
        int length = sizeof(stack) / sizeof(stack[0]);
        // printf("%d",length);
        // 切记这里的length其实是总的数组长度，而不是实际的元素个数。正是因为实际的元素个数
        // 不好求，所以下面多了个一旦stack[i]为空就break的逻辑（也就是这一层一旦循环完了就跳出）。
        struct Node* nextLevel[2500] = {}; int pos = 0;
        for (int i = 0; i < length; i++) {
            if (stack[i] == NULL) {
                break;
            }
            struct Node* node = stack[i];
            struct Node* preNode;
            if (node->left != NULL) nextLevel[pos++] = node->left;
            if (node->right != NULL) nextLevel[pos++] = node->right;
            if (i == 0) {
                    preNode = node;
                }
            else if (i != length-1) {
                preNode->next = node;
                preNode = node;
            }
            else {
                preNode->next = node;
            }  
        }
        memset(stack, '\0', sizeof(stack[0]));
        for (int j = 0; j < pos; j++){
                stack[j] = nextLevel[j];
            }
    }
    return root;
}

/*
https://leetcode-cn.com/submissions/detail/116315707/

58 / 58 个通过测试用例
状态：通过
执行用时: 20 ms
内存消耗: 8.9 MB

执行用时：20 ms, 在所有 C 提交中击败了60.50%的用户
内存消耗：8.9 MB, 在所有 C 提交中击败了10.81%的用户
*/
