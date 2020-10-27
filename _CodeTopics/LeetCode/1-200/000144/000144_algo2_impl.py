# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        res = []
        curr = root
        rightChildrenStack = []

        while curr or rightChildrenStack:
            while curr:
                res.append(curr.val)
                if curr.right:
                    rightChildrenStack.append(curr.right)
                curr = curr.left
            if rightChildrenStack:
                curr = rightChildrenStack.pop()
        return res
        
"""
https://leetcode-cn.com/submissions/detail/118924807/

68 / 68 个通过测试用例
状态：通过
执行用时: 20 ms
内存消耗: 13.2 MB

执行用时：20 ms, 在所有 Python 提交中击败了63.94%的用户
内存消耗：13.2 MB, 在所有 Python 提交中击败了5.04%的用户
"""
