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
        
        n = len(lists)
        dummyHead = ListNode()
        curr = dummyHead
        heads = [lists[i] for i in range(n)]
        remove_none(heads)
        tmpMinVal = float('inf')
        tmpNode = None
        tmpInd = -1
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
            remove_none(heads)
            tmpMinVal = float('inf')
            tmpNode = None
            tmpInd = -1
        return dummyHead.next
        
"""
时间
4504ms
击败 7.32%使用 Python3 的用户

内存
18.88mb
击败 93.73%使用 Python3 的用户
"""
"""
【[:star:][`*`]】 得有一个多月两个月没做每日一题了，现在每天工作还是很卷（看看2023年5月--7月每日一题那里的记录就知道了），但是为了将来的不确定性做准备，还是要尽量坚持做！
"""
