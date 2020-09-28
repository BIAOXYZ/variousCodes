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
            return []
        
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
https://leetcode-cn.com/submissions/detail/111987363/

1 / 55 个通过测试用例
状态：执行出错

执行出错信息：
Line 109: TypeError: [] is not valid value for the expected return type Node
最后执行的输入：
[]
"""
