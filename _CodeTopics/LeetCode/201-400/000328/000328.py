# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # 先用非原地的，两个list分别存储奇数节点和偶数节点。

        if not head or not head.next:
            return head
        curr = head
        stk1, stk2 = [], []
        flag = 1

        while curr:
            if flag == 1:
                stk1.append(curr)
                flag = 2
            else:
                stk2.append(curr)
                flag = 1
            curr = curr.next

        len1, len2 = len(stk1), len(stk2)
        for i in range(len1):
            if i > 0:
                stk1[i-1].next = stk1[i]
        for i in range(len2):
            if i > 0:
                stk2[i-1].next = stk2[i]
        
        # 这步是为了防止产生环。
        stk2[-1].next = None
        stk1[-1].next = stk2[0]
        return head
        
"""
https://leetcode-cn.com/submissions/detail/123072915/

71 / 71 个通过测试用例
状态：通过
执行用时: 32 ms
内存消耗: 16.6 MB

执行用时：32 ms, 在所有 Python 提交中击败了71.10%的用户
内存消耗：16.6 MB, 在所有 Python 提交中击败了9.38%的用户
"""
