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

        if not root:
            return TreeNode(val, None, None)
        
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
https://leetcode-cn.com/submissions/detail/112473227/

35 / 35 个通过测试用例
状态：通过
执行用时: 120 ms
内存消耗: 16.5 MB

执行用时：120 ms, 在所有 Python 提交中击败了88.00%的用户
内存消耗：16.5 MB, 在所有 Python 提交中击败了29.50%的用户
"""
