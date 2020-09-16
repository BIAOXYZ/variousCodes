/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {

        if (root == NULL){
            return root;
        }

        TreeNode* tmpNode = root->left;
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
};

/*
https://leetcode-cn.com/submissions/detail/108762238/

68 / 68 个通过测试用例
状态：通过
执行用时: 0 ms
内存消耗: 9 MB

执行用时：0 ms, 在所有 C++ 提交中击败了100.00%的用户
内存消耗：9 MB, 在所有 C++ 提交中击败了63.40%的用户
*/
