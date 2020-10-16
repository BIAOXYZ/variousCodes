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
        
        leftmost = root
        while leftmost:
            # 如果leftmost已经是叶子节点了，就可以直接结束了。
            if not leftmost.left and not leftmost.right:
                break
            curr = leftmost
            while curr:
                curr.left.next = curr.right
                if curr.next:
                    curr.right.next = curr.next.left
                else:
                    curr.right.next = None
                curr = curr.next
            leftmost = leftmost.left
        return root
        
"""
https://leetcode-cn.com/submissions/detail/116342891/

58 / 58 个通过测试用例
状态：通过
执行用时: 32 ms
内存消耗: 15.9 MB

执行用时：32 ms, 在所有 Python 提交中击败了100.00%的用户
内存消耗：15.9 MB, 在所有 Python 提交中击败了5.02%的用户
"""
