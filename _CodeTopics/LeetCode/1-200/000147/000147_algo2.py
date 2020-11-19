# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head:
            return None
        
        pre, curr = head, head.next
        while curr:
            # 一般的插入排序都是从后开始搜索，但是（单）链表的场景下这样是不行的。只能反过来。
            # 这里先处理一下当前节点需要接到头节点之前的情形。
            if curr.val < head.val:
                pre.next = curr.next
                curr.next = head
                head = curr
                curr = pre.next
                continue
            
            comparePre, compareNode = head, head.next
            while compareNode != curr and curr.val >= compareNode.val:
                comparePre = compareNode
                compareNode = compareNode.next
            if compareNode == curr:
                pre = curr
                curr = curr.next
            else:
                nextNode = curr.next
                comparePre.next = curr
                curr.next = compareNode
                pre.next = nextNode
                curr = nextNode
        return head
        
"""
https://leetcode-cn.com/submissions/detail/124812770/

22 / 22 个通过测试用例
状态：通过
执行用时: 1452 ms
内存消耗: 16.2 MB

执行用时：1452 ms, 在所有 Python 提交中击败了35.95%的用户
内存消耗：16.2 MB, 在所有 Python 提交中击败了35.27%的用户
"""
