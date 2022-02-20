# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        """
        # 没看清题目，写了个更难的版本。。。比如 [0,3,1,0,4,5,2,0] 会输出 [0,4,0,11,0]
        
        currZero = head
        curr = head.next
        currSum = 0
        while curr:
            if curr.val == 0:
                if currSum > 0:
                    node = ListNode(currSum)
                    currZero.next = node
                    node.next = curr
                    currZero = curr
                    currSum = 0
            elif curr.val > 0:
                currSum += curr.val
            curr = curr.next
        return head
        """
        
        res = dummyHead = ListNode(0)
        curr = head
        currSum = 0
        while curr:
            if curr.val == 0:
                if currSum > 0:
                    node = ListNode(currSum)
                    dummyHead.next = node
                    dummyHead = node
                    currSum = 0
            elif curr.val > 0:
                currSum += curr.val
            curr = curr.next
        return res.next
    
"""
https://leetcode-cn.com/submissions/detail/270604232/

39 / 39 个通过测试用例
状态：通过
执行用时: 3588 ms
内存消耗: 193.8 MB
"""
