
`863. 二叉树中所有距离为 K 的结点` https://leetcode-cn.com/problems/all-nodes-distance-k-in-binary-tree/solution/er-cha-shu-zhong-suo-you-ju-chi-wei-k-de-qbla/
- [x] 方法一：深度优先搜索 + 哈希表
  * > 由于输入的二叉树没有记录父结点，为此，我们从根结点 root 出发，使用深度优先搜索遍历整棵树，***同时用一个哈希表记录每个结点的父结点***。
    ```cpp
    void findParents(TreeNode* node) {
        if (node->left != nullptr) {
            parents[node->left->val] = node;
            findParents(node->left);
        }
        if (node->right != nullptr) {
            parents[node->right->val] = node;
            findParents(node->right);
        }
    }
    ```

# 测试用例

```
[3,5,1,6,2,0,8,null,null,7,4]
5
2
```
