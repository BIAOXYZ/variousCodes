# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        curr = head
        dic = dict()
        while curr:
            if not dic.has_key(curr):
                dic[curr] = 1
                curr = curr.next
            else:
                return True
        return False
        
"""
https://leetcode-cn.com/submissions/detail/114198080/

17 / 17 个通过测试用例
状态：通过
执行用时: 32 ms
内存消耗: 19.7 MB

执行用时：32 ms, 在所有 Python 提交中击败了95.61%的用户
内存消耗：19.7 MB, 在所有 Python 提交中击败了5.05%的用户
"""
