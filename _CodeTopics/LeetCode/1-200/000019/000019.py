# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        # 一上来其实先把进阶版的双指针算法写了。这里接着写最普通的：
        # 即先计算链表长度，然后有了长度后再做相应处理的算法。
        curr, length = head, 0
        while curr:
            length += 1
            curr = curr.next
        
        if n == length:
            return head.next
        
        pre = head
        stepNum = length - n - 1
        while stepNum > 0:
            pre = pre.next
            stepNum -= 1
        
        pre.next = pre.next.next
        return head
        
"""
https://leetcode-cn.com/submissions/detail/116715610/

208 / 208 个通过测试用例
状态：通过
执行用时: 24 ms
内存消耗: 13.2 MB

执行用时：24 ms, 在所有 Python 提交中击败了64.93%的用户
内存消耗：13.2 MB, 在所有 Python 提交中击败了5.26%的用户
"""
