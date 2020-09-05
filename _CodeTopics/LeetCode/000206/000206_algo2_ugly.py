# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    pre = None
    # 注意，head此时还没有出现，所以只能是用这种比较丑陋的写法。
    #curr = head
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        def reverse_adjacency(pre, curr):
            if not curr:
                return
            next = curr.next
            curr.next = pre
            pre = curr
            curr = next
            # 这一句更是丑陋之极了。。。但是因为变量作用域问题，没它还不行。
            self.pre = pre
            reverse_adjacency(pre, curr)

        reverse_adjacency(self.pre, head)
        return self.pre
        
"""
https://leetcode-cn.com/submissions/detail/104972566/

27 / 27 个通过测试用例
状态：通过
执行用时: 32 ms
内存消耗: 19.4 MB
"""
"""
执行用时：32 ms, 在所有 Python 提交中击败了24.48%的用户
内存消耗：19.4 MB, 在所有 Python 提交中击败了5.07%的用户
"""
