"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """

        if not root:
            return 0
        
        depth = 0
        stk = [root]
        while stk:
            depth += 1
            nextLevel = []
            for node in stk:
                for child in node.children:
                    nextLevel.append(child)
            stk = nextLevel
        return depth
        
"""
https://leetcode-cn.com/submissions/detail/240657163/

执行用时：40 ms, 在所有 Python 提交中击败了30.00%的用户
内存消耗：16 MB, 在所有 Python 提交中击败了50.63%的用户
通过测试用例：
38 / 38
"""
