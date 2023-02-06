# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:

        def dfs_and_eval_val(node):
            if node.val in [0, 1]:
                return node.val
            elif node.val == 2:
                return dfs_and_eval_val(node.left) or dfs_and_eval_val(node.right)
            elif node.val == 3:
                return dfs_and_eval_val(node.left) and dfs_and_eval_val(node.right)
        return bool(dfs_and_eval_val(root))
        
"""
https://leetcode.cn/submissions/detail/399814744/

执行用时：
56 ms
, 在所有 Python3 提交中击败了
79.52%
的用户
内存消耗：
15.7 MB
, 在所有 Python3 提交中击败了
83.13%
的用户
通过测试用例：
75 / 75
"""
