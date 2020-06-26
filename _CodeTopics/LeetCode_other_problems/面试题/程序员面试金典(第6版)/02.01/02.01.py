# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeDuplicateNodes(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head is None:
            return []
        
        valueList = [head.val]
        currNode = head
        nextNode = head.next
        while nextNode is not None:
            if nextNode.val not in valueList:
                valueList.append(nextNode.val)
                # 这句也不是多余的，因为有可能nextNode其实不是原来紧挨着的。
                currNode.next = nextNode
                currNode = nextNode
                nextNode = nextNode.next
            else:
                # 立刻先把currNode的next指针置空，以免这个已经是链表末尾最后一个node时会出现
                # 返回结果多一个节点。
                currNode.next = None
                nextNode = nextNode.next
        return head
     
"""
https://leetcode-cn.com/submissions/detail/82122498/

35 / 35 个通过测试用例
状态：通过
执行用时：1364 ms
内存消耗：23.5 MB
"""
