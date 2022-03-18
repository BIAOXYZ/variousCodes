# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:

        res = []
        def dfs_and_add_parenthesis(node):
            if not node:
                return
            res.append(str(node.val))
            if node.left:
                res.append('(')
                dfs_and_add_parenthesis(node.left)
                res.append(')')
            if node.right:
                if not node.left:
                    res.append('()')
                res.append('(')
                dfs_and_add_parenthesis(node.right)
                res.append(')')
        
        dfs_and_add_parenthesis(root)
        return ''.join(res)
        
"""
https://leetcode-cn.com/submissions/detail/285580110/

执行用时：56 ms, 在所有 Python3 提交中击败了34.56%的用户
内存消耗：17.7 MB, 在所有 Python3 提交中击败了9.06%的用户
通过测试用例：
160 / 160
"""
