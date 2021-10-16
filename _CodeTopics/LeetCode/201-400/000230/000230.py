# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        def dfs_inorder(node):
            if not node:
                return
            dfs_inorder(node.left)
            res.append(node.val)
            dfs_inorder(node.right)
        
        res = []
        dfs_inorder(root)
        return res[k-1]
        
"""
https://leetcode-cn.com/submissions/detail/229537794/

93 / 93 个通过测试用例
状态：通过
执行用时: 36 ms
内存消耗: 20.8 MB

执行用时：36 ms, 在所有 Python 提交中击败了70.53%的用户
内存消耗：20.8 MB, 在所有 Python 提交中击败了7.37%的用户
"""
