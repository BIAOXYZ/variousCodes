# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    maxdep = currdep = 0
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return 0
        
        ldepth = self.maxDepth(root.left)
        rdepth = self.maxDepth(root.right)
        return max(ldepth, rdepth) + 1
               
"""
https://leetcode-cn.com/submissions/detail/92433565/

39 / 39 个通过测试用例
状态：通过
执行用时：40 ms
内存消耗：15.7 MB
"""
"""
执行用时：40 ms, 在所有 Python 提交中击败了22.52%的用户
内存消耗：15.7 MB, 在所有 Python 提交中击败了7.69%的用户
"""
