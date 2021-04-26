# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """

        def dfs_inorder(node):
            if not node:
                return
            if node.val < low:
                dfs_inorder(node.right)
            elif node.val > high:
                dfs_inorder(node.left)
            else:
                dfs_inorder(node.left)
                vals.append(node.val)
                dfs_inorder(node.right)
        
        vals = []
        dfs_inorder(root)
        return sum(vals)
        
"""
https://leetcode-cn.com/submissions/detail/172310837/

41 / 41 个通过测试用例
状态：通过
执行用时: 220 ms
内存消耗: 28.9 MB

执行用时：220 ms, 在所有 Python 提交中击败了88.07%的用户
内存消耗：28.9 MB, 在所有 Python 提交中击败了65.26%的用户
"""
