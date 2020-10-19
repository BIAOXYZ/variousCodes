/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

struct TreeNode* invertTree(struct TreeNode* root){

    if (root == NULL) {
        return root;
    }

    struct TreeNode* tmpNode = root->left;
    root->left = root->right;
    root->right = tmpNode;

    if (root->left != NULL) {
        invertTree(root->left);
    }
    if (root->right != NULL) {
        invertTree(root->right);
    }
    return root;
}

/*
https://leetcode-cn.com/submissions/detail/108765267/

68 / 68 个通过测试用例
状态：通过
执行用时: 4 ms
内存消耗: 5.3 MB

执行用时：4 ms, 在所有 C 提交中击败了43.82%的用户
内存消耗：5.3 MB, 在所有 C 提交中击败了89.00%的用户
*/
