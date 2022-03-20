# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:

        expected = set()
        def dfs_and_check_sum(node):
            if not node:
                return False
            if node.val in expected:
                return True
            else:
                expected.add(k - node.val)
            resLeft = dfs_and_check_sum(node.left)
            resRight = dfs_and_check_sum(node.right)
            return resLeft or resRight
        
        return dfs_and_check_sum(root)
        
"""
https://leetcode-cn.com/submissions/detail/286685393/

执行用时：76 ms, 在所有 Python3 提交中击败了69.38%的用户
内存消耗：20.1 MB, 在所有 Python3 提交中击败了42.16%的用户
通过测试用例：
422 / 422
"""
