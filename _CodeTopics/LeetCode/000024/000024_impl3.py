# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head or not head.next:
            return head
        
        res = head.next
        preNode, currNode, nextNode = None, head, head.next

        while currNode and nextNode:
            # 交换两节点指向
            nextnext = nextNode.next
            nextNode.next = currNode
            currNode.next = nextnext
            if preNode:
                preNode.next = nextNode
            # 为下一轮交换赋值
            preNode, currNode = currNode, nextnext
            if currNode:
                nextNode = currNode.next
        return res
        
"""
https://leetcode-cn.com/submissions/detail/115393836/

55 / 55 个通过测试用例
状态：通过
执行用时: 24 ms
内存消耗: 12.3 MB

执行用时：24 ms, 在所有 Python 提交中击败了43.33%的用户
内存消耗：12.3 MB, 在所有 Python 提交中击败了95.61%的用户
"""
