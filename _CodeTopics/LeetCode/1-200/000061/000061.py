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
        # 上一个故意错的提交的问题主要就是逻辑不对，应该是倒着移动k次，或者等价于正着移动 length-1-k 次。
        # 比如，假设有5个节点，k等于1或者3，试试就知道了。
        """
        newTail = head
        for i in range(length-1-k):
            newTail = newTail.next
        newHead = newTail.next

        newTail.next = None
        tail.next = head
        return newHead
        
"""
https://leetcode-cn.com/submissions/detail/160351197/

231 / 231 个通过测试用例
状态：通过
执行用时: 28 ms
内存消耗: 13.1 MB

执行用时：28 ms, 在所有 Python 提交中击败了45.64%的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了39.76%的用户
"""
