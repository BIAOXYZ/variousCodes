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

        # 这个月很多栈的题，那就先用栈写一个。

        stk = []
        curr = head
        flag = "push"
        while curr:
            next = curr.next
            curr.next = None
            if not stk:
                stk.append(curr)
            elif stk[-1].val != curr.val:
                if flag == "push":
                    stk.append(curr)
                elif flag == "pop":
                    stk.pop()
                    stk.append(curr)
                    flag = "push"
            else:
                flag = "pop"
            curr = next
        # 如果只有一种元素，比如[1,1]，while循环完了以后第一个1还是在栈里，但是其实是需要pop出去的。
        if stk and flag == "pop":
            stk.pop()

        if not stk:
            return None
        for i in range(1, len(stk)):
            stk[i-1].next = stk[i]
        return stk[0]
        
"""
https://leetcode-cn.com/submissions/detail/159459351/

166 / 166 个通过测试用例
状态：通过
执行用时: 24 ms
内存消耗: 13 MB

执行用时：24 ms, 在所有 Python 提交中击败了88.94%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了78.71%的用户
"""
