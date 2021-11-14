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
            if end != n:
                if sublen % 2 == 0:
                    tmplist = reversed(tmplist)
                vals2.extend(tmplist)
            if end == n:
                if (end - start) % 2 == 0:
                    tmplist = reversed(tmplist)
                vals2.extend(tmplist)
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
https://leetcode-cn.com/submissions/detail/238437992/

164 / 164 个通过测试用例
状态：通过
执行用时: 4176 ms
内存消耗: 122.6 MB
"""
