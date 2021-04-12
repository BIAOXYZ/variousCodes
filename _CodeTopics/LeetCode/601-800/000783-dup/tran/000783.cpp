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
    void dfs_inorder(TreeNode* node, vector<int>& vals) {
        if (node == nullptr) {
            return;
        }
        dfs_inorder(node->left, vals);
        vals.push_back(node->val);
        dfs_inorder(node->right, vals);
    }

    int minDiffInBST(TreeNode* root) {
        vector<int> vals;
        dfs_inorder(root, vals);
        int res = vals[1] - vals[0];
        for (int i = 2; i < vals.size(); ++i) {
            res = min(res, vals[i] - vals[i-1]);
            if (res == 1)
                break;
        }
        return res;
    }
};

/*
https://leetcode-cn.com/submissions/detail/167197757/

46 / 46 个通过测试用例
状态：通过
执行用时: 0 ms
内存消耗: 9.6 MB

执行用时：0 ms, 在所有 C++ 提交中击败了100.00%的用户
内存消耗：9.6 MB, 在所有 C++ 提交中击败了22.55%的用户
*/
/*
0ms 真的不是bug么？感觉我这个写法并不如答案的实现——因为图省事引入了一个额外的vector。。。
*/
