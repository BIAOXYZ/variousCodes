# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # 普通的链表操作实现，不使用额外的栈。
        # 感觉第一大段（找到最靠前的合法head）和第二大段代码好像不少重复，但是目前还没去思考合并。

        if not head or not head.next:
            return head

        # 找到第一个合法的（也就是没有其他节点值和它相同的）head。
        flag = "NotEqual"
        while head.next:
            if head.next.val == head.val:
                flag = "Equal"
                head = head.next
            elif head.next.val != head.val:
                if flag == "NotEqual":
                    break
                else:
                    flag = "NotEqual"
                    head = head.next
        if flag == "Equal":
            return None
        dummyHead = ListNode(0, head)

        prev = ListNode(0, head)
        curr = head
        flag = "NotEqual"
        while curr and curr.next:
            if curr.val != curr.next.val:
                if flag == "NotEqual":
                    prev = curr
                    curr = curr.next
                elif flag == "Equal":
                    flag = "NotEqual"
                    prev.next = curr.next
                    curr = curr.next
            else:
                flag = "Equal"
                curr.next = curr.next.next
        # 如果循环结束了flag还是 "Equal"，说明当前prev指向的curr也不能要。
        if flag == "Equal":
            prev.next = None

        return dummyHead.next
        
"""
https://leetcode-cn.com/submissions/detail/160544826/

166 / 166 个通过测试用例
状态：通过
执行用时: 24 ms
内存消耗: 13.1 MB

执行用时：24 ms, 在所有 Python 提交中击败了89.79%的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了42.63%的用户
"""
