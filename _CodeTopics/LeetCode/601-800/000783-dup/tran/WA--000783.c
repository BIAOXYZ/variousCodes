/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

#define MIN(a, b) ((a) < (b) ? (a) : (b))
#define MAX_ARR_SIZE 101
int length = 0;

void dfs_inorder(struct TreeNode* node, int *vals) {
    if (node == NULL) {
        return;
    }
    dfs_inorder(node->left, vals);
    vals[length++] = node->val;
    dfs_inorder(node->right, vals);
}

int minDiffInBST(struct TreeNode* root){
    unsigned int vals[MAX_ARR_SIZE];
    dfs_inorder(root, vals);
    int res = vals[1] - vals[0];
    for (int i = 2; i < length; ++i) {
        res = MIN(res, vals[i] - vals[i-1]);
        if (res == 1)
            break;
    }
    return res;
}

/*
https://leetcode-cn.com/submissions/detail/167199966/

3 / 46 个通过测试用例
状态：解答错误

输入：
[96,12,null,null,13,null,52,29]
输出：
0
预期：
1
*/
