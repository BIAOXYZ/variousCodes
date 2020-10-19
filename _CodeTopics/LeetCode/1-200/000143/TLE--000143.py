# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """

        # 这题看架势就是递归：大致思想应该就是有个辅助的helper函数。调用helper(head)就
        # 会处理好head和tail，然后令tail指向helper(head.next)，依次类推。

        def reoder_head_and_tail(head):
            if not head:
                return None
            preTail, tail = ListNode(0, head), head
            while tail.next:
                tail = tail.next
                preTail = preTail.next
            # 断开倒数第二个节点和最后一个节点的链接，不然应该会有影响。
            preTail.next = None
            tail.next = reoder_head_and_tail(head.next)
            # 若只有一个节点，这一步不应该执行。
            if head != tail:
                head.next = tail
            return head
        
        return reoder_head_and_tail(head)
        
"""
https://leetcode-cn.com/submissions/detail/117094199/

12 / 13 个通过测试用例
状态：超出时间限制
"""
