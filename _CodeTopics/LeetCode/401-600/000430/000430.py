"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """

        if not head:
            return head

        res = []
        def flatten_one_level(curr):
            while curr:
                nextNode = curr.next
                curr.prev = None
                curr.next = None
                res.append(curr)
                if curr.child:
                    flatten_one_level(curr.child)
                    curr.child = None
                curr = nextNode
        
        flatten_one_level(head)
        for i in range(len(res)-1):
            res[i].next = res[i+1]
            res[i+1].prev = res[i]
        res[-1].next = None
        return head
        
"""
https://leetcode-cn.com/submissions/detail/222579276/

26 / 26 个通过测试用例
状态：通过
执行用时: 28 ms
内存消耗: 13.7 MB

执行用时：28 ms, 在所有 Python 提交中击败了57.78%的用户
内存消耗：13.7 MB, 在所有 Python 提交中击败了66.67%的用户
"""
