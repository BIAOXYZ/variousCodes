# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return 0
        
        dp_withnode, dp_withoutnode = {}, {}

        def dfs(node):
            if not node.left and not node.right:
                dp_withnode[node] = node.val
                dp_withoutnode[node] = 0
            elif not node.left:
                dfs(node.right)
                dp_withnode[node] = node.val + dp_withoutnode[node.right]
                dp_withoutnode[node] = max(dp_withnode[node.right], dp_withoutnode[node.right])
            elif not node.right:
                dfs(node.left)
                dp_withnode[node] = node.val + dp_withoutnode[node.left]
                dp_withoutnode[node] = max(dp_withnode[node.left], dp_withoutnode[node.left])
            else:
                dfs(node.left)
                dfs(node.right)
                dp_withnode[node] = node.val + dp_withoutnode[node.left] + dp_withoutnode[node.right]
                dp_withoutnode[node] = max(dp_withnode[node.left], dp_withoutnode[node.left]) + max(dp_withnode[node.right], dp_withoutnode[node.right])
            return
        
        dfs(root)
        return max(dp_withnode[root], dp_withoutnode[root])
        
"""
https://leetcode-cn.com/submissions/detail/95085279/

124 / 124 个通过测试用例
状态：通过
执行用时：36 ms
内存消耗：18.4 MB
"""
"""
执行用时：36 ms, 在所有 Python 提交中击败了86.41%的用户
内存消耗：18.4 MB, 在所有 Python 提交中击败了6.67%的用户
"""
