# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        res = 0
        if not root:
            return res
        
        def sumOfLeftLeavesFromNode(node):
            if node.left:
                res += node.left.val
                res += sumOfLeftLeavesFromNode(node.left)
            if node.right:
                res += sumOfLeftLeavesFromNode(node.right)
            return res
        
        return sumOfLeftLeavesFromNode(root)
                
"""
https://leetcode-cn.com/submissions/detail/109381798/

0 / 102 个通过测试用例
状态：执行出错

执行出错信息：
Line 21: UnboundLocalError: local variable 'res' referenced before assignment
最后执行的输入：
[3,9,20,null,null,15,7]
"""
