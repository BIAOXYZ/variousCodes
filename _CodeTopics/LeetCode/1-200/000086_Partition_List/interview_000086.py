# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """

        small = curr_small = ListNode(0)
        large = curr_large = ListNode(0)

        while head:
            if head.val < x:
                curr_small.next = head
                curr_small = curr_small.next
                head = head.next
            else:
                curr_large.next = head
                curr_large = curr_large.next
                head = head.next

        # deal with the last node of large list and 
        # concatenate the two to obtain the final result 
        curr_large.next = None
        curr_small.next = large.next
        
        return small.next
"""
https://leetcode-cn.com/submissions/detail/54891785/

166 / 166 个通过测试用例
状态：通过
执行用时: 40 ms
内存消耗: 12.8 MB
"""
