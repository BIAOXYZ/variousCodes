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

        def is_leaf(node):
            return False if node.left or node.right else True

        def dfs_connect(node):
            if not node or is_leaf(node):
                return
            # 本层逻辑的处理。
            node.left.next = node.right
            if node.next:
                node.right.next= node.next.left
            # 递归处理下层。
            dfs_connect(node.left)
            dfs_connect(node.right)

        dfs_connect(root)
        return root
        
"""
https://leetcode-cn.com/submissions/detail/116436429/

58 / 58 个通过测试用例
状态：通过
执行用时: 48 ms
内存消耗: 16.1 MB

执行用时：48 ms, 在所有 Python 提交中击败了85.22%的用户
内存消耗：16.1 MB, 在所有 Python 提交中击败了5.22%的用户
"""
