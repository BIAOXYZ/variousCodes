# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """

        def traverseWithLastSum(root, lastsum):
            res = False
            lastsum += root.val
            if root.left is None and root.right is None:
                return True if lastsum == sum else False
            if root.left:
                res = res or traverseWithLastSum(root.left, lastsum)
            if root.right:
                res = res or traverseWithLastSum(root.right, lastsum)
            return res
        
        if root is None:
            return False
        return traverseWithLastSum(root, 0)
        
"""
https://leetcode-cn.com/submissions/detail/85505479/

114 / 114 个通过测试用例
状态：通过
执行用时：36 ms
内存消耗：16.4 MB
"""
"""
执行用时：36 ms, 在所有 Python 提交中击败了62.04%的用户
内存消耗：16.4 MB, 在所有 Python 提交中击败了20.00%的用户
"""
