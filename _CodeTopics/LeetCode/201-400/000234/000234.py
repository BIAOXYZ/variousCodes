# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        
        def isPalindrome(l):
            length = len(l)
            left, right = 0, length-1
            while left < right:
                if l[left] != l[right]:
                    return False
                left += 1; right -= 1
            return True
        
        return isPalindrome(vals)
        
"""
https://leetcode-cn.com/submissions/detail/117934858/

26 / 26 个通过测试用例
状态：通过
执行用时: 76 ms
内存消耗: 31.6 MB

执行用时：76 ms, 在所有 Python 提交中击败了39.17%的用户
内存消耗：31.6 MB, 在所有 Python 提交中击败了17.39%的用户
"""
