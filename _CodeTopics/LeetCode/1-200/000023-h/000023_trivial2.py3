# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        def remove_none(lis):
            length = len(lis)
            if length == 0:
                return
            for i in range(length-1, -1, -1):
                if lis[i] == None:
                    del lis[i]
        # 用一个函数专门来将那四个变量恢复到类似初始状态
        def reset_state(heads):
            remove_none(heads)
            nonlocal tmpMinVal
            nonlocal tmpNode
            nonlocal tmpInd
            tmpMinVal = float('inf')
            tmpNode = None
            tmpInd = -1            

        n = len(lists)
        dummyHead = ListNode()
        curr = dummyHead
        heads = [lists[i] for i in range(n)]
        remove_none(heads)
        tmpMinVal, tmpNode, tmpInd = float('inf'), None, -1
        while heads:
            for i, head in enumerate(heads):
                if head.val < tmpMinVal:
                    tmpMinVal = head.val
                    tmpNode = head
                    tmpInd = i
            if tmpNode:
                heads[tmpInd] = tmpNode.next
                tmpNode.next = None
                curr.next = tmpNode
                curr = tmpNode
            reset_state(heads)
        return dummyHead.next
        
"""
https://leetcode.cn/problems/merge-k-sorted-lists/submissions/455814387/

时间
详情
4420ms
击败 7.47%使用 Python3 的用户
内存
详情
19.04mb
击败 65.75%使用 Python3 的用户
"""
