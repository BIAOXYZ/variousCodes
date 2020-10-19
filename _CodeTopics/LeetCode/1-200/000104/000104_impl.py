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
            self.maxdep = max(self.maxdep, self.currdep)
            return self.maxdep
        else:
            self.currdep += 1
        
        self.maxDepth(root.left)
        self.maxDepth(root.right)
        self.currdep -= 1
        return self.maxdep
        
"""
https://leetcode-cn.com/submissions/detail/92691900/

39 / 39 个通过测试用例
状态：通过
执行用时：36 ms
内存消耗：15.5 MB
"""
"""
执行用时：36 ms, 在所有 Python 提交中击败了43.04%的用户
内存消耗：15.5 MB, 在所有 Python 提交中击败了7.69%的用户
"""
