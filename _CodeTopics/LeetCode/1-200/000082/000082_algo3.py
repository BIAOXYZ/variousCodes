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

        # 递归实现

        dummyHead = ListNode(0, head)

        def delete_duplicates_from_dummy(dummy):
            if not dummy.next:
                return
            curr = dummy.next
            v = curr.val
            flag = "notMoved"
            while curr.next and curr.next.val == v:
                flag = "moved"
                curr = curr.next
            if flag == "notMoved":
                delete_duplicates_from_dummy(curr)
            else:
                dummy.next = curr.next
                delete_duplicates_from_dummy(dummy)

        delete_duplicates_from_dummy(dummyHead)
        return dummyHead.next
        
"""
https://leetcode-cn.com/submissions/detail/160645893/

166 / 166 个通过测试用例
状态：通过
执行用时: 36 ms
内存消耗: 13.1 MB

执行用时：36 ms, 在所有 Python 提交中击败了26.94%的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了36.67%的用户
"""
