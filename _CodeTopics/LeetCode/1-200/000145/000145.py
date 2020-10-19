# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        def dfs_postorder(node):
            if node.left:
                dfs_postorder(node.left)
            if node.right:
                dfs_postorder(node.right)
            res.append(node.val)
            return

        if not root:
            return []
        res = []
        dfs_postorder(root)
        return res
        
"""
https://leetcode-cn.com/submissions/detail/112210361/

68 / 68 个通过测试用例
状态：通过
执行用时: 12 ms
内存消耗: 12.6 MB

执行用时：12 ms, 在所有 Python 提交中击败了97.42%的用户
内存消耗：12.6 MB, 在所有 Python 提交中击败了10.16%的用户
"""
