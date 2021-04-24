# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    dummyHead = TreeNode(-1)
    curr = dummyHead
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        # 原地修改法。

        def dfs_inorder(node):
            if not node:
                return
            dfs_inorder(node.left)
            self.curr.right = TreeNode(node.val)
            self.curr.right.left = None
            self.curr = self.curr.right
            dfs_inorder(node.right)
        
        dfs_inorder(root)
        return self.dummyHead.right
        
"""
https://leetcode-cn.com/submissions/detail/171598924/

37 / 37 个通过测试用例
状态：通过
执行用时: 16 ms
内存消耗: 12.9 MB

执行用时：16 ms, 在所有 Python 提交中击败了89.47%的用户
内存消耗：12.9 MB, 在所有 Python 提交中击败了88.72%的用户
"""
