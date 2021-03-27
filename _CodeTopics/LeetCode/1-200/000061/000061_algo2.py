# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        if not head:
            return None
        
        curr = head
        prev = ListNode(0, head)
        length = 0
        while curr:
            length += 1
            prev = curr
            curr = curr.next
        tail = prev
        k %= length

        if k == 0:
            return head

        """ 
        # 准备用快慢指针法。由于移动k次，思考下会有如下事实：倒数第k个节点会变成新head，倒数第k+1个节点会变成新tail。
        # 举例如下：输入为[1,2,3,4,5]，k值举例讨论下。
        # 当k=1时，倒数第1个节点5会变成新head，倒数第1+1个节点4变成新tail，最终结果是：[5,1,2,3,4]。
        # 当k=2时，倒数第2个节点4会变成新head，倒数第2+1个节点3变成新tail，最终结果是：[4,5,1,2,3]。
        # 当k=3时，倒数第3个节点3会变成新head，倒数第3+1个节点2变成新tail，最终结果是：[3,4,5,1,2]。
        # 当k=4时，倒数第4个节点2会变成新head，倒数第4+1个节点1变成新tail，最终结果是：[2,3,4,5,1]。
        
        # 所以问题变成找到倒数第k+1个节点，然后它的下一个节点就是返回结果（新head），同时也得把它的nex设成None。
        """
        slow = fast = head
        while k + 1 > 0:
            fast = fast.next
            k -= 1
        while fast:
            fast = fast.next
            slow = slow.next
        
        res = slow.next
        slow.next = None
        # 这个算法由于需要用快慢指针找倒数第k+1个节点，所以也得把连接原始的head和tail的步骤推后。
        tail.next = head
        return res
        
"""
https://leetcode-cn.com/submissions/detail/160504930/

231 / 231 个通过测试用例
状态：通过
执行用时: 32 ms
内存消耗: 13.2 MB

执行用时：32 ms, 在所有 Python 提交中击败了22.48%的用户
内存消耗：13.2 MB, 在所有 Python 提交中击败了18.46%的用户
"""
