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

// 没有 this 的版本。
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

    TreeNode* increasingBST(TreeNode* root) {
        dfs_inorder(root);
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
https://leetcode-cn.com/submissions/detail/171593091/

37 / 37 个通过测试用例
状态：通过
执行用时: 0 ms
内存消耗: 7.8 MB

执行用时：0 ms, 在所有 C++ 提交中击败了100.00%的用户
内存消耗：7.8 MB, 在所有 C++ 提交中击败了24.46%的用户
*/
/*
这肯定不是少了一个this的原因，就快这么多。。。我觉得就是LeetCode系统的问题吧。。。
*/
