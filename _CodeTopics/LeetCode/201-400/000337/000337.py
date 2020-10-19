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
            if not node:
                # 如果没有这一句，后面会报 KeyError: None，如下所示：
                ## KeyError: None
                ## dp_withnode[node] = dp_withoutnode[node.left] + dp_withoutnode[node.right]
                ## 其原因是到了任一个叶子节点后，左右子树均为空，如果直接return，那么dp_withnode和dp_withoutnode里对于叶子节点的子节点（虽然是None）都没有key，所以想去相加时候自然报错了。
                dp_withnode[node] = dp_withoutnode[node] = 0
                return
            if not node.left and not node.right:
                dp_withnode[node] = node.val
                dp_withoutnode[node] = 0
                return
            dfs(node.left)
            dfs(node.right)
            dp_withnode[node] = node.val + dp_withoutnode[node.left] + dp_withoutnode[node.right]
            dp_withoutnode[node] = max(dp_withnode[node.left], dp_withoutnode[node.left]) + max(dp_withnode[node.right], dp_withoutnode[node.right])
            return
        
        dfs(root)
        return max(dp_withnode[root], dp_withoutnode[root])
        
"""
https://leetcode-cn.com/submissions/detail/95050436/

124 / 124 个通过测试用例
状态：通过
执行用时：40 ms
内存消耗：18.7 MB
"""
"""
执行用时：40 ms, 在所有 Python 提交中击败了67.57%的用户
内存消耗：18.7 MB, 在所有 Python 提交中击败了6.67%的用户
"""
