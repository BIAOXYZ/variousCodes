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
    void dfs_inorder(TreeNode* node, vector<int>& res) {
        if (node->left != NULL) {
            dfs_inorder(node->left, res);
        }
        res.push_back(node->val);
        if (node->right != NULL) {
            dfs_inorder(node->right, res);
        }
    }
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> res;
        if (root == NULL) {
            return res;
        }
        dfs_inorder(root, res);
        return res;
    }
};

/*
https://leetcode-cn.com/submissions/detail/112296947/

68 / 68 个通过测试用例
状态：通过
执行用时: 0 ms
内存消耗: 8.1 MB

执行用时：0 ms, 在所有 C++ 提交中击败了100.00%的用户
内存消耗：8.1 MB, 在所有 C++ 提交中击败了16.95%的用户
*/
/*
哎哟我去，我也碰到执行时间0毫秒的情况了。。。果然就击败100%了。。。
*/
