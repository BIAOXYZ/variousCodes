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

        # 官方答案的实现，果然简单的不少。技巧主要在：
        # 1.把dummyHead当成curr，while循环里每次检测的是 curr.next 和 cur.next.next。
        #   这点我倒不是没想到，只是感觉用这种方式也还是不能解决第一个重复节点的删除问题。
        # 2.while循环里又用了一层while循环。
        #   其实这个我当时也有想到并写出来试过，但是当时的问题是我是用head当curr，但是curr都可能是要删除的。
        #   答案这里巧就巧在 **用dummHead当cur**，从而保证cur肯定有效。

        if not head:
            return head
        dummyHead = ListNode(0, head)

        cur = dummyHead
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                v = cur.next.val
                while cur.next and cur.next.val == v:
                    cur.next = cur.next.next
            else:
                cur = cur.next
        return dummyHead.next
        
"""
https://leetcode-cn.com/submissions/detail/160583958/

166 / 166 个通过测试用例
状态：通过
执行用时: 40 ms
内存消耗: 13 MB

执行用时：40 ms, 在所有 Python 提交中击败了11.15%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了70.23%的用户
"""
