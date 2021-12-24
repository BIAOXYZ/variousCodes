from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isEvenOddTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        MAX_VAL = 10**6 + 1
        if not root:
            return "Error Input!"
        
        stk = deque([root])
        level = 0
        while stk:
            preVal = MAX_VAL if level == 1 else -MAX_VAL
            nextLevel = []
            for _ in range(len(stk)):
                node = stk.popleft()
                if (level == 1 and (node.val % 2 == 1 or node.val >= preVal)) or \
                    (level == 0 and (node.val % 2 == 0 or node.val <= preVal)):
                    return False
                else:
                    preVal = node.val
                    if node.left: nextLevel.append(node.left)
                    if node.right: nextLevel.append(node.right)
            stk = deque(nextLevel)
            level = (level + 1) % 2
        return True
        
"""
https://leetcode-cn.com/submissions/detail/251799993/

执行用时：472 ms, 在所有 Python 提交中击败了61.54%的用户
内存消耗：66.3 MB, 在所有 Python 提交中击败了7.69%的用户
通过测试用例：
105 / 105
"""
