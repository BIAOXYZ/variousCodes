# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []
        
        res = []
        stk = [root]
        while stk:
            currLevel = []
            currLevelMax = -float('inf')
            for node in stk:
                currLevelMax = max(currLevelMax, node.val)
                if node.left:
                    currLevel.append(node.left)
                if node.right:
                    currLevel.append(node.right)
            res.append(currLevelMax)
            stk = currLevel
        return res
        
"""
https://leetcode.cn/submissions/detail/328657214/

执行用时：
48 ms
, 在所有 Python3 提交中击败了
81.49%
的用户
内存消耗：
17.6 MB
, 在所有 Python3 提交中击败了
78.10%
的用户
通过测试用例：
78 / 78
"""
