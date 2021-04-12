/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

#define MIN(a, b) ((a) < (b) ? (a) : (b))
#define MAX_ARR_SIZE 101
int length = 0;

void dfs_inorder(struct TreeNode* node, int *vals) {
    if (node == NULL) {
        return;
    }
    dfs_inorder(node->left, vals);
    vals[length++] = node->val;
    dfs_inorder(node->right, vals);
}

int minDiffInBST(struct TreeNode* root){
    // 这里不能少了 unsigned，否则下面两个 vals 里元素相减会出负值。。。
    // 另外，我这里测试用例 [96,12,null,null,13,null,52,29] 没问题啊，为啥上次就错了啊？
    unsigned int vals[MAX_ARR_SIZE];
    dfs_inorder(root, vals);
    int res = vals[1] - vals[0];
    for (int i = 2; i < length; ++i) {
        res = MIN(res, vals[i] - vals[i-1]);
        if (res == 1)
            break;
    }
    return res;
}

/*
https://leetcode-cn.com/submissions/detail/167200048/

3 / 46 个通过测试用例
状态：解答错误

输入：
[96,12,null,null,13,null,52,29]
输出：
0
预期：
1
*/
/*
我擦，我在做题页面试了很多次了，在那里运行（包括运行用例 [96,12,null,null,13,null,52,29] ）就没问题！
*/
