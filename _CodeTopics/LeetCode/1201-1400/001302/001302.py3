# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:

        ddic = defaultdict(int)
        def dfs(node, depth):
            if not node:
                return
            ddic[depth] += node.val
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)
        
        dfs(root, 0)
        return ddic[max(ddic.keys())]
        
"""
https://leetcode.cn/submissions/detail/351203381/

执行用时：
184 ms
, 在所有 Python3 提交中击败了
66.87%
的用户
内存消耗：
19.3 MB
, 在所有 Python3 提交中击败了
55.11%
的用户
通过测试用例：
39 / 39
"""
