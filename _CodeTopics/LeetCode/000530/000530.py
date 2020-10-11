# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        # 先按第一反应来：直接dfs遍历，并把节点的值都存到一个数组里。然后对数组排序，
        # （当然会用中序dfs，这样的话数组直接是排好序的——所以这里其实就用到二叉树的性质了）
        # 并计算出相邻两个值的差，最后返回最小的差即可。

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
https://leetcode-cn.com/submissions/detail/115027853/

186 / 186 个通过测试用例
状态：通过
执行用时: 52 ms
内存消耗: 16.6 MB

执行用时：52 ms, 在所有 Python 提交中击败了52.41%的用户
内存消耗：16.6 MB, 在所有 Python 提交中击败了12.67%的用户
"""
