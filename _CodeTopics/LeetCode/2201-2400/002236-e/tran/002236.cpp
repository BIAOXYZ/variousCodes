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
public:
    bool checkTree(TreeNode* root) {

        return root->val == root->left->val + root->right->val;
        
    }
};

/*
https://leetcode.cn/problems/root-equals-sum-of-children/submissions/458032969/

时间
详情
4ms
击败 53.56%使用 C++ 的用户
内存
详情
11.98MB
击败 33.55%使用 C++ 的用户
*/
