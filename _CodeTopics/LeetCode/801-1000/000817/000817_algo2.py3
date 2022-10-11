# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:

        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        
        se = set(nums)
        res = 0
        inNumsFlag = False
        for val in vals:
            if val in se:
                if not inNumsFlag:
                    res += 1
                    inNumsFlag = True
            else:
                inNumsFlag = False
        return res
        
"""
https://leetcode.cn/submissions/detail/372136551/

执行用时：
84 ms
, 在所有 Python3 提交中击败了
50.33%
的用户
内存消耗：
20.5 MB
, 在所有 Python3 提交中击败了
9.80%
的用户
通过测试用例：
57 / 57
"""
