# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        res = [0]
        def dfs_tree_sum(node):
            if not node:
                return 0
            if not node.left and not node.right:
                return node.val
            leftSum, rightSum = dfs_tree_sum(node.left), dfs_tree_sum(node.right)
            res[0] += abs(leftSum - rightSum)
            return leftSum + rightSum + node.val

        dfs_tree_sum(root)
        return res[0]
        
"""
https://leetcode-cn.com/submissions/detail/239727751/

执行用时：36 ms, 在所有 Python 提交中击败了87.50%的用户
内存消耗：15.7 MB, 在所有 Python 提交中击败了87.50%的用户
通过测试用例：
77 / 77
"""
