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
        """
        # 无需判空
        if not root:
            return res
        """

        curr = root
        rightChildrenStack = []
        while curr:
            res.append(curr.val)
            if curr.right:
                rightChildrenStack.append(curr.right)
            if curr.left:
                curr = curr.left
            elif rightChildrenStack:
                curr = rightChildrenStack.pop()
            else:
                break
        return res
        
"""
https://leetcode-cn.com/submissions/detail/118851839/

68 / 68 个通过测试用例
状态：通过
执行用时: 20 ms
内存消耗: 13.3 MB

执行用时：20 ms, 在所有 Python 提交中击败了63.90%的用户
内存消耗：13.3 MB, 在所有 Python 提交中击败了5.05%的用户
"""
