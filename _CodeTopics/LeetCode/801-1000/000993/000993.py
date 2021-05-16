# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """

        stk = [root]
        while stk:
            nextLevel = []
            flag = 0
            for node in stk:
                if node.left: nextLevel.append(node.left)
                if node.right: nextLevel.append(node.right)
                if node.left and node.right:
                    if set([node.left.val, node.right.val]) == set([x, y]):
                        return False
                if node.val == x or node.val == y:
                    flag += 1
                    if flag == 2:
                        return True
            stk = nextLevel[:]
        return False
        
"""
https://leetcode-cn.com/submissions/detail/178118957/

104 / 104 个通过测试用例
状态：通过
执行用时: 16 ms
内存消耗: 12.9 MB

执行用时：16 ms, 在所有 Python 提交中击败了91.21%的用户
内存消耗：12.9 MB, 在所有 Python 提交中击败了94.51%的用户
"""
