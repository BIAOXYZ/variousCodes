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

        # 这次准备把对node是否为空的判断放到dfs子函数里，这样首先开头不用先判断root是否为空了。
        # 其次dfs函数体里也不用对左、右孩子是否为空进行额外判断了，而是统一判断当前的node是否为空就行。

        res = []

        def dfs_inorder(node):
            if not node:
                return
            dfs_inorder(node.left)
            res.append(node.val)
            dfs_inorder(node.right)
            return
        
        dfs_inorder(root)
        return res
        
"""
https://leetcode-cn.com/submissions/detail/108012722/

68 / 68 个通过测试用例
状态：通过
执行用时: 20 ms
内存消耗: 12.6 MB
"""
"""
执行用时：20 ms, 在所有 Python 提交中击败了67.77%的用户
内存消耗：12.6 MB, 在所有 Python 提交中击败了82.90%的用户
"""
