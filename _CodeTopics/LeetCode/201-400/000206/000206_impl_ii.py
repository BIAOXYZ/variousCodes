# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # 只改第一部分注释起来的语句，为了改成能和下面while循环里的形式相近。但是改完发现其实更丑了。
        # 所以结论就是：对于逆转链表的最常规方法，
        # 要么像 `000206_optm.py`一样根本不考虑head是否为空，而是通过合适的赋值直接进入while循环。
        # 要么像 `000206.py` 一样仅考虑head是否为空，并在处理后进入while循环。
        # 而不是head和head.next一起考虑。

        if not head or not head.next:
            return head
        """
        pre = head.next
        curr = head.next.next
        head.next.next = head
        head.next = None
        """
        next = head.next.next
        head.next.next = head
        pre = head.next
        curr = next
        head.next = None

        while curr:
            next = curr.next
            curr.next = pre
            pre = curr
            curr = next
        return pre
        
"""
https://leetcode-cn.com/submissions/detail/118134011/

27 / 27 个通过测试用例
状态：通过
执行用时: 28 ms
内存消耗: 14.8 MB

执行用时：28 ms, 在所有 Python 提交中击败了47.22%的用户
内存消耗：14.8 MB, 在所有 Python 提交中击败了31.77%的用户
"""
