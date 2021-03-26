# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        if not head:
            return None
        
        curr = head
        prev = ListNode(0, head)
        length = 0
        while curr:
            length += 1
            prev = curr
            curr = curr.next
        tail = prev
        k %= length

        """
        # 这里本来想的是直接开始移动k个位置，然后算出新的头节点和尾节点，但其实逻辑是有问题的。
        # 只对第一个用例是有效的，把 2 换成 1、3之类的数字都不行。
        [1,2,3,4,5]
        2
        """
        newTail = head
        for i in range(k):
            newTail = newTail.next
        newHead = newTail.next

        newTail.next = None
        tail.next = head
        return newHead
        
"""
https://leetcode-cn.com/submissions/detail/160345583/

16 / 231 个通过测试用例
状态：解答错误

输入：
[1]
0
输出：
[]
预期：
[1]
"""
