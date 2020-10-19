# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        # 这次不用递归，用迭代。迭代的实现需要用到栈。

        res = []
        if not root:
            return []
        
        stack, currnode = [], root
        while currnode:
            stack.append(currnode)
            currnode = currnode.left
        while stack:
            tmpnode = stack.pop()
            res.append(tmpnode.val)
            currnode = tmpnode.right
            while currnode:
                stack.append(currnode)
                currnode = currnode.left
        return res
        
"""
https://leetcode-cn.com/submissions/detail/108087146/

68 / 68 个通过测试用例
状态：通过
执行用时: 20 ms
内存消耗: 12.6 MB
"""
"""
执行用时：20 ms, 在所有 Python 提交中击败了67.77%的用户
内存消耗：12.6 MB, 在所有 Python 提交中击败了95.55%的用户
"""
