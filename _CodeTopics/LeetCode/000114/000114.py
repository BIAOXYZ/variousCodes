# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    rightChildrenStack = []
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """

        if not root:
            return
        else:    
            if root.right and root.left:
                self.rightChildrenStack.append(root.right)
                root.right = root.left
                root.left = None
                self.flatten(root.right)
            elif root.right:
                self.flatten(root.right)
            elif root.left:
                root.right = root.left
                root.left = None
                self.flatten(root.right)
            else:
                if self.rightChildrenStack:
                    node = self.rightChildrenStack.pop()
                    root.right = node
                    root.left = None
                    self.flatten(node)
                else:
                    return
                    
"""
https://leetcode-cn.com/submissions/detail/93741091/

225 / 225 个通过测试用例
状态：通过
执行用时：32 ms
内存消耗：13.8 MB
"""
"""
执行用时：32 ms, 在所有 Python 提交中击败了36.54%的用户
内存消耗：13.8 MB, 在所有 Python 提交中击败了12.82%的用户
"""
