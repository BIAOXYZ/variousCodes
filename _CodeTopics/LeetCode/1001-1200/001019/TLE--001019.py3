# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:

        def linkedlist_to_list(head):
            res = []
            cur = head
            while cur:
                res.append(cur.val)
                cur = cur.next
            return res
        
        lis = linkedlist_to_list(head)
        n = len(lis)
        res = []
        for i in range(n):
            if i == n:
                res.append(0)
            else:
                j = i + 1
                while j < n and lis[j] <= lis[i]:
                    j += 1
                res.append(0) if j == n else res.append(lis[j])
        return res
        
"""
https://leetcode.cn/submissions/detail/422946362/

63 / 76 个通过测试用例
状态：超出时间限制
"""
