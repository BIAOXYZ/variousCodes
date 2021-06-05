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

        # 如果肯用个dummyHead（并且while循环里不是用curr判断，而是用prev.next来判断！），
        # 就不用单独考虑初始的head（以及之后的若干节点）不能用的问题了。

        dummyHead = ListNode(0)
        dummyHead.next = head
        prev = dummyHead
       
        while prev.next:
            if prev.next.val != val:
                prev = prev.next
            else:
                prev.next = prev.next.next
        return dummyHead.next
        
"""
https://leetcode-cn.com/submissions/detail/184181461/

66 / 66 个通过测试用例
状态：通过
执行用时: 68 ms
内存消耗: 19.8 MB

执行用时：68 ms, 在所有 Python 提交中击败了17.40%的用户
内存消耗：19.8 MB, 在所有 Python 提交中击败了28.89%的用户
"""
