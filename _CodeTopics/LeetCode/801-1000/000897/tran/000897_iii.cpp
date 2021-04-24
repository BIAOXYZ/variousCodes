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

// 不使用成员变量的版本。
class Solution {
public:
    void dfs_inorder(TreeNode* node, vector<int>& vals) {
        if (node == nullptr) {
            return;
        }
        dfs_inorder(node->left, vals);
        vals.push_back(node->val);
        dfs_inorder(node->right, vals);
    }

    TreeNode* increasingBST(TreeNode* root) {
        vector<int> vals;
        dfs_inorder(root, vals);
        TreeNode* newRoot = new TreeNode(vals[0]);
        newRoot->left = nullptr;
        TreeNode* curr = newRoot;
        for (int i = 1; i < vals.size(); ++i) {
            curr->left = nullptr;
            curr->right = new TreeNode(vals[i]);
            curr = curr->right;
        }
        return newRoot;
    }
};

/*
https://leetcode-cn.com/submissions/detail/171593740/

37 / 37 个通过测试用例
状态：通过
执行用时: 0 ms
内存消耗: 7.8 MB

执行用时：0 ms, 在所有 C++ 提交中击败了100.00%的用户
内存消耗：7.8 MB, 在所有 C++ 提交中击败了36.19%的用户
*/
/*
呃，难道 0ms 真的不是LeetCode系统问题么。。。如果是的话连着两次（参见 `000897_ii.cpp`）出现也有点巧啊。。。
*/
