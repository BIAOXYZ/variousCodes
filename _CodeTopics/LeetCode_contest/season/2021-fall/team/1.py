# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def numColor(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        res = set()
        def dfs_in_LCCUP(node):
            if not node:
                return
            dfs_in_LCCUP(node.left)
            res.add(node.val)
            dfs_in_LCCUP(node.right)
        
        dfs_in_LCCUP(root)
        return len(res)
    
"""
https://leetcode-cn.com/contest/season/2021-fall/submissions/223037692/
"""
