# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return 0
        
        def sumOfLeftLeavesFromNode(node):
            res = 0
            if node.left:
                res += node.left.val
                res += sumOfLeftLeavesFromNode(node.left)
            if node.right:
                res += sumOfLeftLeavesFromNode(node.right)
            return res
        
        return sumOfLeftLeavesFromNode(root)
"""
https://leetcode-cn.com/submissions/detail/109390726/

31 / 102 个通过测试用例
状态：解答错误

输入：
[1,2,3,4,5]
输出：
6
预期：
4
"""
