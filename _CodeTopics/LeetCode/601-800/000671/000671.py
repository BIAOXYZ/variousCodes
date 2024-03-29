# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        vals = set()
        def dfs(node):
            if not node:
                return
            vals.add(node.val)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        if len(vals) < 2:
            return -1
        return sorted(list(vals))[1]
        
"""
https://leetcode-cn.com/submissions/detail/200146026/

39 / 39 个通过测试用例
状态：通过
执行用时: 12 ms
内存消耗: 13.1 MB

执行用时：12 ms, 在所有 Python 提交中击败了88.46%的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了17.95%的用户
"""
