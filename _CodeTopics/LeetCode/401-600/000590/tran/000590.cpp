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
    vector<int> postorder(Node* root) {
        // https://leetcode-cn.com/submissions/detail/281572173/
        
        vector<int> res = {};

        std::function<void(Node*)> postorder_dfs_n_ary_tree; 
        postorder_dfs_n_ary_tree = [&](Node* node) -> void {
            if (nullptr == node) {
                return;
            }
            for (const auto & child : node->children) {
                postorder_dfs_n_ary_tree(child);
            }
            res.emplace_back(node->val);
        };

        postorder_dfs_n_ary_tree(root);
        return res;
    }
};

/*
https://leetcode.cn/problems/n-ary-tree-postorder-traversal/submissions/503120342/?envType=daily-question&envId=2024-02-19

执行用时分布
13
ms
击败
75.15%
使用 C++ 的用户
消耗内存分布
14.72
MB
击败
25.23%
使用 C++ 的用户
*/
