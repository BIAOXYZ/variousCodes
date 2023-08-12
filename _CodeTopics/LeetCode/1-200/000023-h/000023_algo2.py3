# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq as hpq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        n = len(lists)
        dummyHead = ListNode()
        curr = dummyHead
        hp = []
        hpq.heapify(hp)
        for i in range(n):
            if lists[i]:
                node, val = lists[i], lists[i].val
                hpq.heappush(hp, (val, i, node))

        while hp:
            _, i, node = hpq.heappop(hp)
            nextNode = node.next
            if nextNode:
                nextTuple = (nextNode.val, i, nextNode)
                hpq.heappush(hp, nextTuple)
            curr.next = node  
            curr = node
            node.next = None
        return dummyHead.next
        
"""
https://leetcode.cn/problems/merge-k-sorted-lists/submissions/455852816/

时间
详情
72ms
击败 81.41%使用 Python3 的用户
内存
详情
19.27mb
击败 43.04%使用 Python3 的用户
"""
