# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        
        maxLen = 0
        def dfs(node):
            nonlocal maxLen
            if not node.left and not node.right:
                return 0
            leftLen = rightLen = currLen = 0
            if node.left:
                leftLen = dfs(node.left)
                if node.val == node.left.val:
                    currLen += 1 + leftLen
            if node.right:
                rightLen = dfs(node.right)
                if node.val == node.right.val:
                    currLen += 1 + rightLen
            maxLen = max(maxLen, currLen)
            return currLen
        
        dfs(root)
        return maxLen
        
"""
https://leetcode.cn/submissions/detail/358277208/

43 / 71 个通过测试用例
状态：解答错误

输入：
[1,null,1,1,1,1,1,1]
输出：
6
预期结果：
4
"""
