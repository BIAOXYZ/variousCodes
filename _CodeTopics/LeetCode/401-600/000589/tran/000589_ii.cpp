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
    vector<int> preorder(Node* root) {
        vector<int> res = {};
        dfs_n_ary_tree(root, res);
        return res;
    };
    
    void dfs_n_ary_tree(const Node* node, vector<int>& res) {
        if (node == nullptr) {
            return;
        }
        res.emplace_back(node->val);
        for (const auto & child : node->children) {
            dfs_n_ary_tree(child, res);
        }
    };
};

/*
https://leetcode-cn.com/submissions/detail/280510751/

执行用时：12 ms, 在所有 C++ 提交中击败了94.90%的用户
内存消耗：11.3 MB, 在所有 C++ 提交中击败了32.56%的用户
通过测试用例：
38 / 38
*/
