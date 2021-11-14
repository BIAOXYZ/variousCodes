# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseEvenLengthGroups(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        cur = head
        vals = []
        while cur:
            vals.append(cur.val)
            cur = cur.next
        n = len(vals)
        
        vals2 = []
        start, sublen = 0, 1
        while start < n:
            end = min(start + sublen, n)
            tmplist = vals[start:end]
            if sublen % 2 == 0:
                tmplist = reversed(tmplist)
            vals2.extend(tmplist)
            if end == n:
                break
            start += sublen
            sublen += 1
        
        cur = dummy = ListNode(0)
        for i in range(n):
            tmp = ListNode(vals2[i])
            cur.next = tmp
            cur = tmp
        return dummy.next
    
"""
https://leetcode-cn.com/submissions/detail/238435368/

116 / 164 个通过测试用例
状态：解答错误

输入：
[0,4,2,1,3]
输出：
[0,2,4,1,3]
预期：
[0,2,4,3,1]
"""
