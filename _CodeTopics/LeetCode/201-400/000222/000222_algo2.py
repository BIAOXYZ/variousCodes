# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        # DFS递归，最简单的写法了应该。

        if not root:
            return 0
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        
"""
https://leetcode-cn.com/submissions/detail/125765306/

18 / 18 个通过测试用例
状态：通过
执行用时: 68 ms
内存消耗: 28.4 MB

执行用时：68 ms, 在所有 Python 提交中击败了88.53%的用户
内存消耗：28.4 MB, 在所有 Python 提交中击败了22.22%的用户
"""
