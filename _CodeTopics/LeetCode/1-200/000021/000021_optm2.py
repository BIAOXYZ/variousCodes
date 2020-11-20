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
        
"""
https://leetcode-cn.com/submissions/detail/125048697/

208 / 208 个通过测试用例
状态：通过
执行用时: 24 ms
内存消耗: 13.1 MB

执行用时：24 ms, 在所有 Python 提交中击败了70.96%的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了17.36%的用户
"""
"""
其实这个应该比前面一个（`000021_optm.py`）更快一点点的，不过这里比那个还慢就不是算法的原因了，就是执行环境的原因。
"""
