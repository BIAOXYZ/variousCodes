"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """

        if not root:
            return None
        
        stack = []
        if root.left:
            stack.append(root.left)
        if root.right:
            stack.append(root.right)
        
        while stack:
            nextLevel = []
            length = len(stack)
            for i in range(length):
                if i < length - 1:
                    stack[i].next = stack[i+1]
                for child in [stack[i].left, stack[i].right]:
                    if child:
                        nextLevel.append(child)
            stack = nextLevel
        return root
        
"""
https://leetcode-cn.com/submissions/detail/111992087/

55 / 55 个通过测试用例
状态：通过
执行用时: 36 ms
内存消耗: 15 MB

执行用时：36 ms, 在所有 Python 提交中击败了81.13%的用户
内存消耗：15 MB, 在所有 Python 提交中击败了31.49%的用户
"""
