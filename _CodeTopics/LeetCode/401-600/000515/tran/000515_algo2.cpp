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
    vector<int> largestValues(TreeNode* root) {
        
        if (!root) {
            return vector<int>{};
        }

        unordered_map<int, int> dic;
        std::function<void(TreeNode*, int)> dfs = [&](TreeNode* node, int level) -> void {
            if (dic.find(level) != dic.end()) {
                dic[level] = max(dic[level], node->val);
            } else {
                dic[level] = node->val;
            }
            if (node->left)
                dfs(node->left, level+1);
            if (node->right)
                dfs(node->right, level+1);
        };

        dfs(root, 0);
        vector<int> res = {};
        for (int i = 0; i < dic.size(); ++i) {
            res.push_back(dic[i]);
        }
        return res;
    }
};

/*
https://leetcode.cn/submissions/detail/328659754/

执行用时：
12 ms
, 在所有 C++ 提交中击败了
49.35%
的用户
内存消耗：
22 MB
, 在所有 C++ 提交中击败了
5.02%
的用户
通过测试用例：
78 / 78
*/
