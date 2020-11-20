# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        dummyHead = ListNode(0)
        curr = dummyHead

        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                nextNode = l1.next
                l1.next = None
                l1 = nextNode
            else:
                curr.next = l2
                nextNode = l2.next
                l2.next = None
                l2 = nextNode
            curr = curr.next
        # 下面这俩while应该不需要整成while循环了，因为是链表啊，后面的节点都是连着的
        # 所以猜测是换成if，并且不需要在一直next到空节点了。等会再提交下。
        while l1:
            curr.next = l1
            l1 = l1.next
            curr = curr.next
        while l2:
            curr.next = l2
            l2 = l2.next
            curr = curr.next
        return dummyHead.next
        
"""
https://leetcode-cn.com/submissions/detail/125044732/

208 / 208 个通过测试用例
状态：通过
执行用时: 28 ms
内存消耗: 13.1 MB

执行用时：28 ms, 在所有 Python 提交中击败了47.07%的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了8.66%的用户
"""
