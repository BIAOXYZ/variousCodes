# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:

        se = set()
        def dfs(node):
            if not node:
                return
            se.add(node.val)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return len(se) == 1
        
"""
https://leetcode.cn/submissions/detail/317285876/

执行用时：
32 ms
, 在所有 Python3 提交中击败了
93.01%
的用户
内存消耗：
15 MB
, 在所有 Python3 提交中击败了
24.82%
的用户
通过测试用例：
72 / 72
"""
