# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        fast = head
        for i in range(n-1):
            fast = fast.next
        # 如果fast的下一个节点已经是None了，说明已经到头了。也就是
        # 需要删掉的节点是正着数第一个节点。比如，输入为：
        # [1,2,3,4,5]
        # 5
        if not fast.next:
            return head.next

        slow, slowPre, slowPre.next = head, ListNode(0), head
        while fast.next:
            fast = fast.next
            slow = slow.next
            slowPre = slowPre.next
        
        slowPre.next = slow.next
        return head
        
"""
https://leetcode-cn.com/submissions/detail/116664791/

208 / 208 个通过测试用例
状态：通过
执行用时: 16 ms
内存消耗: 13.1 MB

执行用时：16 ms, 在所有 Python 提交中击败了95.98%的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了5.26%的用户
"""
