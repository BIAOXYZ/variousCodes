# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        # 这题确实无聊。。。而且其实有点违背原地算法的意思，更像是脑筋急转弯- -
        node.val = node.next.val
        node.next = node.next.next
        
"""
https://leetcode-cn.com/submissions/detail/234550424/

执行用时：28 ms, 在所有 Python 提交中击败了26.93%的用户
内存消耗：13.5 MB, 在所有 Python 提交中击败了14.46%的用户
通过测试用例：
41 / 41
"""
