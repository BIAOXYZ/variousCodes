# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """

        preNode, currCompareNode, direction = root, root, ''

        while currCompareNode:
            if currCompareNode.val < val:
                direction = 'right'
                preNode = currCompareNode
                currCompareNode = currCompareNode.right
            elif currCompareNode.val > val:
                direction = 'left'
                preNode = currCompareNode
                currCompareNode = currCompareNode.left
        
        newNode = TreeNode(val, None, None)
        if direction == 'left':
            preNode.left = newNode
        else:
            preNode.right = newNode
        return root
        
"""
https://leetcode-cn.com/submissions/detail/112473137/

8 / 35 个通过测试用例
状态：执行出错

执行出错信息：
Line 31: AttributeError: 'NoneType' object has no attribute 'right'
最后执行的输入：
[]
5
"""
