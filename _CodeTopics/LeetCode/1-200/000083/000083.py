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

        # 昨天的 LC82 比这个难，昨天那个要求是把所有重复的元素都删除，所以需要一个flag，同时情况也更多。
        # 这里首先写基于栈的实现，比昨天的 `000082.py` 还是简单多了。

        stk = []
        curr = head
        while curr:
            next = curr.next
            curr.next = None
            if not stk or stk[-1].val != curr.val:
                stk.append(curr)
            curr = next
        if stk:
            for i in range(1, len(stk)):
                stk[i-1].next = stk[i]
        return head
        
"""
https://leetcode-cn.com/submissions/detail/159896745/

165 / 165 个通过测试用例
状态：通过
执行用时: 24 ms
内存消耗: 12.9 MB

执行用时：24 ms, 在所有 Python 提交中击败了88.71%的用户
内存消耗：12.9 MB, 在所有 Python 提交中击败了96.96%的用户
"""
