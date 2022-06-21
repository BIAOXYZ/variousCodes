# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:

        stk = [root]
        res = root.val
        while stk:
            nextLevel = []
            for node in stk:
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            if nextLevel:
                res = nextLevel[0].val
            stk = nextLevel
        return res
        
"""
https://leetcode.cn/submissions/detail/327880010/

执行用时：
44 ms
, 在所有 Python3 提交中击败了
88.86%
的用户
内存消耗：
17.6 MB
, 在所有 Python3 提交中击败了
57.73%
的用户
通过测试用例：
76 / 76
"""
