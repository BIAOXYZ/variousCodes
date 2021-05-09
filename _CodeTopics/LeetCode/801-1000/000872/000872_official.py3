# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        
        # official -- 主要是为了这个 yield 语法。
        def dfs(node: TreeNode):
            if not node.left and not node.right:
                yield node.val
            else:
                if node.left:
                    yield from dfs(node.left)
                if node.right:
                    yield from dfs(node.right)
        
        seq1 = list(dfs(root1)) if root1 else list()
        seq2 = list(dfs(root2)) if root2 else list()
        return seq1 == seq2
        
"""
https://leetcode-cn.com/submissions/detail/175930422/

40 / 40 个通过测试用例
状态：通过
执行用时: 36 ms
内存消耗: 14.9 MB

执行用时：36 ms, 在所有 Python3 提交中击败了91.33%的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了32.66%的用户
"""
