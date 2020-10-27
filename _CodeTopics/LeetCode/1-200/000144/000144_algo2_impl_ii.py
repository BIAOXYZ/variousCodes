# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        res = []
        curr = root
        stack = []

        while curr or stack:
            while curr:
                res.append(curr.val)
                stack.append(curr)
                curr = curr.left
            curr = stack.pop().right
        return res
        
"""
https://leetcode-cn.com/submissions/detail/118925765/

68 / 68 个通过测试用例
状态：通过
执行用时: 24 ms
内存消耗: 13 MB

执行用时：24 ms, 在所有 Python 提交中击败了35.85%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了6.63%的用户
"""
