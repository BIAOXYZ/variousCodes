# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # 普通的链表操作实现，不使用额外的栈。且无dummyHead版本。
        # 不想在while循环里带两个的判断，试试去掉一个。--> 这次去掉另一个。

        if not head:
            return None
        
        curr = head
        while curr.next:
            if curr.val != curr.next.val:
                curr = curr.next
            else:
                curr.next = curr.next.next
        return head
        
"""
https://leetcode-cn.com/submissions/detail/159900621/

165 / 165 个通过测试用例
状态：通过
执行用时: 28 ms
内存消耗: 12.9 MB

执行用时：28 ms, 在所有 Python 提交中击败了70.37%的用户
内存消耗：12.9 MB, 在所有 Python 提交中击败了93.70%的用户
"""
