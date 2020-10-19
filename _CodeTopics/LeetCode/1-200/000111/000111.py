# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return 0
        
        level = 0
        stack = [[root]]
        while stack != []:
            currlevel, nextlevel = stack.pop(0), []
            level += 1
            for node in currlevel:
                if node.left == None and node.right == None:
                    return level
                else:
                    if node.left:
                        nextlevel.append(node.left)
                    if node.right:
                        nextlevel.append(node.right)
            stack.append(nextlevel)
        
"""
https://leetcode-cn.com/submissions/detail/100473285/

41 / 41 个通过测试用例
状态：通过
执行用时：40 ms
内存消耗：15.6 MB
"""
"""
执行用时：40 ms, 在所有 Python 提交中击败了37.68%的用户
内存消耗：15.6 MB, 在所有 Python 提交中击败了43.32%的用户
"""
