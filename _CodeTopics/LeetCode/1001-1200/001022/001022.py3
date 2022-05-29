# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:

        res = 0
        def dfs_and_form_prefix(node, currStr):
            nonlocal res
            if not node.left and not node.right:
                res += int(currStr, 2)
            if node.left:
                dfs_and_form_prefix(node.left, currStr + str(node.left.val))
            if node.right:
                dfs_and_form_prefix(node.right, currStr + str(node.right.val))
        
        dfs_and_form_prefix(root, str(root.val))
        return res
        
"""
https://leetcode.cn/submissions/detail/319630223/

执行用时：
32 ms
, 在所有 Python3 提交中击败了
99.01%
的用户
内存消耗：
15.4 MB
, 在所有 Python3 提交中击败了
18.09%
的用户
通过测试用例：
63 / 63
"""
