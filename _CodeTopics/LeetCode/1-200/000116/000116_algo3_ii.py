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

        def dfs_connect(leftNode, rightNode):
            if not leftNode:
                return
            leftNode.next = rightNode
            dfs_connect(leftNode.left, leftNode.right)
            if rightNode:
                dfs_connect(leftNode.right, rightNode.left)
                dfs_connect(rightNode.left, rightNode.right)
            else:
                leftNode.right = None
        dfs_connect(root, None)
        return root
        
"""
https://leetcode-cn.com/submissions/detail/116433264/

58 / 58 个通过测试用例
状态：通过
执行用时: 188 ms
内存消耗: 15.8 MB

执行用时：188 ms, 在所有 Python 提交中击败了8.42%的用户
内存消耗：15.8 MB, 在所有 Python 提交中击败了5.22%的用户
"""
