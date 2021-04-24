# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        vals = []
        def dfs_inorder(node):
            if not node:
                return
            dfs_inorder(node.left)
            vals.append(node.val)
            dfs_inorder(node.right)
        
        dfs_inorder(root)
        curr = newRoot = TreeNode(vals[0])
        newRoot.left = None
        for i in range(1, len(vals)):
            curr.left = None
            curr.right = TreeNode(vals[i])
            curr = curr.right
        return newRoot
        
"""
https://leetcode-cn.com/submissions/detail/171587364/

37 / 37 个通过测试用例
状态：通过
执行用时: 20 ms
内存消耗: 13 MB

执行用时：20 ms, 在所有 Python 提交中击败了58.09%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了81.62%的用户
"""
