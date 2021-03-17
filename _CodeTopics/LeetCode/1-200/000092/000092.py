# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """

        pre = None
        curr = head
        currInd = 1
        while currInd < left:
            pre = curr; curr = curr.next; currInd += 1
        
        mid1, mid2 = pre, curr

        pre = None
        # 这句当然是废话，但是主要是为了更符合一般性反转链表的步骤。
        curr = curr
        while currInd <= right:
            next = curr.next
            curr.next = pre
            pre = curr
            curr = next
            currInd += 1
        
        mid2.next = curr
        # 这里是为了处理 m 从 1 开始的情况。此时 mid1 为 None， mid1.next 不合法。
        if not mid1:
            return pre
        else:
            mid1.next = pre
            return head
        
"""
https://leetcode-cn.com/submissions/detail/156531897/

44 / 44 个通过测试用例
状态：通过
执行用时: 16 ms
内存消耗: 13 MB

执行用时：16 ms, 在所有 Python 提交中击败了85.52%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了96.03%的用户
"""
