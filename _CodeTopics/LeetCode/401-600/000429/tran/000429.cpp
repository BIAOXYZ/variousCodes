/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
public:
    vector<vector<int>> levelOrder(Node* root) {
        
        if (!root)
            return {};
        
        std::queue<Node*> stk;
        stk.push(root);
        vector<vector<int>> res = {};
        while (!stk.empty()) {
            vector<int> currLevel;
            // 这里必须把 n 显式的先算出来，不能像 Python 那样用类似 i < stk.size();
            int n = stk.size();
            for (int i = 0; i < n; ++i) {
                Node* node = stk.front();
                stk.pop();
                currLevel.push_back(node->val);
                for (Node* child : node->children) {
                    stk.push(child);
                }
            }
            // 这里不用 move 语意也是可以的，比如：`res.push_back(currLevel);`
            res.push_back(std::move(currLevel));
        }
        return res;
    }
};

/*
https://leetcode-cn.com/submissions/detail/296815122/

执行用时：
16 ms
, 在所有 C++ 提交中击败了
79.75%
的用户
内存消耗：
11.5 MB
, 在所有 C++ 提交中击败了
88.04%
的用户
通过测试用例：
38 / 38
*/
