# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        pre = None
        curr = head
        while curr:
            next = curr.next
            curr.next = pre
            pre = curr
            curr = next
        return pre
    
    def findMiddle(self, head):
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
    
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        middle = self.findMiddle(head)
        head1, head2 = head, self.reverseList(middle)
        while head2:
            if head1.val != head2.val:
                return False
            head1 = head1.next
            head2 = head2.next
        return True
        
"""
https://leetcode-cn.com/submissions/detail/118152496/

26 / 26 个通过测试用例
状态：通过
执行用时: 84 ms
内存消耗: 31.5 MB

执行用时：84 ms, 在所有 Python 提交中击败了20.24%的用户
内存消耗：31.5 MB, 在所有 Python 提交中击败了19.11%的用户
"""
