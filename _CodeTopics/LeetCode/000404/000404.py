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

        def sumOfLeftLeavesFromNode(node, isLeft):
            res = 0
            if not node:
                return 0
            elif not node.left and not node.right:
                if isLeft:
                    res += node.val
            else:
                res += sumOfLeftLeavesFromNode(node.left, True)
                res += sumOfLeftLeavesFromNode(node.right, False)
            return res
        
        return sumOfLeftLeavesFromNode(root, False)
        
"""
https://leetcode-cn.com/submissions/detail/109392793/

102 / 102 个通过测试用例
状态：通过
执行用时: 28 ms
内存消耗: 13.2 MB

执行用时：28 ms, 在所有 Python 提交中击败了24.60%的用户
内存消耗：13.2 MB, 在所有 Python 提交中击败了36.22%的用户
"""
