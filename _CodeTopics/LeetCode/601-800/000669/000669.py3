# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def trimBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: TreeNode
        """

        if not root:
            return None
        if not root.left and not root.right:
            return root if low <= root.val <= high else None
        if root.val < low:
            return self.trimBST(root.right, low, high)
        if root.val > high:
            return self.trimBST(root.left, low, high)
        newLeft = self.trimBST(root.left, low, high)
        newRight = self.trimBST(root.right, low, high)
        root.left, root.right = newLeft, newRight
        return root
        
"""
https://leetcode.cn/submissions/detail/361223424/

执行用时：
32 ms
, 在所有 Python 提交中击败了
84.68%
的用户
内存消耗：
20.6 MB
, 在所有 Python 提交中击败了
27.47%
的用户
通过测试用例：
78 / 78
"""
