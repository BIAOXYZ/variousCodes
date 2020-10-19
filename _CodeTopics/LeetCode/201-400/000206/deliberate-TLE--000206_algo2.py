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

        if head == None or head.next == None:
            return head
        end = self.reverseList(head.next)
        head.next.next = head
        # 注释掉下面这行，输入为 [] 或 [1] 都能过，但是 [1,2] 或更多节点就死循环了。
        # head.next = None
        return end
        
"""
https://leetcode-cn.com/submissions/detail/104878505/

0 / 27 个通过测试用例
状态：超出时间限制

最后执行的输入：
[1,2,3,4,5]
"""
