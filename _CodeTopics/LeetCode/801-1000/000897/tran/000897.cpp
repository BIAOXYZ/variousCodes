/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
private:
    vector<int> vals;
public:
    void dfs_inorder(TreeNode* node) {
        if (node == nullptr) {
            return;
        }
        dfs_inorder(node->left);
        this->vals.push_back(node->val);
        dfs_inorder(node->right);
    }

    TreeNode* increasingBST(TreeNode* root) {
        dfs_inorder(root);
        TreeNode* newRoot = new TreeNode(this->vals[0]);
        newRoot->left = nullptr;
        TreeNode* curr = newRoot;
        for (int i = 1; i < this->vals.size(); ++i) {
            curr->left = nullptr;
            curr->right = new TreeNode(this->vals[i]);
            curr = curr->right;
        }
        return newRoot;
    }
};

/*
https://leetcode-cn.com/submissions/detail/171592815/

37 / 37 个通过测试用例
状态：通过
执行用时: 4 ms
内存消耗: 7.8 MB

执行用时：4 ms, 在所有 C++ 提交中击败了51.71%的用户
内存消耗：7.8 MB, 在所有 C++ 提交中击败了20.79%的用户
*/
