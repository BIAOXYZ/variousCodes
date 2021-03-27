# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        if not head:
            return None
        
        curr = head
        prev = ListNode(0, head)
        length = 0
        while curr:
            length += 1
            prev = curr
            curr = curr.next
        tail = prev
        k %= length

        if k == 0:
            return head

        """ 
        # 上一个从head开始移动，这次从tail开始移动。不过这种实现需要先把tail的next设成head。
        # 等写完了发现和上一种（`000061.py`）也没有本质区别。。。
        """
        tail.next = head
        newTail = tail
        for i in range(length-k):
            newTail = newTail.next
        
        newHead = newTail.next
        newTail.next = None
        return newHead
        
"""
https://leetcode-cn.com/submissions/detail/160492247/

231 / 231 个通过测试用例
状态：通过
执行用时: 24 ms
内存消耗: 12.9 MB

执行用时：24 ms, 在所有 Python 提交中击败了69.97%的用户
内存消耗：12.9 MB, 在所有 Python 提交中击败了82.38%的用户
"""
