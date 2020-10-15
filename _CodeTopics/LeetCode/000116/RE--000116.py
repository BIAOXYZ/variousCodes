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

        stack = [root]
        while stack:
            length, nextLevel = len(stack), []
            for i, node in enumerate(stack):
                if node.left: nextLevel.append(node.left)
                if node.right: nextLevel.append(node.right)
                if i == 0:
                    preNode = node
                elif i != length-1:
                    preNode.next = node
                    preNode = node
                else:
                    preNode.next = node
            stack = nextLevel[:]
        return root
        
"""
https://leetcode-cn.com/submissions/detail/115964754/

1 / 58 个通过测试用例
状态：执行出错

执行出错信息：
Line 22: AttributeError: 'NoneType' object has no attribute 'left'
最后执行的输入：
[]
"""
