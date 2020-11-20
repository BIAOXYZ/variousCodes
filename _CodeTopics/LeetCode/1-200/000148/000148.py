# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # 和 `000147.py` 一模一样的代码，这种方法太“流氓”了，哈哈。

        if not head:
            return None
        
        curr, tmplist = head, []
        while curr:
            tmplist.append([curr.val, curr])
            nextNode = curr.next
            curr.next = None
            curr = nextNode
        
        tmplist.sort(key=lambda elem:elem[0])
        length = len(tmplist)
        for i in range(length-1):
            tmplist[i][1].next = tmplist[i+1][1]
        return tmplist[0][1]
        
"""
https://leetcode-cn.com/submissions/detail/125041807/

28 / 28 个通过测试用例
状态：通过
执行用时: 196 ms
内存消耗: 49.3 MB

执行用时：196 ms, 在所有 Python 提交中击败了85.69%的用户
内存消耗：49.3 MB, 在所有 Python 提交中击败了5.76%的用户
"""
