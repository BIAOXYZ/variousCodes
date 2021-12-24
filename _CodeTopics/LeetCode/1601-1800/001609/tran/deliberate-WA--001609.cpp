#include <queue>

#define MAX_VAL 100001

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
    bool isEvenOddTree(TreeNode* root) {

        std::queue<TreeNode*> stk;
        stk.push(root);
        int level = 0;

        while (!stk.empty()) {
            int preVal = level % 2 == 1? MAX_VAL : -MAX_VAL;
            std::queue<TreeNode*> nextLevel;
            for (int i = 0; i < stk.size(); ++i) {
                TreeNode* node = stk.front(); stk.pop();
                if ( (level == 1 && (node->val % 2 == 1 || node->val >= preVal)) || 
                    (level == 0 && (node->val % 2 == 0 || node->val <= preVal)) ) {
                        return false;
                } else {
                    preVal = node->val;
                    if (node->left != nullptr) nextLevel.push(node->left);
                    if (node->right != nullptr) nextLevel.push(node->right);
                }
            }
            // 怀疑是这里导致用例 [5,4,2,3,3,7] 过不去。先记一下吧，太晚了。
            stk = nextLevel;
            level = (level + 1) % 2;
        }
        return true;
    }
};

/*
https://leetcode-cn.com/submissions/detail/251802787/

59 / 105 个通过测试用例
状态：解答错误

输入：
[5,4,2,3,3,7]
输出：
true
预期结果：
false
*/
