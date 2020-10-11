# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        # 注：因为该题和 LC530 相同（两道题的题目描述里也互相引用了），
        # 所以此代码和 000530.py 完全相同。

        def dfs_inorder(node):
            if not node:
                return
            dfs_inorder(node.left)
            vals.append(node.val)
            dfs_inorder(node.right)
        
        vals = []
        dfs_inorder(root)
        res = vals[1] - vals[0]
        for i in range(2, len(vals)):
            res = min(res, vals[i] - vals[i-1])
            if res == 1:
                return 1
        return res
        
"""
https://leetcode-cn.com/submissions/detail/115028129/

45 / 45 个通过测试用例
状态：通过
执行用时: 24 ms
内存消耗: 12.8 MB

执行用时：24 ms, 在所有 Python 提交中击败了49.11%的用户
内存消耗：12.8 MB, 在所有 Python 提交中击败了9.01%的用户
"""
