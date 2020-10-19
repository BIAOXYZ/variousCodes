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
        currNode, nextNode = head, head.next

        while True:
            if currNode:
                if nextNode:
                    # 交换两节点指向
                    nextnext = nextNode.next
                    nextNode.next = currNode
                    currNode.next = nextnext
                    # 为下一轮交换赋值
                    currNode = nextnext
                    if currNode:
                        nextNode = currNode.next
                else:
                    break
            else:
                break
        return res
        
"""
https://leetcode-cn.com/submissions/detail/115316601/

11 / 55 个通过测试用例
状态：解答错误

输入：
[1,2,3,4]
输出：
[2,1,3]
预期：
[2,1,4,3]
"""
