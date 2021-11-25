# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """

        def dfs_bst(node):
            if not node:
                return None
            if node.val == val:
                return node
            elif node.val > val:
                return dfs_bst(node.left)
            else:
                return dfs_bst(node.right)
        
        return dfs_bst(root)
        
"""
https://leetcode-cn.com/submissions/detail/242399928/

执行用时：56 ms, 在所有 Python 提交中击败了62.20%的用户
内存消耗：17 MB, 在所有 Python 提交中击败了5.18%的用户
通过测试用例：
36 / 36
"""
