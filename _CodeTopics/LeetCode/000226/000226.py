# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        # 思路：最开始想着BFS，然后每层把当前栈倒着输出。但是后来发现递归其实更简单
        # 就先写个递归的吧。

        if not root:
            return None
        
        root.left, root.right = root.right, root.left
        if root.left:
            self.invertTree(root.left)
        if root.right:
            self.invertTree(root.right)
        return root
        
"""
https://leetcode-cn.com/submissions/detail/108724486/

68 / 68 个通过测试用例
状态：通过
执行用时: 20 ms
内存消耗: 12.7 MB
"""
"""
执行用时：20 ms, 在所有 Python 提交中击败了68.08%的用户
内存消耗：12.7 MB, 在所有 Python 提交中击败了5.48%的用户
"""
