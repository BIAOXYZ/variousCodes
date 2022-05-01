# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:

        def dfs(node: TreeNode) -> None:
            if not node:
                return
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)
        
        res = []
        dfs(root1)
        dfs(root2)
        return sorted(res)
        
"""
https://leetcode-cn.com/submissions/detail/307985526/

执行用时：
284 ms
, 在所有 Python3 提交中击败了
86.54%
的用户
内存消耗：
24.1 MB
, 在所有 Python3 提交中击败了
40.86%
的用户
通过测试用例：
48 / 48
"""
