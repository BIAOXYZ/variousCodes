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
            return root
        
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
https://leetcode-cn.com/submissions/detail/115967967/

58 / 58 个通过测试用例
状态：通过
执行用时: 52 ms
内存消耗: 15.7 MB

执行用时：52 ms, 在所有 Python 提交中击败了67.29%的用户
内存消耗：15.7 MB, 在所有 Python 提交中击败了5.08%的用户
"""
