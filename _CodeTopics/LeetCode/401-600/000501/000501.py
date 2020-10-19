# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        def dfs_and_count_frequency(node):
            if dic.has_key(node.val):
                dic[node.val] += 1
            else:
                dic[node.val] = 1
            if node.left:
                dfs_and_count_frequency(node.left)
            if node.right:
                dfs_and_count_frequency(node.right)
        
        res, dic = list(), dict()

        if not root:
            return []
        dfs_and_count_frequency(root)
        maxFrequency = max(dic.values())
        for k, v in dic.items():
            if v == maxFrequency:
                res.append(k)
        return res
        
"""
https://leetcode-cn.com/submissions/detail/110894038/

25 / 25 个通过测试用例
状态：通过
执行用时: 48 ms
内存消耗: 20.4 MB

执行用时：48 ms, 在所有 Python 提交中击败了79.75%的用户
内存消耗：20.4 MB, 在所有 Python 提交中击败了14.29%的用户
"""
