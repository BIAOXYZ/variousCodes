# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:

        def dfs(node, level):
            if not node.left and not node.right:
                return node.val, level
            elif node.left and not node.right:
                return dfs(node.left, level+1)
            elif not node.left and node.right:
                return dfs(node.right, level+1)
            else:
                leftVal, leftLevel = dfs(node.left, level+1)
                rightVal, rightLevel = dfs(node.right, level+1)
                if rightLevel > leftLevel:
                    return rightVal, rightLevel
                else:
                    return leftVal, leftLevel
        
        res, _ = dfs(root, 0)
        return res
        
"""
https://leetcode.cn/submissions/detail/327881623/

执行用时：
48 ms
, 在所有 Python3 提交中击败了
71.87%
的用户
内存消耗：
18.1 MB
, 在所有 Python3 提交中击败了
10.64%
的用户
通过测试用例：
76 / 76
"""
