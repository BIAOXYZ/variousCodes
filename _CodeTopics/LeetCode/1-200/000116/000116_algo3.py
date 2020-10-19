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

        # BFS和递归共4种方式解决（最后3种击败了100%的用户） --  3，递归方式
        # https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node/solution/bfshe-di-gui-zui-hou-liang-chong-ji-bai-liao-100-2/

        def dfs_connect(leftNode, rightNode):
            if not leftNode:
                return
            leftNode.next = rightNode
            dfs_connect(leftNode.left, leftNode.right)
            if rightNode:
                dfs_connect(leftNode.right, rightNode.left)
            else:
                dfs_connect(leftNode.right, None)
        dfs_connect(root, None)
        return root
        
"""
https://leetcode-cn.com/submissions/detail/116414240/

58 / 58 个通过测试用例
状态：通过
执行用时: 56 ms
内存消耗: 15.9 MB

执行用时：56 ms, 在所有 Python 提交中击败了50.72%的用户
内存消耗：15.9 MB, 在所有 Python 提交中击败了5.22%的用户
"""
