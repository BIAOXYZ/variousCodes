# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs_and_prune(node):
            if not node:
                return False
            hasOneInLeft = dfs_and_prune(node.left)
            hasOneInRight = dfs_and_prune(node.right)
            if not hasOneInLeft:
                node.left = None
            if not hasOneInRight:
                node.right = None
            if hasOneInLeft or hasOneInRight or node.val == 1:
                return True
            else:
                return False
        
        if not dfs_and_prune(root):
            return None
        else:
            return root
        
"""
https://leetcode.cn/submissions/detail/340217790/

执行用时：
40 ms
, 在所有 Python3 提交中击败了
49.47%
的用户
内存消耗：
14.9 MB
, 在所有 Python3 提交中击败了
75.13%
的用户
通过测试用例：
30 / 30
"""
