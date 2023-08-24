# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        res = 0
        def dfs(node, currMax):
            if not node:
                return
            nonlocal res
            if node.val >= currMax:
                res += 1
            nextMax = max(currMax, node.val)
            dfs(node.left, nextMax)
            dfs(node.right, nextMax)
        dfs(root, root.val)
        return res
        
"""
https://leetcode.cn/problems/count-good-nodes-in-binary-tree/submissions/459642639/

时间
详情
208ms
击败 64.55%使用 Python3 的用户
内存
详情
33.38MB
击败 87.60%使用 Python3 的用户
"""
