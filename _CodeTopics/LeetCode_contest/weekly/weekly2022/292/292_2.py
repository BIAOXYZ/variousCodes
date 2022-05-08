# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfSubtree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        
        nodes = []
        def dfs(node):
            if not node.left and not node.right:
                nodes.append([node, node.val, 1])
                return node.val, 1
            sumLeft = sumRight = nLeft = nRight = 0
            if node.left:
                sumLeft, nLeft = dfs(node.left)
            if node.right:
                sumRight, nRight = dfs(node.right)
            nodes.append([node, sumLeft+sumRight+node.val, nLeft+nRight+1])
            return sumLeft+sumRight+node.val, nLeft+nRight+1
        
        dfs(root)
        res = 0
        for node, summ, n in nodes:
            if node.val == summ // n:
                res += 1
        return res
    
"""
https://leetcode-cn.com/submissions/detail/310682107/

138 / 138 个通过测试用例
状态：通过
执行用时: 28 ms
内存消耗: 15.2 MB
"""
