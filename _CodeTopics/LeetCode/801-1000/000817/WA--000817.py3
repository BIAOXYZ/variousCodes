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
        currMax = currNum = 0
        for val in vals:
            if val in se:
                currNum += 1
            else:
                currMax = max(currMax, currNum)
                currNum = 0
        currMax = max(currMax, currNum)
        return currMax
        
"""
https://leetcode.cn/submissions/detail/372135399/

6 / 57 个通过测试用例
状态：解答错误

输入：
[0,1,2]
[0,2]
输出：
1
预期结果：
2
"""
