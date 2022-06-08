# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def dfs_and_check_symmetry(leftTree, rightTree):
            if not leftTree and not rightTree:
                return True
            elif (not leftTree and rightTree) or (leftTree and not rightTree):
                return False
            elif leftTree and rightTree:
                if leftTree.val == rightTree.val and \
                    dfs_and_check_symmetry(leftTree.right, rightTree.left) and \
                    dfs_and_check_symmetry(leftTree.left, rightTree.right):
                    return True
                else:
                    return False
        
        return dfs_and_check_symmetry(root.left, root.right)
        
"""
https://leetcode.cn/submissions/detail/323268208/

执行用时：
44 ms
, 在所有 Python3 提交中击败了
34.68%
的用户
内存消耗：
15.1 MB
, 在所有 Python3 提交中击败了
22.97%
的用户
通过测试用例：
198 / 198
"""
