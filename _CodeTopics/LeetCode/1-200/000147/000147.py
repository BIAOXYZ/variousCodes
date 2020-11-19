# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # 这个方法比较流氓。。。回避了题目想考察的知识点。也就是不搞那些链表操作，
        # 直接把每个节点和节点值形成复合list（注意节点要和其next断开），然后排序一下。
        # 最后把这些节点一个一个手动连起来。。。

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
https://leetcode-cn.com/submissions/detail/124809690/

22 / 22 个通过测试用例
状态：通过
执行用时: 36 ms
内存消耗: 16.9 MB

执行用时：36 ms, 在所有 Python 提交中击败了99.17%的用户
内存消耗：16.9 MB, 在所有 Python 提交中击败了12.45%的用户
"""
