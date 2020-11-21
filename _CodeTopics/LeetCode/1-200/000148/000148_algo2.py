# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    # LC21: `000021_optm2.py`
    def mergeTwoLists(self, l1, l2):
        dummyHead = ListNode(0)
        curr = dummyHead
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        if l1:
            curr.next = l1
        if l2:
            curr.next = l2
        return dummyHead.next
    # LC876: `000876_optm.py` + 额外的四句 slowPre 相关的语句。
    # 从而每次找到中点mid后，利用 slowPre 来断开链表的前半部分和 mid之后部分之间的连接。
    def middleNode(self, head):
        fast, slow = head, head
        slowPre = ListNode(0)
        slowPre.next = slow
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            slowPre = slowPre.next
        slowPre.next = None
        return slow
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # 使用归并排序，并且直接用之前两道题的已有代码。
        if not head or not head.next:
            return head
        mid = self.middleNode(head)
        head1 = self.sortList(head)
        head2 = self.sortList(mid)
        return self.mergeTwoLists(head1, head2)
        
"""
https://leetcode-cn.com/submissions/detail/125253598/

28 / 28 个通过测试用例
状态：通过
执行用时: 472 ms
内存消耗: 42.1 MB

执行用时：472 ms, 在所有 Python 提交中击败了8.79%的用户
内存消耗：42.1 MB, 在所有 Python 提交中击败了25.68%的用户
"""
