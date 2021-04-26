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
        vals.push_back(node->val);
        dfs_inorder(node->right);
    }

    int rangeSumBST(TreeNode* root, int low, int high) {
        dfs_inorder(root);
        int res = 0;
        for (auto val : vals) {
            if (val >= low && val <= high) {
                res += val;
            }
        }
        return res;
    }
};

/*
https://leetcode-cn.com/submissions/detail/172320399/

41 / 41 个通过测试用例
状态：通过
执行用时: 128 ms
内存消耗: 65.9 MB

执行用时：128 ms, 在所有 C++ 提交中击败了96.14%的用户
内存消耗：65.9 MB, 在所有 C++ 提交中击败了5.04%的用户
*/
