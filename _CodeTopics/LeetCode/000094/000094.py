# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        res = []
        if not root:
            return res

        def dfs_inorder(node):
            if node.left:
                dfs_inorder(node.left)
            res.append(node.val)
            if node.right:
                dfs_inorder(node.right)
            return
        
        dfs_inorder(root)
        return res
        
"""
https://leetcode-cn.com/submissions/detail/108001202/

68 / 68 个通过测试用例
状态：通过
执行用时: 24 ms
内存消耗: 12.9 MB
"""
"""
执行用时：24 ms, 在所有 Python 提交中击败了39.24%的用户
内存消耗：12.9 MB, 在所有 Python 提交中击败了11.08%的用户
"""
