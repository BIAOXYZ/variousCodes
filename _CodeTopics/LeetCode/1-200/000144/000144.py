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

        def dfs_preorder(node):
            res.append(node.val)
            if node.left:
                dfs_preorder(node.left)
            if node.right:
                dfs_preorder(node.right)

        if not root:
            return []
        res = []
        dfs_preorder(root)
        return res
        
"""
https://leetcode-cn.com/submissions/detail/118845762/

68 / 68 个通过测试用例
状态：通过
执行用时: 16 ms
内存消耗: 13.2 MB

执行用时：16 ms, 在所有 Python 提交中击败了86.39%的用户
内存消耗：13.2 MB, 在所有 Python 提交中击败了5.05%的用户
"""
