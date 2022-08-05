# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:

        if depth == 1:
            newRoot = TreeNode(val, root, None)
            return newRoot
        
        def dfs(node, dep):
            if not node:
                return
            if dep == depth - 1:
                lchild, rchild = node.left, node.right
                newLeft, newRight = TreeNode(val, lchild, None), TreeNode(val, None, rchild)
                node.left = newLeft
                node.right = newRight
                return
            dfs(node.left, dep+1)
            dfs(node.right, dep+1)
        
        dfs(root, 1)
        return root
        
"""
https://leetcode.cn/submissions/detail/346422919/

执行用时：
60 ms
, 在所有 Python3 提交中击败了
16.10%
的用户
内存消耗：
18.1 MB
, 在所有 Python3 提交中击败了
39.51%
的用户
通过测试用例：
109 / 109
"""
