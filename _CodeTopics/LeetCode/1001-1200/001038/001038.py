# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        def dfs_and_append_value(node):
            if not node:
                return
            dfs_and_append_value(node.left)
            nodeValue.append(node.val)
            dfs_and_append_value(node.right)

        def dfs_and_change_value(node):
            if not node:
                return
            dfs_and_change_value(node.left)
            node.val += prefixSumdic[node.val]
            dfs_and_change_value(node.right)

        if not root:
            return root    
        nodeValue, prefixSumdic = [], {}
        dfs_and_append_value(root)
        totalsum = sum(nodeValue)

        prefixSumdic[nodeValue[0]] = totalsum - nodeValue[0]
        for i in range(1, len(nodeValue)):
            prefixSumdic[nodeValue[i]] = prefixSumdic[nodeValue[i-1]] - nodeValue[i]        
        
        dfs_and_change_value(root)
        return root
        
"""
https://leetcode-cn.com/submissions/detail/110234830/

28 / 28 个通过测试用例
状态：通过
执行用时: 12 ms
内存消耗: 12.5 MB

执行用时：12 ms, 在所有 Python 提交中击败了100.00%的用户
内存消耗：12.5 MB, 在所有 Python 提交中击败了45.83%的用户
"""
"""
注：和 LC538 是一模一样的题。所以这个code除了函数名字等以外，也是直接从 000538.py 复制粘贴过来的。
"""
