# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """

        # 上个实现（`000203_impl.py`），也就是类似官方答案的实现，while循环里不用curr判断，而是用prev.next来判断。        
        # 确实是个小trick，但是如果想用curr也不是不能。

        dummyHead = ListNode(0)
        dummyHead.next = head
        prev = dummyHead
        curr = head
       
        while curr:
            if curr.val != val:
                curr = curr.next
                prev = prev.next
            else:
                prev.next = curr.next
                curr = curr.next
        return dummyHead.next
        
"""
https://leetcode-cn.com/submissions/detail/184182435/

66 / 66 个通过测试用例
状态：通过
执行用时: 48 ms
内存消耗: 19.7 MB

执行用时：48 ms, 在所有 Python 提交中击败了91.07%的用户
内存消耗：19.7 MB, 在所有 Python 提交中击败了34.57%的用户
"""
