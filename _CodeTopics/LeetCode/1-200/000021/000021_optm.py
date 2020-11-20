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
        # 换成if应该就可以，不需要while循环；并且不用在往后继续next了。
        if l1:
            curr.next = l1
        if l2:
            curr.next = l2
        return dummyHead.next
        
"""
https://leetcode-cn.com/submissions/detail/125044795/

208 / 208 个通过测试用例
状态：通过
执行用时: 20 ms
内存消耗: 13.1 MB

执行用时：20 ms, 在所有 Python 提交中击败了89.44%的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了16.42%的用户
"""
