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

        vector<int> res{};

        // 只引用一个 res 是不够的，因为还要递归地调用 lambda 匿名函数本身。
        //// std::function<void(Node*)> dfs_n_ary_tree = [&res](Node* node) -> void {
        // 下面这种写法看攻略明明从 C++ 11 到 C++ 20 都可以，但是这里就是会报错。
        //// std::function<void(Node*)> dfs_n_ary_tree = [&res, this](Node* node) -> void {
        // 于是只好老老实实用下面这种没有任何访问控制的写法：
        std::function<void(Node*)> dfs_n_ary_tree = [&](Node* node) -> void {
            if (node == nullptr) {
                return;
            }
            res.emplace_back(node->val);
            for (const auto & child : node->children) {
                dfs_n_ary_tree(child);
            }
        };
        
        dfs_n_ary_tree(root);
        return res;
    }
};

/*
https://leetcode-cn.com/submissions/detail/280434277/

执行用时：16 ms, 在所有 C++ 提交中击败了75.29%的用户
内存消耗：11.4 MB, 在所有 C++ 提交中击败了20.13%的用户
通过测试用例：
38 / 38
*/
